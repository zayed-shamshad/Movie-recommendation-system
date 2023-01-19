
import pandas as pd
from scipy.sparse import csr_matrix
import pickle
from sklearn.neighbors import NearestNeighbors as KNN

class Movie_Recommender():
    def __init__(self):
        self.movies = pd.read_csv('./data/movies.csv')
        self.ratings = pd.read_csv('./data/ratings.csv')
        self.final_dataset = None
        self.final = None
        self.knn = pickle.load(open('./Model/finalized_model.sav','rb'))
        #self.knn = None
    def prepare(self):
        self.final_dataset = self.ratings.pivot(index='movieId',columns='userId',values='rating')

        self.final_dataset.fillna(0, inplace = True)

        self.final_dataset.head()

        no_user_voted = self.ratings.groupby('movieId')['rating'].agg('count')
        no_movies_voted = self.ratings.groupby('userId')['rating'].agg('count')


        self.final_dataset = self.final_dataset.loc[no_user_voted[no_user_voted > 10].index,:]
        self.final_dataset = self.final_dataset.loc[:,no_movies_voted[no_movies_voted > 50].index]

        
        self.final = csr_matrix(self.final_dataset)
        self.final_dataset.reset_index(inplace = True)
        #self.knn = KNN(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
        #self.knn.fit(self.final)

    def find_reccs(self,movie_name):
        n_movies_to_reccomend = 10
        movie_list = self.movies[self.movies['title'].str.contains(movie_name)]  
        if len(movie_list):        
            movie_idx= movie_list.iloc[0]['movieId']
            movie_idx = self.final_dataset[self.final_dataset['movieId'] == movie_idx].index[0]
            distances , indices = self.knn.kneighbors(self.final[movie_idx],n_neighbors=n_movies_to_reccomend+1)    
            rec_movie_indices = sorted(list(zip(indices.squeeze().tolist(),distances.squeeze().tolist())),key=lambda x: x[1])[:0:-1]
            recommend_frame = []
            for val in rec_movie_indices:
                movie_idx = self.final_dataset.iloc[val[0]]['movieId']
                idx = self.movies[self.movies['movieId'] == movie_idx].index
                recommend_frame.append({'Title':self.movies.iloc[idx]['title'].values[0],'Distance':val[1]})
            df = pd.DataFrame(recommend_frame,index=range(1,n_movies_to_reccomend+1))
            return df
        else:
            return "No movies found. Please check your input"
    def recommend(self,movie_name):
        temp = self.find_reccs(movie_name)
        if(type(temp) == type('Zaid')):
            return ['']
        temp = temp.iloc[:,0:1].values
        mobie = []
        for i in range(len(temp)):
            temp[i][0] = temp[i][0].split()[:-1]
            s = ''
            for j in temp[i][0]:
                s+=j+" "
            temp[i] = s
            s = ''
            for j in temp[i][0].split(',')[::-1]:
                s+=j
            mobie.append(s)
        for i in range(len(mobie)):
            mobie[i] = mobie[i].strip()
        return mobie

        
if __name__ == '__main__':
    Recommender = Movie_Recommender()
    Recommender.prepare()
    print(Recommender.recommend("Iron Man"))
        
        




