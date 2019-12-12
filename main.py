import pandas as pd



pd.set_option('display.max_colwidth', 8)
pd.set_option('display.max_colwidth', 10)
pd.options.display.float_format = '{:,.0f}'.format

#cleaning
data_listencount = 'set1.csv'
data_metasong = 'song_data.csv'
temp_df1 = pd.read_csv(data_listencount,header=None)
temp_df1.columns = ['user_id', 'song_id', 'listen_count']
temp_df2 = pd.read_csv(data_metasong)
song_df = pd.merge(temp_df1, temp_df2.drop_duplicates(['song_id']), on="song_id", how="left")
song_df.drop(song_df.tail(1).index,inplace=True)

#grouping
song_df['song'] = song_df["artist_name"] + ' - ' + song_df["title"]
grouped_song = song_df.groupby(['song']).agg({'listen_count':'count'}).reset_index()
grouped_song.drop(grouped_song.tail(1).index,inplace=True)
totallisten = grouped_song['listen_count'].sum()
grouped_song['percentage'] = grouped_song['listen_count'].div(totallisten)*100
grouped_song.sort_values(['listen_count', 'song'], ascending = [0,1],inplace=True)


#training and testing data
users = song_df['user_id'].unique()
songs = song_df['song'].unique()
from sklearn.model_selection import train_test_split
training_set, testing_set = train_test_split(song_df, test_size = 0.20, random_state=0)


#applying model
#calculate running time
import timeit
start = timeit.default_timer()

import model

CFmodel = model.CollaborativeFilter()
CFmodel.input(training_set, 'user_id', 'song')
#Get user's dislike list
CFmodel.dislike(["Florence + The Machine - You've Got The Love"])

#Generate recommendations according to a particular user id
user_id = users[17]
print("----------------------------------------------------------------------")
print("The user id is: ",user_id)
unique_items = CFmodel.user_unique_items(user_id)
print("Users' listening history: ")
print("----------------------------------------------------------------------")
for unique_item in unique_items:
    print(unique_item)


print("----------------------------------------------------------------------")
print("Personalized Recommendations:")
print("----------------------------------------------------------------------")

results = CFmodel.output(user_id)
print(results)
recommendlist = results["song"].tolist()


# stop = timeit.default_timer()
# print('Running Time: ', "{}s".format(stop - start))
# print("----------------------------------------------------------------------")
# print("")


#test for precison and recall
# import test
# sample_percentage = 0.01
#
# testinput = test.calculator(testing_set, training_set, CFmodel)
# (precision_list, recall_list) = testinput.wrapped_calculator(sample_percentage)
# print("----------------------------------------------------------------------")
# print("Precision list: ", precision_list)
# print("Recall list: ",recall_list)
# print("----------------------------------------------------------------------")



