import random

class calculator():

    def __init__(self, testing_set, training_set, recommendationmodel):
        self.testing_set = testing_set
        self.training_set = training_set
        self.model = recommendationmodel
        self.sample_testing = None

        self.predicted_dict = dict()
        self.actual_dict = dict()

#random sample
    def get_random(self, mylist, percentage):
        k = int(len(mylist) * percentage)
        random.seed(0)
        index = random.sample(range(len(mylist)), k)
        random_result = [mylist[i] for i in index]

        return random_result

#list sampled testing data
    def get_sampled_users(self, percentage):
        commonusers_trainntest = list(set(self.testing_set['user_id'].unique()).intersection(set(self.training_set['user_id'].unique())))
        print("Number of users in both training and testing dataset: ", len(commonusers_trainntest))
        self.random_user_sampled = self.get_random(commonusers_trainntest, percentage)
        print("Number of users sampled: ",len(self.random_user_sampled))

# Generate recommendation results for sampled users:
    def get_sampled_recommendations(self):
        for user_id in self.random_user_sampled:
            print("Sampled user ID: ",user_id)
            recommend_results = self.model.output(user_id)
            self.predicted_dict[user_id] = list(recommend_results["song"])
            actual_results = self.testing_set[self.testing_set['user_id'] == user_id]
            self.actual_dict[user_id] = set(actual_results['song'].unique())

# Calculate precision and recall
    def get_precision_n_recall(self):
        cutoff_list = list(range(1, 11))
        precision_list = []
        recall_list = []
        sampled_number = len(self.random_user_sampled)

        for n in cutoff_list:
            precision_sum = 0
            recall_sum = 0
            precision_avg = 0
            recall_avg = 0


            for user_id in self.random_user_sampled:
                true_positive = set(self.predicted_dict[user_id][0:n]).intersection(self.actual_dict[user_id])
                testset = self.actual_dict[user_id]
                #true positive relevant to TP+FP (top 10 recommended songs)
                precision_sum += float(len(true_positive)) / float(len(testset))
                # true positive relevant to TP + FN(all songs)
                recall_sum += float(len(true_positive)) / float(n)

            precision_avg = precision_sum / float(sampled_number)
            recall_avg = recall_sum / float(sampled_number)
            precision_list.append(precision_avg)
            recall_list.append(recall_avg)

        return (precision_list, recall_list)


    def wrapped_calculator(self, percentage):
        self.get_sampled_users(percentage)
        self.get_sampled_recommendations()
        return self.get_precision_n_recall()