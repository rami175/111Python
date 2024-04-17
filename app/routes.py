from flask import Flask     #from the flask moudle import the flask class

app =Flask(__name__)        #create instance of the Flask class

@app.get("/")                #flask decorator that maps fuctions to routes
def index():
    me = {
        "first_name":"Rami",
        "last_name": "Mahmoud",
        "hobbies": "Travel",
        "is_online":True
    }
    
    return me