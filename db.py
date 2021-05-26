import pymysql
import credential


def signup(name,username,password,email,phone_no,gender):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )
    try:
        with conn.cursor() as curr:
            sql1 = "select username from usermaster where username=(%s)"
            curr.execute(sql1,username)
            output=curr.fetchone()
            print(output)
            if(output):
                return "usernameAlreadyExist"
            sql = "insert into usermaster (name,username,password,email,phone_no,gender) value (%s,%s,%s,%s,%s,%s)"
            phone_no=int(phone_no)
            curr.execute(sql,(name,username,password,email,phone_no,gender))
            conn.commit()
    except Exception as e:
        print(e)        


def login(username,password):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )
    try:
        with conn.cursor() as curr:
            sql = "select password from usermaster where username=(%s)"
            curr.execute(sql,username)
            output=curr.fetchone()
            if(output):
                if(password == output[0]):
                    return "correctPassword"
                else: return "wrongPassword"    
            else:
                return "UsernameDosenotExit"    
    except Exception as e:
        print(e)       

def new_question(ques_id,ques_location,ques_name,ques_test_case_file,ques_sol,ques_output,time_limit,space_limit):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )
    try:
        with conn.cursor() as curr:
            sql = "insert into ques_master (ques_id,ques_location,ques_name,ques_test_case_file,ques_sol,ques_output,time_limit,space_limit) values (%s,%s,%s,%s,%s,%s,%s,%s)"
            # print(ques_id,ques_location,ques_name,ques_test_case_file)
            time_limit = int(time_limit)
            space_limit = int(space_limit)
            curr.execute(sql,(ques_id,ques_location,ques_name,ques_test_case_file,ques_sol,ques_output,time_limit,space_limit))
            # print(ques_id,ques_location,ques_name,ques_test_case_file)
            conn.commit()
    except Exception as e:
        print(e)            

def check_qkey(key):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )
    try:
        with conn.cursor() as curr:
            sql = "select ques_id from ques_master where ques_id=(%s)"
            curr.execute(sql,(key))
            output = curr.fetchall()
            if len(output)==0:
                return False
            return True 
    except Exception as e:
        print(e)        

def check_ques_name(data):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )
    try:
        with conn.cursor() as curr:
            sql = "select * from ques_master where ques_name=(%s) limit 1"
            curr.execute(sql,(data))
            output = curr.fetchone()
            if(str(output)=="None"):
                return False
            return True
    except Exception as e:
        print(e)         

def api_get_all():
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )   
    try:
        with conn.cursor() as curr:
            sql = "select ques_name,ques_id from ques_master"
            curr.execute(sql)
            output = curr.fetchall()
            # sql = "select ques_id from ques_master"
            # curr.execute(sql)
            # output2 = curr.fetchall()
            # print(output)
            output = dict(output)
            # print(output)
            return output
    except Exception as e:
        print(e)      

def api_get_id():
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )   
    try:
        with conn.cursor() as curr:
            sql = "select ques_id from ques_master"
            curr.execute(sql)
            output = curr.fetchall()
            return output
    except Exception as e:
        print(e)  

def get_quest(ques_id):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    ) 
    try:
        with conn.cursor() as curr:
            sql = "select ques_location,ques_name,time_limit,space_limit from ques_master where ques_id=(%s)"
            curr.execute(sql,(ques_id))
            output = curr.fetchall()
            return output[0][0],output[0][1],output[0][2],output[0][3]
    except Exception as e:
        print(e)             

def submit(ques_id,sub_id,username,result,execut_time,sub_loc,out_loc,state,memory):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )
    try:
        with conn.cursor() as curr:
            sql = "insert into sub_master (ques_id,sub_id,username,result,execut_time,sub_loc,out_loc,state,memory_used) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            execut_time = int(execut_time)
            curr.execute(sql,(ques_id,sub_id,username,result,execut_time,sub_loc,out_loc,state,memory))
            conn.commit()
    except Exception as e:
        print(e)            


