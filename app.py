from flask import Flask,render_template,redirect,request,session,flash,json,url_for,g
import db as api
import credential
from werkzeug.utils import secure_filename
import os
import sys
import random
import generator as gen

app = Flask(__name__)



app.secret_key=os.urandom(24)

@app.route('/')
def home():
    if 'username' in session:
        username=session['username']
        return render_template('index.html',username=username)  
    return redirect('/login')
    

@app.route('/signup',methods=['POST','GET'])
def sign_up():
    print
    if 'username' in session:
        username=session['username']
        return redirect('/')
    if(request.method=='POST'):
        form_details=request.form
        print(form_details)
        session['username']=request.form['username']
        data=api.signup(form_details['name'],form_details['username'],form_details['password'],form_details['email'],form_details['phone_no'],form_details['gender']) 
        if data == "usernameAlreadyExist":
            print('usernameAlreadyExist')
            return render_template('signup.html',error='usernameAlreadyExist') 
        if data == "emailAlreadyExist":
            print('emailAlreadyExist')
            return render_template('signup.html',error='emailAlreadyExist') 
        if data == "phone_noAlreadyExist":
            print('phone_noAlreadyExist')
            return render_template('signup.html',error='phone_noAlreadyExist') 
        flash('Hey, you signed in')
        return redirect('/')
    return render_template('signup.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if 'username' in session:
        username=session['username']
        print('user in session---')
        print(username)
        return redirect('/')
    
    if(request.method=='POST'):
        form_details=request.form
        session['username']=request.form['username']
        print(session['username'])
        data=api.login(form_details['username'],form_details['password'])
        if data == "UsernameDosenotExit":
            # flash('UsernameDosenotExit')
            print('UsernameDosenotExit')
            return render_template('login.html') 
        if data == "wrongPassword":
            # flash('wrongPassword')
            print('wrongPassword')
            return render_template('login.html')
        if data == "correctPassword":
            print('Successfully logged in')
            return redirect('/')
        
             
    return render_template('login.html')            


@app.route('/logout')
def logout():
    session.pop('username')
    print('You logged out')
    return redirect('/login')
    
    # return json.dumps({'status':'logout'})






@app.route('/api_check_name', methods=['POST'])
def api_check_name():
    data=request.get_data().decode("utf-8").split("=")[1]
    if(api.check_ques_name(data)==True):
        return json.dumps({'status':'0'})
    return json.dumps({'status':'1'})

@app.route('/api_question',methods=['POST','GET'])
def api_question():
    try:
        file1 = request.files['file1']
        file2 = request.files['file2']
        file3 = request.files['file3']    
        form_details = request.form
        l1=""
        l2=""
        l3 = ""
        filename = secure_filename(file1.filename)
        app.config['UPLOAD_FOLDER']=credential.path
        file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        l1=os.path.join(app.config['UPLOAD_FOLDER'], filename)
        filename = secure_filename(file2.filename)
        app.config['UPLOAD_FOLDER']=credential.path2
        file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))                
        l2 = os.path.join(app.config['UPLOAD_FOLDER'], filename)  
        app.config['UPLOAD_FOLDER']=credential.path3
        filename = secure_filename(file3.filename)
        file3.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))        
        l3 = os.path.join(app.config['UPLOAD_FOLDER'], filename)  
        q_key=gen.key()
        while api.check_qkey(q_key)==False:
            q_key=gen.key()
        api.new_question(q_key,l1,form_details['question_name'],l2,l3)
        return json.dumps({'status':'0'})
    except:
        return json.dumps({'status':'1'})   

@app.route('/admin', methods=['POST','GET'])
def new_question():
    return render_template('admin_question.html')






@app.before_request
def before_request():
    g.user=None

    if'user' in session:
        g.user=session['user']

if __name__ == '__main__':
    app.run(debug=True)