import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
import pickle
from sklearn.neighbors import NearestNeighbors as KNN
import re
from tensorflow import keras 

class Movie_Recommender():
    def __init__(self):
        self.movies_names = pd.read_csv('./data/movies.csv')
        self.ratings = pd.read_csv('./data/ratings.csv')
        self.final_dataset = None
        self.final = None
        self.knn = pickle.load(open('./Model/knn_users_model.sav','rb'))
        self.Neural_network = pickle.load(open('./Model/NN_model.sav','rb'))
        #self.knn = None
    def clean(self):
        for i in range(len(self.movies_names)):
            temp = self.movies_names['title'][i].split()[:-1]
            s = ''
            for j in temp:
                s+=j+" "
            temp = s
            s = ''
            re.sub(r"[\([{})\]]", "", temp)
            for j in temp.split(',')[::-1]:
                s+=j
            temp = s
            temp = temp.strip()
            temp = temp.lower()
            re.sub('[^A-Za-z0-9]+', '', temp)
            self.movies_names['title'][i] = temp

    def prepare(self):
        self.users = self.ratings.userId.unique()
        self.movies = self.ratings.movieId.unique()
        self.userid2idx = {o:i for i,o in enumerate(self.users)}
        self.movieid2idx = {o:i for i,o in enumerate(self.movies)}
        self.ratings['userId'] = self.ratings['userId'].apply(lambda x: self.userid2idx[x])
        self.ratings['movieId'] = self.ratings['movieId'].apply(lambda x: self.movieid2idx[x])
        split = np.random.rand(len(self.ratings)) < 0.8
        self.train = self.ratings[split]
        self.valid = self.ratings[~split]
        self.utils = self.ratings.pivot(index='userId',columns='movieId',values='rating')
        self.util.fillna(0, inplace = True)
        self.final_users = csr_matrix(self.util)

    def encode_movies(self,names):
        n, m = self.final_users.shape
        arr = np.zeros((1,m),dtype = 'float32')

        count = 0
        for name in names:
            name = name.lower()
            movie_list = self.movies_names[self.movies_names['title'].str.contains(name)]
            if len(movie_list):        
                movie_idx= movie_list.iloc[0]['movieId']
                movie_idx = self.movies_names[self.movies_names['movieId'] == movie_idx].index[0]
                arr[0,movie_idx] = 5.0
                count+=1
        temp = csr_matrix(arr)
        if(count==0):
            return []
        else:
            return temp
    def find_reccs(self,inp):
        preds = self.Neural_network.predict([pd.Series([inp for i in range(len(self.movies))]),pd.Series([i for i in range(len(self.movies))])])
        preds = np.ndarray.flatten(preds)
        ids = [i for i in range(len(self.movies))]
        preds, ids = zip(*sorted(zip(preds, ids)))
        reccs = []
        for i in ids[:10]:
            reccs.append(self.movies_names[self.movies_names['movieId']==i]['title'].values[0])
        return reccs

    def recommend(self,movie_name):
        movie_name = movie_name.split(',')
        encoded_inp = self.encode_movies(encoded_inp)
        if len(encoded_inp)==0:
            return encoded_inp
        reccs = self.find_reccs(encoded_inp)
        return reccs
        
if __name__ == '__main__':
    Recommender = Movie_Recommender()
    Recommender.prepare()
    Recommender.clean()
    print(Recommender.recommend("Iron Man"))
        
        




