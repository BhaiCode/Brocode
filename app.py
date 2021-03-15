from flask import Flask,render_template,redirect,request,session,flash,json,url_for,g
import db as api
import credential
from werkzeug.utils import secure_filename
import os
import sys
import random
import generator as gen
import mysql.connector

app = Flask(__name__)

conn=mysql.connector.connect(host="localhost",user="root",password="Granger@7",database="brocode", buffered = True)
# ,auth_plugin="caching_sha2_password"
cursor=conn.cursor()

# app.secret_key=credential.secret_key
app.secret_key=os.urandom(24)

# if __name__ == '__main__'
#     app.run(debug=True)

@app.route('/')
def home():
    # if 'username' in session:
    #     username=session['username']
    #     return render_template('index.html')  
    # return redirect('/login')
    # items = api.api_get_all()
    # print(items)
    # return render_template('index.html',items=items)
    # if 'username' in session:
    #     username=session['username']
    #     return render_template('index.html')  
    # # return redirect('/login')
    if 'user_id' in session:
        return render_template('index.html') 
    else: 
        return redirect('/login') 

@app.route('/signup',methods=['POST','GET'])
def sign_up():
    if(request.method=='POST'):
        form_details=request.form
        # print(form_details)
        # session['username']=request.form['username']
        # api.signup(form_details['name'],form_details['username'],form_details['password'],form_details['email'],form_details['phone_no'],form_details['gender']) 
        flash('Hey, you signed in')
        return redirect('/login')
    return render_template('signup.html')

# @app.route('/login',methods=['POST','GET'])
# def login():
#     if(request.method=='POST'):
#         form_details=request.form
#         session['username']=request.form['username']
#         data=api.login(form_details['username'],form_details['password'])
#         if data == "correctPassword":
#             flash('Successfully logged in')
#             return redirect('/')
#         if data == "wrongPassword":
#             flash('wrongPassword')
#             return render_template('login.html')
#         if data == "UsernameDosenotExit":
#             flash('UsernameDosenotExit')
#             return render_template('login.html')      
#     return render_template('login.html')            

@app.route('/login_validation',methods=['POST'])
def login_validation():
    username=request.form.get('username')
    password=request.form.get('password')

    cursor.execute("""SELECT *FROM `usermaster` WHERE `username` LIKE '{}' AND `password` LIKE '{}' """.format(username,password))
    users=cursor.fetchall()
    print(users)

    if len(users)>0:
        session['user_id']=users[0][0]
        return render_template("index.html",username=username)
    else:
        return redirect('/login')

    # return "the emial is {} and the password is {} ".format(username,password)
@app.route('/add_user',methods=['POST'])
def add_user():
    name=request.form.get('name')
    email=request.form.get('email')
    password=request.form.get('password')
    username=request.form.get('username')
    phone_no=request.form.get('phone_no')
    gender=request.form.get('gender')
    cursor.execute("""INSERT INTO `usermaster` (`sno`,`name`,`username`,`password`,`email`,`phone_no`,`gender`) VALUES (NULL,'{}','{}','{}','{}','{}','{}') """.format(name,username,password,email,phone_no,gender))
    conn.commit()

    cursor.execute(""" SELECT *FROM  `usermaster` WHERE `username` LIKE '{}' """.format(username))
    myuser=cursor.fetchall()
    session['user_id']=myuser[0][0]
    return render_template("index.html",username=username)

@app.route('/login',methods=['POST','GET'])
def login():
    if 'user_id' in session:
        return render_template('index.html')
    # if request.method =='POST':
    #     session.pop('user',None)
    #     # data=api.login(form_details['username'],form_details['password'])
    #     if request.form['password'] == 'password':
    #         session['user'] = request.form['username']
    #         flash('Successfully logged innnn')
    #         return redirect(url_for('logged_in'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/login')
    # flash('You logged out')
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




@app.route('/logged_in')
def logged_in():
    # if g.user:
    #     return render_template('logged_in.html',user=session['user'])
    return render_template('logged_in.html')

@app.before_request
def before_request():
    g.user=None

    if'user' in session:
        g.user=session['user']

if __name__ == '__main__':
    app.run(debug=True)