pip install flask

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Terrence<h1>Welcome</h1>"

if __name__=='__main__':
    app.run()

pip install google_auth_oauthlib

pip freeze > requirements.txt

pip freeze

pip install -r requirements.txt

pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib

import os
import pathlib
import requests
from flask import Flask, session, abort, redirect, request, render_template
from flask_session import Session
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests

app = Flask("Google Login App") 
app.secret_key = "CodeSpecialist.com"

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

GOOGLE_CLIENT_ID = "303605692402-fejcovf91lj3olrvnp9g9as12mqaadfq.apps.googleusercontent.com"

current_folder = globals()['_dh'][0]

client_secrets_file = os.path.join(current_folder.parent, "Flask/client_secret.json")
#client_secrets_file = os.path.abspath('')

flow = Flow.from_client_secrets_file(client_secrets_file=client_secrets_file, scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"], redirect_uri="http://127.0.0.1:5000/callback")

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401) #Authorization required
        else:
            return function()
        
    return wrapper

@app.route("/login") 
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)
    

@app.route("/callback") 
def callback(): 
    flow.fetch_token(authorization_response=request.url)
    
    if not session["state"] == request.args["state"]:
        abort(500) #State does not match!
        
    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)
    
    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )
    
    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/protected_area")

 
@app.route("/logout") 
def logout(): 
    session.clear()
    return redirect("/")

@app.route("/") 
def index(): 
    return "Hello World <a href='/login'><button>Login</button></a>"

@app.route("/protected_area")
@login_is_required
def protected_area(): 
    return "Landing page! <a href='/logout'><button>Log Out</button></a>"

if __name__ == "__main__": 
    app.run(debug=True, use_reloader=False)

pip install py-session

import json

with open('client_secret.json', 'w') as f:
    print("The json file is created")

pip install Flask-Session