def get_check_need(ques_id):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )   
    try:
        with conn.cursor() as curr:
            sql = "select ques_test_case_file,ques_output,time_limit,space_limit from ques_master where ques_id=(%s)"
            curr.execute(sql,(ques_id))
            output = curr.fetchall()
            return output[0][0],output[0][1],output[0][2],output[0][3]
    except Exception as e:
        print(e)  

def get_sub_det(sub_id):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )   
    try:
        with conn.cursor() as curr:
            sql = "select ques_id,sub_loc from sub_master where sub_id=(%s)"
            curr.execute(sql,(sub_id))
            output = curr.fetchone()
            return output[0],output[1]
    except Exception as e:
        print(e)  

def sub_update(sub_id,result,execut_time,memory_used,state):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )   
    try:
        with conn.cursor() as curr:
            sql = "update sub_master set result=(%s),execut_time=(%s),memory_used=(%s),state=(%s) where sub_id=(%s)"
            print(execut_time,memory_used,state)
            curr.execute(sql,(result,execut_time,memory_used,state,sub_id))
            conn.commit()
    except Exception as e:
        print(e)

def check_subid(sub_id):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )   
    try:
        with conn.cursor() as curr:
            sql = "select sub_id from sub_master where sub_id=(%s)"
            curr.execute(sql,(sub_id))
            output = curr.fetchall()
            if len(output)==0:
                return False
            return True
    except Exception as e:
        print(e)

def check_username(data):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )
    try:
        with conn.cursor() as curr:
            sql = "select * from usermaster where username=(%s) limit 1"
            curr.execute(sql,(data))
            output = curr.fetchone()
            if(str(output)=="None"):
                return False
            return True
    except Exception as e:
        print(e)      

def get_details(key):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    ) 
    try:
        with conn.cursor() as curr:
            sql = 'select ques_location,ques_test_case_file,ques_sol,ques_output from ques_master where ques_id = (%s)'
            curr.execute(sql,key)
            output = curr.fetchall()
            return output[0]   
    except Exception as e:
        print(e)      

def delete_question(key):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    ) 
    try:
        with conn.cursor() as curr:
            sql = 'delete from ques_master where ques_id = (%s)'
            curr.execute(sql,key)
            conn.commit()
            return 1    
    except Exception as e:
        print(e)    
        return 0  

def sub_test_update(sub_id,out_loc,time_taken,memory_used,state):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )   
    try:
        with conn.cursor() as curr:
            sql = "insert into sub_result (sub_id,test_case,time_taken,memory_used,state) values (%s,%s,%s,%s,%s)"
            curr.execute(sql,(sub_id,out_loc,time_taken,memory_used,state))
            conn.commit()
    except Exception as e:
        print(e)       

def get_result(name,ques_id):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    ) 
    try:
        with conn.cursor() as curr:
            sql = 'select result,execut_time,sub_id,state from sub_master where username = (%s) and ques_id=(%s)'
            curr.execute(sql,(name,ques_id))
            output = curr.fetchall()
            # print(output)
            return output   
    except Exception as e:
        print(e)      
# get_result("sid","RLpfh1cCwTc347N")
def state_update(sub_id,state):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )  
    try:
        with conn.cursor() as curr:
            sql = "update sub_master set state=(%s) where sub_id=(%s)"
            # print(sub_id,state)
            curr.execute(sql,(state,sub_id))
            conn.commit()
    except Exception as e:
        print(e)        

def get_state(sub_id):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )  
    try:
        with conn.cursor() as curr:
            sql = "select state from sub_master where sub_id=(%s)"
            # print(sub_id,state)
            curr.execute(sql,(sub_id))
            output = curr.fetchone()
            return (output[0])
    except Exception as e:
        print(e)        
# state_update("988790171572078","inprogress")       
 
