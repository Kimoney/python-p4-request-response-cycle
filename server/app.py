#!/usr/bin/env python3
import os
from flask import Flask, request, current_app, g, make_response

app = Flask(__name__)

@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

# Without Response Objects
    
# @app.route('/')
# def index():
#     host = request.headers.get("Host")
#     appname = current_app.name
#     return f'''<h1>The host for this page is {host}</h1>
#                 <h2> The path of the application is on the user's device is {g.path} 
#                <h2>The name of this application is {appname}</h2>''', \
#                202

@app.route('/')
def index():
    host = request.headers.get("Host")
    appname = current_app.name
    response_body = f'''<h1>The host for this page is {host}</h1>
                 <h2> The path of the application is on the user's device is {g.path}
                 <h2>The name of this application is {appname}</h2>'''
    status_code = 200
    headers = {}

    return make_response(response_body, status_code, headers)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
