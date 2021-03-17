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
            print(output)
            if(output):
                if(password == output[0]):
                    return "correctPassword"
                else: return "wrongPassword"    
            else:
                return "UsernameDosenotExit"    
    except Exception as e:
        print(e)       

def new_question(ques_id,ques_location,ques_name,ques_test_case_file,ques_sol,ques_output):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )
    try:
        with conn.cursor() as curr:
            sql = "insert into ques_master (ques_id,ques_location,ques_name,ques_test_case_file,ques_sol,ques_output) values (%s,%s,%s,%s,%s,%s)"
            # print(ques_id,ques_location,ques_name,ques_test_case_file)
            curr.execute(sql,(ques_id,ques_location,ques_name,ques_test_case_file,ques_sol,ques_output))
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
            sql = "select exist(select* from ques_master where ques_id=(%s))"
            curr.execute(sql,(key))
            output = curr.fetchone()
            if(output==1):
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
            sql = "select ques_location,ques_name from ques_master"
            curr.execute(sql)
            output = curr.fetchall()
            output = dict(output)
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
            sql = "select ques_location from ques_master where ques_id=(%s)"
            curr.execute(sql,(ques_id))
            output = curr.fetchone()
            return (output[0])
    except Exception as e:
        print(e) 
             