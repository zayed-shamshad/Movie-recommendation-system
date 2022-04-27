from flask import Flask, jsonify, request 
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(__name__)
CORS(app, resources={r"/*":{'origins':"*"}})
#CORS(app, resources={r'/*':{'origins': 'http://localhost:3000',"allow_headers": "Access-Control-Allow-Origin"}})

@app.route('/<string:s>',methods=['GET'])
def movie(s):
    return(s)
if __name__ == "__main__":
    app.run(debug=True)