from flask import Flask,render_template,redirect,request,session,flash,json,url_for,g,make_response,Response
import db as api
import credential
from werkzeug.utils import secure_filename
import os
import sys
import random
import generator as gen
import check as compiler
app = Flask(__name__)



app.secret_key=credential.secret_key


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
    if 'username' in session:
        username=session['username']
        return redirect('/')
    if(request.method=='POST'):
        form_details=request.form
        print(form_details)
        data=api.signup(form_details['name'],form_details['username'],form_details['password'],form_details['email'],form_details['phone_no'],form_details['gender']) 
        if data == "usernameAlreadyExist":
            print('usernameAlreadyExist')
            return render_template('signup.html',error='usernameAlreadyExist') 
        session['username']=request.form['username']
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
            session['username']=request.form['username']
            print(session['username'])
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

# @app.route('/api_question',methods=['POST','GET'])
# def api_question():
#     try:
#         file1 = request.files['file1']
#         # file2 = request.files['file2']
#         # file3 = request.files['file3']    
#         # file4 = request.files['file4']   
#         # form_details = request.form
#         l1=""
#         # l2=""
#         # l3 = ""
#         q_key=gen.key()
#         while api.check_qkey(q_key):
#             q_key=gen.key()
#         name = q_key + '.pdf'
#         filename = secure_filename(name)
#         print(filename)
#         # app.config['UPLOAD_FOLDER']=credential.path
#         # file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         # l1=os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         f = drive.CreateFile({'title': filename})
#         print("hhahaha")
#         # f.SetContentFile(os.path.join(credential.drive_path,filename))
#         print("hhahaha22")
#         f.Upload()
#         print("hhahaha333")
#         f=None
#         l1 = os.path.join(credential.drive_path,filename)
#         print(l1)
#         # name = q_key + '.txt'
#         # filename = secure_filename(name)
#         # app.config['UPLOAD_FOLDER']=credential.path2
#         # file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))                
#         # l2 = os.path.join(app.config['UPLOAD_FOLDER'], filename)  
        
#         # ext = file3.filename.split('.')[-1]
#         # name = q_key + '.'+ext
#         # app.config['UPLOAD_FOLDER']=credential.path3
#         # filename = secure_filename(name)
#         # file3.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))        
#         # l3 = os.path.join(app.config['UPLOAD_FOLDER'], filename) 
        
#         # name = q_key + '.txt'
#         # app.config['UPLOAD_FOLDER']=credential.path4
#         # filename = secure_filename(name)
#         # file4.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))        
#         # l4 = os.path.join(app.config['UPLOAD_FOLDER'], filename)   
#         # api.new_question(q_key,l1,form_details['question_name'],l2,l3,l4,form_details['time_limit'])
#         return json.dumps({'status':'0'})
#     except Exception as e:
#         print(e)
#         return json.dumps({'status':'1'})   
@app.route('/api_question',methods=['POST','GET'])
def api_question():
    try:
        form_details = request.form
        sol = request.files['solution']

        
        # # create question key
        q_key=gen.key()
        while api.check_qkey(q_key):
            q_key=gen.key()

        ext = sol.filename.split('.')[-1]
        name = q_key + '.'+ext
        app.config['UPLOAD_FOLDER']=credential.path3
        filename = secure_filename(name)
        sol.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))        
        sol_path = os.path.join(app.config['UPLOAD_FOLDER'], filename) 

        directory = q_key
        parent_dir = credential.parent_dir
        path = os.path.join(parent_dir,q_key)
        os.mkdir(path)

        parent_dir = path
        directory = "input"
        path = os.path.join(parent_dir,directory)
        os.mkdir(path)
        test_path = path

        i=1
        for f in request.files.getlist('testfiles'):
            f.save(os.path.join(path,"test_case_"+str(i)))
            i+=1
        
        directory = "output"
        path = os.path.join(parent_dir,directory)
        os.mkdir(path)
        out_path = path

        i=1
        for f in request.files.getlist('opfiles'):
            f.save(os.path.join(path,"test_output_"+str(i)))
            i+=1
        
        q_path = credential.path
        q_name = str(q_key)+".txt"
        ques_path = os.path.join(q_path,q_name)
        # print(q)
        with open(ques_path,'w') as fl:
            fl.write(form_details['content'])
            fl.close()


        api.new_question(q_key,ques_path,form_details['name'],test_path,sol_path,out_path,form_details['timelimit'],form_details['spacelimit'])        

        return json.dumps({'status':'0'})
    except Exception as e:
        print(e)
        return json.dumps({'status':'1'})  

