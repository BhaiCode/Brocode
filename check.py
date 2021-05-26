import os
import sys,subprocess
import credential
import contextlib
import filecmp 
import db as api
import glob,time

# for only now i take submission id as a location after complition it must be taken from database
# question id as solution id
# alter queston table
to_check = []
def get_file(name,path):
    try:
        name = name + '.txt'
        with open(os.path.join(path,name),'w') as fp:
            pass
        path = str(path)+'/'+str(name)
        # print(os.path.relpath(path))
        return (os.path.relpath(path))
    except Exception as e:
        print(e)
        return -1

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

def del_file(loc):
    try:
        os.remove(loc) 
        print('Done')
        return 1
    except OSError as error:
        print(error)
        return 0    

# def check(ques_id,submission_id):
#     # test_case,act_out = api.get_check_need(ques_id)
#     # sub_file = api.get_sub_det(submission_id)
#     sub_file = "kjnbojhno.py"
#     if sub_file.endswith('.py'):
#         # sub_name = get_name(submission_id)
#         # name = str(submission_id)
#         # +str('yes') #yes used for name of question
#         # out = get_file(name)
#         out = "static/compiler/user/output/582096018400882.txt"
#         st = []
#         st = get_command('python3',"static/compiler/admin/solution/6p1uW0x8v4FB1t8.py",out)
        
#         test_case="static/compiler/admin/test_cases/6p1uW0x8v4FB1t8/input/test_case_1"
#         s=""
#         with open(out,'w+') as f:
#             with open(test_case,'r') as r:
#                 stattime = time.time()
#                 s = subprocess.run(st,stdin=r,stdout=f,stderr = f,text=True)
#                 print(time.time()-stattime)
#                 print(s)
#         print(s)
#         tag = 's'
#         # if result(str(out),str(act_out),tag):
#         #     api.sub_update(submission_id,out,"1")
#         #     return True
#         # else:
#         #     api.sub_update(submission_id,out,"0")
#         #     return False 
#     else: print("hahah")        
# check("hnhjn","ojhoiuhouihno")
def check(sub_id):
    q_id,sol_path = api.get_sub_det(sub_id)
    test_inp,test_out,time_limit,space = api.get_check_need(q_id)
    
    parent_dir = credential.out_path
    directory = str(sub_id)
    path = os.path.join(parent_dir,directory)
    os.mkdir(path)
    out_path = path

    # test_inp = test_inp 
    # test_out = test_out 
    test_in_files = os.listdir(test_inp)
    test_out_files = os.listdir(test_out)
    # sort(test_in_files)
    test_in_files.sort()
    test_out_files.sort()
    # sort(test_out_files)
    if sol_path.endswith('.py'):
        j=1
        max_time=0
        b=True
        for i in range(len(test_in_files)):
            # sub_name = get_name(submission_id)
            api.state_update(q_id,"running on"+str(i+1))
            name = "output_"+str(j)
            j+=1
            # +str('yes') #yes used for name of question
            out = get_file(name,out_path)
            if out==-1:
                break
            st = []
            st = get_command('python3',sol_path,out)
            s = ""
            start_time = 0
            end_time = 0
            test_path = test_inp +"/"+ test_in_files[i]
            out_test_path = test_out +"/"+ test_out_files[i]
            with open(out,'w+') as f:
                with open(test_path,'r') as r:
                    start_time = time.time()
                    s = subprocess.run(st,stdin=r,stdout=f,stderr = f,text=True)
                    end_time=time.time()
            time_taken = end_time-start_time
            if(s.returncode==1):
                api.sub_test_update(sub_id,out,"0","","error")
                b=False
                api.sub_update(sub_id,"error","0","0","executed")
                return

            if(end_time-start_time>=time_limit):
                api.sub_test_update(sub_id,out,time_limit,"","timelimit_exceed")
                b=False
                api.sub_update(sub_id,"timelimit_exceed","0","0","executed")
                return
            tag = 's'
            max_time = max(time_taken,max_time)
            if result(str(out),str(out_test_path),tag):
                api.sub_test_update(sub_id,out,time_taken,"0","correct")
            else:
                api.sub_test_update(sub_id,out,time_taken,"0","wrong")
                b=False
                api.sub_update(sub_id,"wrong answer on"+str(i+1),time_taken,"0","executed")
                return
        if b:
            api.sub_update(sub_id,"correct",max_time,"0","executed")      
            return
    

def queue_len():    
    return len(to_check)
def run():    
    while(len(to_check)!=0):
        id = to_check.pop(0)
        check(id)

# print(os.path.abspath('static/submission/test.py'))
# get_file('staticsubmissiontestyes')
