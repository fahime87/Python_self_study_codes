import Models
from collegeAPI import CollegeAPI

def testCollegeAPI(filename,tagname):
    college = CollegeAPI(filename)
    college.binaryFileProcessToDatabase(tagname)
def get_ERROR_Log(db_connection):
    q=F"SELECT * FROM DB_LOG " \
      F"WHERE  LOCATE(\'ERROR\',LOG_TYPE)>0 "
    try:
        cr=db_connection.mycursor
        cr.execute(q)
        error=cr.fetchall()
        return error
    except Exception:
        print(Exception)

def runTestScript():
    file="college.bin"
    tage_name="database1"
    db_con=Models.db_connector(tage_name)
    db_con.clear_database()
    testCollegeAPI(file,tage_name)
    errors=get_ERROR_Log(db_con)
    if len(errors)>0:
        print("----------ERROR while encoding data--------------------------")
        for el in errors:
            print(el[4])
    else:
        print("------------------------well done! data encoding is done completely----------------------------")






