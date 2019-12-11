import numpy as np
import pandas as pd


class CollaborativeFilter():
    def __init__(self):
        self.training_set = None
        self.userID = None
        self.itemID = None
        self.songs_dict = None
        self.rev_songs_dict = None
        self.cooccurrence_mtx = None
        self.CFrecommendations = None
        self.dislikefilter = []

#input
    def input(self, training_set, userID, itemID):
        self.training_set = training_set
        self.userID = userID
        self.itemID = itemID

#dislike filter
    def dislike(self,dislist):
        self.dislikefilter = dislist

        return self.dislikefilter


# get unique items for an user
    def user_unique_items(self, user):
        user_data = self.training_set[self.training_set[self.userID] == user]
        unique_items = list(user_data[self.itemID].unique())

        return unique_items

# get unique users for an item
    def get_unique_users(self, item):
        item_data = self.training_set[self.training_set[self.itemID] == item]
        unique_users = set(item_data[self.userID].unique())

        return unique_users

# Get all unique items
    def get_all_items_training_set(self):
        all_items = list(self.training_set[self.itemID].unique())

        return all_items

# construct co-occurrence matrix
    def construct_cooccurrence_mtx(self, user_history, all_songs):
        unique_users_li = []
        for i in range(0, len(user_history)):
            unique_users_li.append(self.get_unique_users(user_history[i]))
        cooccurrence_mtx = np.matrix(np.zeros(shape=(len(user_history), len(all_songs))), float)

        for i in range(0, len(all_songs)):
            songs_data_i = self.training_set[self.training_set[self.itemID] == all_songs[i]]
            users_i = set(songs_data_i[self.userID].unique())
            #1: history matrix, intersection and union
            for j in range(0, len(user_history)):
                users_j = unique_users_li[j]
                userset_itsc = users_i.intersection(users_j)

                if len(userset_itsc) != 0:
                    userset_un = users_i.union(users_j)
                    # 2:similarity calculation
                    cooccurrence_mtx[j, i] = float(len(userset_itsc)) / float(len(userset_un))
                else:
                    cooccurrence_mtx[j, i] = 0
        return cooccurrence_mtx

#Generate top 10 recommendation list and output df
    def top_recommendations_df(self, user, cooccurrence_mtx, all_songs, user_history):
        #3: weighted average score
        columns = ['user ID', 'song', 'score', 'ranked']
        relevance_scores = cooccurrence_mtx.sum(axis=0) / float(cooccurrence_mtx.shape[0])
        relevance_scores = np.array(relevance_scores)[0].tolist()
        sorted_index = sorted(((e, i) for i, e in enumerate(list(relevance_scores))), reverse=True)
        df = pd.DataFrame(columns=columns)

        ranked = 1
        for i in range(0, len(sorted_index)):
            if all_songs[sorted_index[i][1]] not in user_history and all_songs[sorted_index[i][1]] not in self.dislikefilter and ranked <= 10 and ~np.isnan(sorted_index[i][0]):
                df.loc[len(df)] = [user, all_songs[sorted_index[i][1]], sorted_index[i][0], ranked]
                ranked = ranked + 1

        if df.shape[0] == 0:
            print("More listening history for this user is needed for making recommendations.")
            return -1
        else:
            return df


    #Final output
    def output(self, user):
        user_history = self.user_unique_items(user)
        all_songs = self.get_all_items_training_set()
        cooccurrence_mtx = self.construct_cooccurrence_mtx(user_history, all_songs)
        df_recommendations = self.top_recommendations_df(user, cooccurrence_mtx, all_songs, user_history)

        return df_recommendations