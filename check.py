import os
import sys,subprocess
import credential
import contextlib
import filecmp 
import db as api
# for only now i take submission id as a location after complition it must be taken from database
# question id as solution id
# alter queston table
def get_file(name):
    path = credential.out_path
    name = name + '.txt'
    with open(os.path.join(path,name),'w') as fp:
        pass
    path = str(path)+'/'+str(name)
    # print(os.path.relpath(path))
    return (os.path.relpath(path))

def get_command(compiler,file1,opfile):
    st = []
    st.append('python3')
    st.append(str(file1))
    st.append(str(opfile))
    return st

def result(sub_out,act_out,tag):
    if tag == 's':    
        r = filecmp.cmp(sub_out,act_out,shallow=False)
        return r
    elif tag == 'd':
        print('krna hai')



def get_name(name):
    sub_name = os.path.splitext(name)[0]
    # print(sub_name)
    # op = ''
    # sub_name = op.join(sub_name)
    return sub_name

def del_file(name):
    location = credential.out_path
    name = name + '.txt'
    path = os.path.join(location,name)
    try:
        os.remove(path) 
        print('Done')
    except OSError as error:
        print(error)    

def check(ques_id,submission_id):
    test_case,act_out = api.get_check_need(ques_id)
    sub_file = api.get_sub_det(submission_id)
    if sub_file.endswith('.py'):
        # sub_name = get_name(submission_id)
        name = str(submission_id)
        # +str('yes') #yes used for name of question
        out = get_file(name)
        st = []
        st = get_command('python3',sub_file,out)
        with open(out,'w+') as f:
            with open(test_case,'r') as r:
                s = subprocess.run(st,stdin=r,stdout=f,stderr = f,text=True)
        tag = 's'
        if result(str(out),str(act_out),tag):
            api.sub_update(submission_id,out,"1")
            return True
        else:
            api.sub_update(submission_id,out,"0")
            return False 
    else: print("hahah")        



# print(os.path.abspath('static/submission/test.py'))
# get_file('staticsubmissiontestyes')