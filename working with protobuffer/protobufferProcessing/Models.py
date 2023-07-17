import mysql.connector
import configparser
from datetime import datetime as dt
from logInfo import log

class DataBaseInitial():
    def __init__(self,tagname):
        config_data = configparser.ConfigParser()
        # reading data
        config_data.read("conf.ini")
        # app configuration data
        database = config_data[tagname]

        self.mydb = mysql.connector.connect(
            host=database['host'],
            user=database['admin'],
            passwd=database['password'],
        )
        #print(dt.now(),"connected to masql server",database['host'],database['admin'],)
        self.mycursor=self.mydb.cursor()
        self.sqlScriptFile=database['script']

        with open(self.sqlScriptFile, 'r') as sql_file:
            try:
                result_iterator = self.mycursor.execute(sql_file.read(), multi=True)
                for res in result_iterator:
                    log("INIT DB",dt.now(), "","CREATE", res)
            except Exception as e:
                log("ERROR INIT DB",dt.now(),"","CREATE",e)


    def __del__(self):
        self.mydb.close()
        #print(dt.now(),"closing mysql server connection ")

class db_connector():
    mydb=""
    mycursor=""
    def __init__(self,tagname="database1"):
        config_data = configparser.ConfigParser()
        # reading data
        config_data.read("conf.ini")
        # app configuration data
        database = config_data[tagname]

        self.mydb = mysql.connector.connect(
            host=database['host'],
            user=database['admin'],
            passwd=database['password'],
            db=database['database']
        )
        #print(dt.now(),"connected to masql server",database['host'],", User:",database['admin'],", DataBase:",database['database'])
        self.mycursor=self.mydb.cursor()


    def __del__(self):
        self.mydb.close()
        #print(dt.now(),"closing mysql server connection ")

    def clear_database(self):
        Student_model().deleteAll()
        Course_model().deleteAll()
        Telephon_model().deleteAll()
        Address_model().deleteAll()
        Student_course_Model().deleteAll()
        Log_model().delete()

class Student_model(db_connector):
    table_name = 'STUDENT'
    def __init__(self, id=None, name=None, birthday=None, gender=None):
        super(Student_model, self).__init__()
        self.id = id
        self.name = name
        self.birthday = birthday
        self.gender = gender

    def savemany(self,list_):
        try:
            q = f"INSERT INTO {self.table_name} " \
                f"(ID,SNAME,GENDER,BIRTHDAY) " \
                f"VALUES (%s,%s,%s,%s)"
            self.mycursor.executemany(q,list_)
            self.mydb.commit()
            for el in list_:
                log("SUCCESS DB",dt.now(),self.table_name,"INSERT", el[0])
        except Exception as e:
            log("ERROR DB",dt.now(),self.table_name," INSERT ",e)

    def save(self):
        try:
            q = f"INSERT INTO {self.table_name} " \
                f"(ID,SNAME,GENDER,BIRTHDAY) " \
                f"VALUES ({self.id},\'{self.name}\',{self.gender},\'{self.birthday}\')"
            self.mycursor.execute(q)
            self.mydb.commit()
            log("SUCCESS DB",dt.now(),self.table_name, "INSERT ",self.id)
        except Exception as e:
            log("ERROR DB",dt.now(),self.table_name,"INSERT",e)

    def delete(self, id=None):
        if id == None:
            id = self.id
        try:
            q = f"DELETE FROM {self.table_name} " \
                f"WHERE ID={id}"

            self.mycursor.execute(q)
            self.mydb.commit()
            log("SUCCESS DB", dt.now(), self.table_name, " DELETE ", id)
        except Exception as e:
            log("ERROR DB", dt.now(), self.table_name, " DELETE ", 0)

    def deleteAll(self):
        try:
            q=f"SET FOREIGN_KEY_CHECKS = 0"
            self.mycursor.execute(q)

            q = f"TRUNCATE TABLE  {self.table_name} "
            self.mycursor.execute(q)

            q = f"SET FOREIGN_KEY_CHECKS = 1"
            self.mycursor.execute(q)
            self.mydb.commit()
            log("SUCCESS DB", dt.now(), self.table_name, " TRUNCATE", 0)
        except Exception as e:
            log("ERROR DB", dt.now(), self.table_name, " TRUNCATE", e)

    def update_row(self, name, bithday, gender):

        pass

    def get_all(self):
        try:
            q = f"SELECT * FROM {self.table_name} "
            self.mycursor.execute(q)
            students_data = self.mycursor.fetchall()
            for e in  students_data:
                log("SUCCESS DB", dt.now(), self.table_name, " SELECT ", 0)
            return students_data
        except Exception as e:
            log("ERROR DB", dt.now(), self.table_name, " SELECT ", e)

    def get(self, id=None):
        try:
            if id==None:
                id=self.id
            q = f"SELECT * FROM {self.table_name} " \
                f"where id={id} "
            self.mycursor.execute(q)
            student_data = self.mycursor.fetchone()
            log("SUCCESS DB", dt.now(), self.table_name, " SELECT ", id)
            return student_data
        except Exception as e:
            log("ERROR DB", dt.now(), self.table_name, " SELECT ", e)



