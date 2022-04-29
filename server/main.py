from flask import Flask, jsonify, request 
from flask_cors import CORS
import requests 
import json
import json
import io

app = Flask(__name__)

app.config.from_object(__name__)
CORS(app, resources={r"/*":{'origins':"*"}})
#CORS(app, resources={r'/*':{'origins': 'http://localhost:3000',"allow_headers": "Access-Control-Allow-Origin"}})

@app.route('/<string:s>',methods=['GET'])
def movie(s):
    result={1:"Batman",2:"Superman",3:"Iron-man",4:"Hulk",5:"Thor",6:"Loki",7:"Spiderman",8:"Captain-America",9:"IT",10:"Joker"}
    r = requests.get("https://api.themoviedb.org/3/search/movie?api_key=80a99c25c9f9f65e580f9c9e19d1d737&query="+"batman"+ "&callback=?")
    content=r.text
    p=str(content)
    image_source=[]
    k=p[2:len(p)-1]
    m=json.loads(k)
    f=str(m['results'][0]['poster_path'])
    path_name='http://image.tmdb.org/t/p/w500/'+f
    image_source.append(path_name)
    return path_name
if __name__ == "__main__":
    app.run(debug=True)
