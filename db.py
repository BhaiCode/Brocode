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

def new_question(ques_id,ques_location,ques_name,ques_test_case_file,ques_sol,ques_output,time_limit):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )
    try:
        with conn.cursor() as curr:
            sql = "insert into ques_master (ques_id,ques_location,ques_name,ques_test_case_file,ques_sol,ques_output,time_limit) values (%s,%s,%s,%s,%s,%s,%s)"
            # print(ques_id,ques_location,ques_name,ques_test_case_file)
            time_limit = int(time_limit)
            curr.execute(sql,(ques_id,ques_location,ques_name,ques_test_case_file,ques_sol,ques_output,time_limit))
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
            sql = "select ques_location,ques_name from ques_master where ques_id=(%s)"
            curr.execute(sql,(ques_id))
            output = curr.fetchall()
            return output[0][0],output[0][1]
    except Exception as e:
        print(e)             

def submit(ques_id,sub_id,username,result,execut_time,sub_loc,out_loc):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )
    try:
        with conn.cursor() as curr:
            sql = "insert into sub_master (ques_id,sub_id,username,result,execut_time,sub_loc,out_loc) values (%s,%s,%s,%s,%s,%s,%s)"
            execut_time = int(execut_time)
            curr.execute(sql,(ques_id,sub_id,username,result,execut_time,sub_loc,out_loc))
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
            sql = "select ques_test_case_file,ques_output from ques_master where ques_id=(%s)"
            curr.execute(sql,(ques_id))
            output = curr.fetchall()
            return output[0][0],output[0][1]
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
            sql = "select sub_loc from sub_master where sub_id=(%s)"
            curr.execute(sql,(sub_id))
            output = curr.fetchone()
            return output[0]
    except Exception as e:
        print(e)  

def sub_update(sub_id,out_loc,result):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )   
    try:
        with conn.cursor() as curr:
            sql = "update sub_master set out_loc=(%s),result=(%s) where sub_id=(%s)"
            curr.execute(sql,(out_loc,result,sub_id))
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