class Course_model(db_connector):
    table_name = "COURSE"
    def __init__(self, id=None, name=None, unit=None):
        super(Course_model, self).__init__()
        self.id = id
        self.name = name
        self.unit = unit

    def savemany(self,list_):
        try:
            q = f"INSERT INTO {Course_model.table_name} " \
                f"(ID,CNAME,UNIT) " \
                f"VALUES (%s,%s,%s)"
            self.mycursor.executemany(q,list_)
            self.mydb.commit()
            for el in list_:
              log("SUCCESS DB",dt.now(),self.table_name,"INSERT", el[0])
        except Exception as e:
            log("ERROR DB",dt.now(),self.table_name," INSERT ",e)
    def save(self):
        try:
            q = f"INSERT INTO {self.table_name} " \
                f"(ID,CNAME,UNIT) " \
                f"VALUES ({self.id},\'{self.name}\',{self.unit}) "

            self.mycursor.execute(q)
            self.mydb.commit()
            log("SUCCESS DB",dt.now(),self.table_name,"INSERT", self.id)
        except Exception as e:
            log("ERROR DB", dt.now(), self.table_name, " INSERT ", e)

        """    def is_exist(self):

        q = f"SELECT FROM {self.table_name}" \
            f"WHERE ID={self.id}"

        self.mycursor.execute(q)
        student = self.mycursor.fetchone()

        if len(student) > 0:
            return True
        else:
            return False"""
    def delete(self, id=None):
        if id == None:
            id = self.id
        try:
            q = f"DELETE FROM {self.table_name} " \
                f"WHERE ID={id}"
            self.mycursor.execute(q)
            self.mydb.commit()
            log("SUCCESS DB", dt.now(), self.table_name, " DELETE ", id)
        except Exception as e:
            log("ERROR DB", dt.now(), self.table_name, " DELETE ", e)
    def deleteAll(self):
        try:
            q = f"SET FOREIGN_KEY_CHECKS = 0"
            self.mycursor.execute(q)
            q = f" TRUNCATE TABLE {self.table_name} "
            self.mycursor.execute(q)
            q = f"SET FOREIGN_KEY_CHECKS = 1"
            self.mycursor.execute(q)
            self.mydb.commit()
            log("SUCCESS DB", dt.now(), self.table_name, " TRUNCATE", 0)
        except Exception as e:
            log("ERROR DB", dt.now(), self.table_name, " TRUNCATE", e)
    def update_row(self, name, unit):
        pass
    def get_all(self):
        try:
            q = f"SELECT * FROM {self.table_name} "
            self.mycursor.execute(q)
            courses_data = self.mycursor.fetchall()
            return courses_data
            log("SUCCESS DB", dt.now(), self.table_name, " SELECT ", 0)
        except Exception as e:
            log("ERROR DB", dt.now(), self.table_name, " SELECT ", e)
    def get(self, id):
        try:
            q = f"SELECT * FROM {self.table_name} " \
                f"where id={id} "
            self.mycursor.execute(q)
            course_data = self.mycursor.fetch()
            log("SUCCESS DB", dt.now(), self.table_name, " SELECT ", id)
            return course_data

        except Exception as e:
            log("ERROR DB", dt.now(), self.table_name, " SELECT ", e)