@app.route('/admin', methods=['POST','GET'])
def new_question():
    # if 'username' in session:
    #     return render_template('admin/admin_index.html')
    # return render_template('admin/admin_login.html')
    return render_template('admin/admin_index.html')


@app.route('/add_question',methods=['POST','GET'])
def add_question():
    return render_template('admin_question.html')

@app.route('/login_admin', methods=['POST','GET'])
def login_admin():
    try:
        form_details = request.form
        if form_details['username'] == credential.admin_username:
            if form_details['password'] == credential.admin_password:
                # session['username'] = credential.admin_username
                items= api.api_get_all()
                return render_template('admin/admin_index.html',items=items)
        return redirect('/admin')
    except Exception as e:
        print(e)    

@app.route('/delete_question',methods=['POST','GET'])
def delete_question():
    try:
        key = request.get_data().decode("utf-8")
        data = api.get_details(key)
        if compiler.del_file(data[0])==1:
            if compiler.del_file(data[1])==1:
                if compiler.del_file(data[2])==1:
                    if compiler.del_file(data[3])==1:
                        if api.delete_question(key)==1:
                            return json.dumps({'status':'1'})
                        else:
                            return json.dumps({'status':'0'})
                    else:
                        return json.dumps({'status':'0'})
                else:
                    return json.dumps({'status':'0'})            
            else:
                return json.dumps({'status':'0'})        
        else:
            return json.dumps({'status':'0'})        
    except Exception as e:    
        return json.dumps({'status':'0'})

# @app.before_request
# def before_request():
#     g.user=None

#     if'user' in session:
#         g.user=session['user']

@app.route('/question/<key>',methods=['POST','GET'])        
def show_question(key):
    q_loc,name,timelimit,space_limit = api.get_quest(key)
    # username=session['username']
    result = ""
    if "username" in session:
        result = api.get_result(session["username"],key)
    file = open(q_loc,'r+')
    data = file.read()
    # print(q_loc,name,timelimit,space_limit)
    # response = make_response( render_template('question.html', loc=loc,name=name,key=key))
    # response.headers['Content-Type']='application/pdf'
    # response.headers['Content-Disposition']='inline;'     
    # return  response  
    return  render_template('question.html', data=data,name=name,key=key,timelimit=timelimit,spacelimit=space_limit,result=result)  

@app.route('/submit',methods=['POST','GET'])
def submit():
    try:
        if "username" in session:
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
            api.submit(q,sub_id,username,"0","0",l1,"","queue","0")
            if compiler.queue_len() == 0:
                compiler.to_check.append(sub_id)
                compiler.run()
            else:
                compiler.to_check.append(sub_id)
            return json.dumps({'status':sub_id})
        else:
            return json.dumps({'status':'2'})        
    except Exception as e:   
        return json.dumps({'status':'1'}) 

@app.route('/api_check_username', methods=['POST'])
def api_check_username():
    # print("hello")
    data=request.get_data().decode("utf-8").split("=")[1]
    # print(data)
    if(api.check_username(data)==True):
        return json.dumps({'status':'0'})
    return json.dumps({'status':'1'})

#  data=request.get_data().decode("utf-8").split("=")[1]
#     if(api.check_ques_name(data)==True):
#         return json.dumps({'status':'0'})
#     return json.dumps({'status':'1'})

@app.route('/get_updates',methods=['POST','GET'])
def get_updates():
    try:
        data = request.get_data().decode("utf-8").split("=")[1]
        state = api.get_state(data)
        print(state)
        return json.dumps({'status':state})
    except Exception as e:
        print(e)
        return json.dumps({'status':'system error'})

if __name__ == '__main__':
    app.run(debug=True)
