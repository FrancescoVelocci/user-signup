from flask import Flask, request, redirect, render_template
import os
import cgi
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_pwd = request.form['verify_pwd']
    email = request.form['email']
    username_error = ""
    password_error = ""
    v_pwd_error = ""
    email_error = ""

    # error in user name
    if username == "" or " " in username or len(username)<3 or len(username)>20:
        username_error = "That's not a valid username"
    # error in password
    if password == "" or " " in password or len(password)<3 or len(password)>20:
        password = ""
        password_error = "That's not a valid password"
    # error in verify password
    if verify_pwd != password or verify_pwd == "" or len(verify_pwd)<3 or len(verify_pwd)>20:
        verify_pwd = ""
        v_pwd_error = "Passwords don't match"
    # error email
    #if email.count("@") != 1 or email.count(".") != 1 or " " in email or len(email)<3 or len(email)>20:
    if len(re.findall('@', email)) != 1 or email.count(".") != 1 or " " in email or len(email)<3 or len(email)>20:
        email_error = "That's not a valid email"

    #no error so welcome message
    if username_error == "" and password_error == "" and v_pwd_error == "" and email_error == "":
        return render_template('welcome.html', username=username)
    if not username_error and not password_error and not v_pwd_error and email == "":
        return render_template('welcome.html', username=username)
    
    #error messages
    else:
        return render_template(
        'index.html', 
        username = username,
        password = "",
        verify_pwd = "",
        email = email,
        username_error = username_error,
        password_error = password_error,
        v_pwd_error = v_pwd_error,
        email_error = email_error
        )

app.run()