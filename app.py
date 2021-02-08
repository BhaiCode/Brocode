from flask import Flask,render_template,redirect,request,session,flash,json
import db as api
import credential
app = Flask(__name__)
app.secret_key=credential.secret_key

@app.route('/')
def home():
    if 'username' in session:
        username=session['username']
        return render_template('index.html')  
    return redirect('/login')

@app.route('/signup',methods=['POST','GET'])
def sign_up():
    if(request.method=='POST'):
        form_details=request.form
        # print(form_details)
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
            flash('Successfully logged in')
            return redirect('/')
        if data == "wrongPassword":
            flash('wrongPassword')
            return render_template('login.html')
        if data == "UsernameDosenotExit":
            flash('UsernameDosenotExit')
            return render_template('login.html')      
    return render_template('login.html')            

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username',None)
    flash('You logged out')
    return json.dumps({'status':'logout'})
if __name__ == '__main__':
    app.run(debug=True)