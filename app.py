from flask import Flask,render_template,redirect,request
import db as api


app = Flask(__name__)

@app.route('/')
def hello_world():  
    return 'Hello, World!'

@app.route('/signup',methods=['POST','GET'])
def sign_up():
    if(request.method=='POST'):
        form_details=request.form
        # print(form_details)
        api.signup(form_details['name'],form_details['username'],form_details['password'],form_details['email'],form_details['phone_no']) 
        return redirect('/')
    return render_template('signup.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if(request.method=='POST'):
        form_details=request.form
        data=api.login(form_details['username'],form_details['password'])
        if data == "correctPassword":
            return redirect('/')
        if data == "wrongPassword":
            return render_template('login.html')
        if data == "UsernameDosenotExit":
            return render_template('login.html')
    return render_template('login.html')            

if __name__ == '__main__':
    app.run(debug=True)