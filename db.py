import pymysql
import credential


def signup(name,username,password,email,phone_no):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )
    try:
        with conn.cursor() as curr:
            sql = "insert into usermaster (name,username,password,email,phone_no) value (%s,%s,%s,%s,%s)"
            phone_no=int(phone_no)
            curr.execute(sql,(name,username,password,email,phone_no))
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