class Telephon_model(db_connector):
    table_name = "TELEPHON"
    def __init__(self, st_id=None, num=None, type=None):
        super(Telephon_model, self).__init__()
        self.student_id = st_id
        self.number = num
        self.type = type

    def savemany(self,list_):
        try:
            q = f"INSERT INTO {Telephon_model.table_name}" \
                f"(STUDENT_ID,TNUMBER,TTYPE)" \
                f"VALUES (%s,%s,%s)"
            self.mycursor.executemany(q, list_)
            self.mydb.commit()
            for el in list_:
                log("SUCCESS DB",dt.now(),self.table_name,"INSERT", el[0])
        except Exception as e:
            log("ERROR DB",dt.now(),self.table_name," INSERT ",e)

    def save(self):
        try:
            q = f"INSERT INTO {self.table_name}" \
                f"(STUDENT_ID,TNUMBER,TTYPE)" \
                f"VALUES ({self.student_id},\'{self.number}\',{self.type})"
            self.mycursor.execute(q)
            self.mydb.commit()
            log("SUCCESS DB",dt.now(),self.table_name,"INSERT", self.id)
        except Exception as e:
            log("ERROR DB",dt.now(),self.table_name," INSERT ",e)

    def delete(self, id=None):
        try:
            if id == None:
                id = self.id
            q = f"DELETE FROM {self.table_name} " \
                f"WHERE STUDENT_ID={id}"

            self.mycursor.execute(q)
            self.mydb.commit()
            log("SUCCESS DB", dt.now(), self.table_name, " DELETE ", 0)
        except Exception as e:
            log("ERROR DB", dt.now(), self.table_name, " DELETE ", 0)

    def deleteAll(self):
        try:
            q = f"TRUNCATE TABLE  {self.table_name} "
            self.mycursor.execute(q)
            self.mydb.commit()
            log("SUCCESS DB", dt.now(), self.table_name, " TRUNCATE", 0)
        except Exception as e:
            log("ERROR DB", dt.now(), self.table_name, " TRUNCATE", 0)

    def update_row(self, num=None, type=None):
        pass

    def get_all(self, st_id):
        try:
            q = f"SELECT FROM {self.table_name}" \
                f"WHERE STUDENT_ID={st_id}"
            self.mycursor.execute(q)
            telephon_list = self.mycursor.fetchall()
            log("SUCCESS DB", dt.now(), self.table_name, " SELECT ", 0)
            return telephon_list
        except Exception as e:
            log("ERROR DB", dt.now(), self.table_name, " SELECT ", e)

class Address_model(db_connector):
    table_name = 'ADDRESS'
    def __init__(self, st_id=None, country=None, city=None, street=None):
        super(Address_model, self).__init__()
        self.student_id = st_id
        self.country = country
        self.city = city
        self.street = street

    def savemany(self,list_):
        try:
            q = f"INSERT INTO {self.table_name}" \
                f"(STUDENT_ID,COUNTRY,CITY,STREET)" \
                f"VALUES (%s,%s,%s,%s)"
            self.mycursor.executemany(q, list_)
            self.mydb.commit()
            for el in list_:
                log("SUCCESS DB",dt.now(),self.table_name,"INSERT", el[0])
        except Exception as e:
            log("ERROR DB",dt.now(),self.table_name," INSERT ",e)

    def save(self):
        try:
            q = f"INSERT INTO {self.table_name} " \
                f"(STUDENT_ID,COUNTRY,CITY,STREET)" \
                f"VALUES ({self.student_id},\'{self.country}\',\'{self.city}\',\'{self.street}\')"
            self.mycursor.execute(q)
            self.mydb.commit()
            log("SUCCESS DB",dt.now(),self.table_name,"INSERT", self.student_id)
        except Exception as e:
            log("ERROR DB",dt.now(),self.table_name," INSERT ",e)

    def delete(self, id=None):
        try:
            if id == None:
                id = self.id
            q = f"DELETE FROM {self.table_name} " \
                f"WHERE STUDENT_ID={id}"

            self.mycursor.execute(q)
            self.mydb.commit()
            log("SUCCESS DB", dt.now(), self.table_name, " DELETE ", id)
        except Exception as e:
            log("SUCCESS DB", dt.now(), self.table_name, " DElETE ", e)

    def deleteAll(self):
        try:
            q = f"TRUNCATE TABLE  {self.table_name} "
            self.mycursor.execute(q)
            self.mydb.commit()
            log("SUCCESS DB", dt.now(), self.table_name, " TRUNCATE", 0)
        except Exception as e:
            log("ERROR DB", dt.now(), self.table_name, " TRUNCATE", 0)

    def update_row(self, country=None, city=None, street=None):
        pass

    def get_all(self, st_id):
        try:
            q = f"SELECT FROM {self.table_name}" \
                f"WHERE STUDENT_ID={st_id}"
            self.mycursor.execute(q)
            address_list = self.mycursor.fetchall()
            log("SUCCESS DB", dt.now(), self.table_name, " SELECT ", 0)
            return address_list
        except Exception as e:
            log("ERROR DB", dt.now(), self.table_name, " SELECT ", e)

