import os
import sys,subprocess
import credential
import contextlib

# for only now i take submission id as a location after complition it must be taken from database
# question id as solution id
def check(ques_id,submission_id,user_id):
    if submission_id.endswith('.py'):
        sub_name = get_name(submission_id)
        name = str(sub_name)+str(user_id)
        out = get_file(name)
        st = []
        st = get_command('python3',submission_id,out)
        with open(out,'w+') as f:
            s = subprocess.run(st,stdout=f,stderr = f,text=True)

def get_command(compiler,file1,opfile):
    st = []
    st.append('python3')
    st.append(str(file1))
    st.append(str(opfile))
    return st

def get_name(name):
    sub_name = os.path.splitext(name)[0]
    sub_name = sub_name.split('/')
    op = ''
    sub_name = op.join(sub_name)
    return sub_name

def get_file(name):
    path = credential.out_path
    name = name + '.txt'
    with open(os.path.join(path,name),'w') as fp:
        pass
    path = str(path)+'/'+str(name)
    # print(os.path.relpath(path))
    return (os.path.relpath(path))

def del_file(name):
    location = credential.out_path
    name = name + '.txt'
    path = os.path.join(location,name)
    try:
        os.remove(path) 
        print('Done')
    except OSError as error:
        print(error)    

# print(os.path.abspath('static/submission/test.py'))
check('haha','static/submission/test.py','yes')
# get_file('staticsubmissiontestyes')