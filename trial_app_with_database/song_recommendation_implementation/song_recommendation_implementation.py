import pandas as pd


#*** integrating datasets
#triplets_file = 'https://static.turi.com/datasets/millionsong/10000.txt'    # 3-columns, tablet-separated, no header
#songs_metadata_file = 'https://static.turi.com/datasets/millionsong/song_data.csv'  # song_id, title, release, artist_name, year
triplets_file = '10000.csv'    # 3-columns, tablet-separated, no header
songs_metadata_file = 'song_data.csv'  # song_id, title, release, artist_name, year

print('Reading the triplet file 10000.csv ...')
song_df_1 = pd.read_csv(triplets_file, header=None)
song_df_1.columns = ['user_id', 'song_id', 'listen_count']
print('Reading the song metadata file song_data.csv ...')
song_df_2 =  pd.read_csv(songs_metadata_file)
# merge song_df_1 and song_df_2 on the song_id column (and drop the duplicated song_id column)
print('Merging the two datasets ...')
song_df = pd.merge(song_df_1, song_df_2.drop_duplicates(['song_id']), on="song_id", how="left")

print('The result of the merging:')
print(song_df.head())  # visualize the beginning of song_df
print('The length of the merged dataset is ' + str(len(song_df)))


#*** data transformation

##song_grouped = song_df.groupby(['song']).agg({'listen_count': 'count'}).reset_index()
##grouped_sum = song_grouped['listen_count'].sum()
##song_grouped['percentage']  = song_grouped['listen_count'].div(grouped_sum)*100
##song_grouped.sort_values(['listen_count', 'song'], ascending = [0,1])
##
##print('The result of the grouping of the merged dataset:')
##song_grouped.head()  # visualize the beginning of song_df
##print('The length of the grouped dataset is ' + str(len(song_grouped)))



users = song_df['user_id'].unique()
print('There are totally ' + str(len(users)) + ' users.')
songs = song_df['song_id'].unique()
print('There are totally ' + str(len(songs)) + ' songs.')


print('\nSplitting the merged song dataset into training and test datasets ...')
from sklearn.model_selection import train_test_split
train_data, test_data = train_test_split(song_df, test_size = 0.20, random_state=0)




#*** popularity-based recommendation system

##import Recommenders
##pm = Recommenders.popularity_recommender_py()
##pm.create(train_data, 'user_id', 'song')
###user the popularity model to make some prediction
##user_id = users[5]
##pm.recommend(user_id)




#*** item similarity based collaborative filtering model

import Recommenders
is_model = Recommenders.item_similarity_recommender_py()
##is_model.create(train_data, 'user_id', 'song')
is_model.create(train_data, 'user_id', 'song_id')

#Print the songs for the user in training data
user_id = users[5]
user_items = is_model.get_user_items(user_id)
#
print("------------------------------------------------------------------------------------")
print("Training data songs for the user userid: %s:" % user_id)
print("------------------------------------------------------------------------------------")
for user_item in user_items:
    print(user_item)
print("----------------------------------------------------------------------")
print("Recommendation process going on:")
print("----------------------------------------------------------------------")
#Recommend songs for the user using personalized model
user_recommended_music = is_model.recommend(user_id)
print('The recommended music for the user:')
print(user_recommended_music)

print('\n')

music = 'U Smile - Justin Bieber'
similar_music = is_model.get_similar_items([music])
print('The music similar to ' + music + ':')
print(similar_music)


print('\n')


#*** Matrix Factorization based Recommender

#constants defining the dimensions of our User Rating Matrix (URM) MAX_PID = 4 
MAX_PID = 4
MAX_UID = 5

#Compute SVD of the user ratings matrix 
def computeSVD(urm, K):
    # using cython-0.29.13 sparsesvd-0.2.2
    from sparsesvd import sparsesvd
    U, s, Vt = sparsesvd(urm, K)      
    dim = (len(s), len(s))     
    S = np.zeros(dim, dtype=np.float32)     
    from scipy.sparse import csc_matrix
    import math as mt
    for i in range(0, len(s)):         
        S[i,i] = mt.sqrt(s[i])      
        U = csc_matrix(np.transpose(U), dtype=np.float32)     
        S = csc_matrix(S, dtype=np.float32)     
        Vt = csc_matrix(Vt, dtype=np.float32)          
        return U, S, Vt

#Compute estimated rating for the test user
def computeEstimatedRatings(urm, U, S, Vt, uTest, K, test):
    rightTerm = S*Vt
    estimatedRatings = np.zeros(shape=(MAX_UID, MAX_PID), dtype=np.float16)
    for userTest in uTest:
        prod = U[userTest, :]*rightTerm
        #we convert the vector to dense format in order to get the     #indices
        #of the movies with the best estimated ratings 
        estimatedRatings[userTest, :] = prod.todense()
        recom = (-estimatedRatings[userTest, :]).argsort()[:250]
    return recom


import numpy as np
from scipy.sparse import csc_matrix

#Used in SVD calculation (number of latent factors)
K=2
#Initialize a sample user rating matrix
urm = np.array([[3, 1, 2, 3],[4, 3, 4, 3],[3, 2, 1, 5], [1, 6, 5, 2], [5, 0,0 , 0]])
print('The user rating matrix (numpy array) urm = ')
print(urm)
urm = csc_matrix(urm, dtype=np.float32)
#Compute SVD of the input user ratings matrix
U, S, Vt = computeSVD(urm, K)
#Test user set as user_id 4 with ratings [0, 0, 5, 0]
uTest = [4]
print("User id for whom recommendations are needed: %d" % uTest[0])
#Get estimated rating for test user
print("Predicted ratings:")
uTest_recommended_items = computeEstimatedRatings(urm, U, S, Vt, uTest, K, True)
print(uTest_recommended_items)