class Student_course_Model(db_connector):
    table_name = "STUDENT_COURSE"

    def __init__(self, s_id=None, c_id=None, term=None, score=None):
        super(Student_course_Model, self).__init__()
        self.student_id = s_id
        self.course_id = c_id
        self.term = term
        self.score = score

    def savemany(self,list_):
        try:
            q = f"INSERT INTO {Student_course_Model.table_name} " \
                f"(STUDENT_ID,COURSE_ID,TERM,SCORE)" \
                f"VALUES (%s,%s,%s,%s)"
            self.mycursor.executemany(q,list_)
            self.mydb.commit()
            for el in list_:
                log("SUCCESS DB",dt.now(),self.table_name,f"INSERT student{el[0]}", el[1])
        except Exception as e:
            log("ERROR DB",dt.now(),self.table_name," INSERT ",e)

    def save(self):
        try:
            q = f"INSERT INTO {self.table_name} " \
                f"(STUDENT_ID,COURSE_ID,TERM,SCORE)" \
                f"VALUES ({self.student_id},{self.course_id},{self.term},{self.score})"
            self.mycursor.execute(q)
            self.mydb.commit()
            log("SUCCESS DB",dt.now(),self.table_name,f"INSERT student{self.student_id}", self.course_id)
        except Exception as e:
            log("ERROR DB",dt.now(),self.table_name," INSERT ",e)

    def delete(self, s_id, c_id):
        try:
            q = f"DELETE FROM {self.table_name} " \
                f"WHERE STUDENT_ID={s_id} and COURSE_ID={c_id}"
            self.mycursor.execute(q)
            self.mydb.commit()
            log("SUCCESS DB", dt.now(), self.table_name, " DELETE ", s_id)
        except Exception as e:
            log("ERROR DB", dt.now(), self.table_name, " DELETE ", e)

    def deleteAll(self):
        try:
            q = f"TRUNCATE TABLE  {self.table_name} "
            self.mycursor.execute(q)
            self.mydb.commit()
            log("SUCCESS DB", dt.now(), self.table_name, " TRUNCATE", 0)
        except Exception as e:
            log("ERROR DB", dt.now(), self.table_name, " TRUNCATE", 0)

    def deleteBYStdentId(self, s_id):
        try:
            q = f"DELETE FROM {self.table_name} " \
                f"WHERE STUDENT_ID={s_id} "
            self.mycursor.execute(q)
            self.mydb.commit()
            log("SUCCESS DB", dt.now(), self.table_name, " DELETE ", s_id)
        except Exception as e:
            log("ERROR DB", dt.now(), self.table_name, " DELETE ", e)

    def deleteByCourseId(self, c_id):
        try:
            q = f"DELETE FROM {self.table_name} " \
                f"WHERE COURSE_ID={c_id}"
            self.mycursor.execute(q)
            self.mydb.commit()
            log("SUCCESS DB", dt.now(), self.table_name, " DELETE ", c_id)
        except Exception as e:
            log("ERROR DB", dt.now(), self.table_name, " DELETE ", e)

    def update_row(self, score=None, teacher=None):
        pass

    def get_all(self):
        try:
            q = f"SELECT * FROM {self.table_name}"
            self.mycursor.execute(q)
            recs = self.mycursor.fetchall()
            log("SUCCESS DB", dt.now(), self.table_name, " SELECT ", 0)
            return recs
        except Exception as e:
            log("ERROR DB", dt.now(), self.table_name, " SELECT ", e)

class Log_model(db_connector):
    tablename="DB_LOG"
    def __init__(self):
        super(Log_model,self).__init__()

    def savemany(self,list_):

        try:
            q=f"INSERT INTO {self.tablename}" \
              f"(LOG_TYPE,ACTION_MODULE,ACTION_TYPE,ACTION_DATE,MESSAGE)" \
              f"value (%s,%s,%s,%s,%s)"
            self.mycursor.executemany(q,list_)
            self.mydb.commit()
        except Exception as e:
            log("ERROR DB",dt.now(),"LOG_DB","INSERT",e)

    def save(self,type,name_db,action_t,action_d,ref):
        try:
            q = f"INSERT INTO {self.tablename}" \
                f"(LOG_TYPE,CTION_MODULE,ACTION_TYPE,ACTION_DATE,REF_ID)" \
                f"value (%s,%s,%s,%s,%s)"
            self.mycursor.execute(q,(type,name_db,action_t,action_d,ref))
            self.mydb.commit()
        except Exception as e:
             log("ERROR DB", dt.now(), "DB_log", "INSERT", e)
    def delete(self):
        try:
            q = f"TRUNCATE TABLE {self.tablename}"
            self.mycursor.execute(q)
            self.mydb.commit()
        except Exception as e:
            log("ERROR DB",dt.now(),"DB_log","TRUNCATE",e)
            exit()
    def get_all(self):
        try:
            q = f"SELECT * FROM {self.tablename}"
            self.mycursor.execute(q)
            data=self.mycursor.fetchall()
            return data
        except Exception as e:
            log("ERROR DB",dt.now(),"DB_log","SELECT",e)



