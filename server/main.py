from unittest import result
from flask import Flask, jsonify, request 
from flask_cors import CORS
from numpy import result_type
import requests 
import json
import json
import io

from load_data import Movie_Recommender

'''Loading the Data and Creating the instance for the model'''
from load_data import Movie_Recommender
Recommender = Movie_Recommender()
Recommender.prepare()

app = Flask(__name__)

app.config.from_object(__name__)
CORS(app, resources={r"/*":{'origins':"*"}})
#CORS(app, resources={r'/*':{'origins': 'http://localhost:3000',"allow_headers": "Access-Control-Allow-Origin"}})

@app.route('/<string:s>',methods=['GET'])
def movie(s):
    result_list = Recommender.recommend(s)
    result_dict = {}
    for i in range(len(result_list)):
        result_dict[i] = result_list[i]
    
    #result={1:"Batman",2:"Superman",3:"Iron-man",4:"Hulk",5:"Thor",6:"Loki",7:"Spiderman",8:"Captain-America",9:"IT",10:"Joker"}
    image_dict = {}
    overview_dict={}
    for movie_names in result_list:
        r = requests.get("https://api.themoviedb.org/3/search/movie?api_key=80a99c25c9f9f65e580f9c9e19d1d737&query="+movie_names+ "&callback=?")
        content=r.text
        p=str(content)
        k=p[2:len(p)-1]
        m=json.loads(k)
        f=str(m['results'][0]['poster_path'])
        path_name='http://image.tmdb.org/t/p/w500/'+f
        overview=str(m['results'][0]['overview'])
        image_dict[movie_names] = path_name
        overview_dict[movie_names]=overview
    info={}
    info['1']=image_dict
    info['2']=overview_dict
    return jsonify(info)
if __name__ == "__main__":
    app.run(debug=True)
