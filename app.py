from flask import Flask,render_template,redirect,request,session,flash,json,url_for,g
import db as api
import credential
from werkzeug.utils import secure_filename
import os
import sys
import random
import generator as gen
import check as compiler
app = Flask(__name__)



app.secret_key=os.urandom(24)

@app.route('/')
def home():
    if 'username' in session:
        username=session['username']
        items= api.api_get_all()
        return render_template('index.html',items=items,username=username)  
    return redirect('/login')
    
    # print(items,key)
    # return render_template('index.html',items=items)

@app.route('/signup',methods=['POST','GET'])
def sign_up():
    if(request.method=='POST'):
        form_details=request.form
        print(form_details)
        session['username']=request.form['username']
        api.signup(form_details['name'],form_details['username'],form_details['password'],form_details['email'],form_details['phone_no'],form_details['gender']) 
        flash('Hey, you signed in')
        return redirect('/')
    return render_template('signup.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if(request.method=='POST'):
        form_details=request.form
        session['username']=request.form['username']
        data=api.login(form_details['username'],form_details['password'])
        if data == "correctPassword":
            # flash('Successfully logged in')
            print('Successfully logged in')
            items= api.api_get_all()
            return redirect("/")
        if data == "wrongPassword":
            # flash('wrongPassword')
            print('wrongPassword')
            return render_template('login.html')
        if data == "UsernameDosenotExit":
            # flash('UsernameDosenotExit')
            print('UsernameDosenotExit')
            return render_template('login.html')      
    return render_template('login.html')            


@app.route('/logout')
def logout():
    # session.pop('user_id')
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
        file4 = request.files['file4']   
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
        app.config['UPLOAD_FOLDER']=credential.path4
        filename = secure_filename(file4.filename)
        file4.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))        
        l4 = os.path.join(app.config['UPLOAD_FOLDER'], filename)   
        q_key=gen.key()
        print("yes")
        while api.check_qkey(q_key):
            q_key=gen.key()
        print("hello")
        api.new_question(q_key,l1,form_details['question_name'],l2,l3,l4,form_details['time_limit'])
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

@app.route('/question/<key>',methods=['POST','GET'])        
def show_question(key):
    loc,name = api.get_quest(key)
    return render_template('question.html',loc=loc,name=name,key=key)

@app.route('/submit',methods=['POST','GET'])
def submit():
    try:
        f = request.files['file']
        q = request.form['ques_id']
        sub_id = gen.sub_id()
        while api.check_subid(sub_id):
            sub_id = gen.sub_id()
        f.filename = sub_id+".py"
        filename = secure_filename(f.filename)
        app.config['UPLOAD_FOLDER']=credential.sub_path
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        l1=os.path.join(app.config['UPLOAD_FOLDER'], filename)
        username = session['username']
        api.submit(q,sub_id,username,"0","0",l1,"")
        if compiler.check(q,sub_id)==True:
            print("helllo bro")
            return json.dumps({'status':'0'})
        else:
            print("kya kr rhe bhai")
            return json.dumps({'status':'1'}) 
    except Exception as e:   
        return json.dumps({'status':'1'}) 

if __name__ == '__main__':
    app.run(debug=True)