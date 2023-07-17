import college_pb2 as collegeAPI
from Models import  *
from logInfo import log

class CollegeAPI():

    def __init__(self,filename):
        self.binary_file_name=filename

    def binaryFileProcessToDatabase(self,tag_name):
        college_=collegeAPI.college()
        binary_data=self.readBinaryDataFile(self.binary_file_name)
        college_.ParseFromString(binary_data)
        self.collegeParser(college_,tag_name)


    def collegeParser(self,college,tag):
        crs_id=[]
        crs_name=[]
        st_id=[]
        st_list = []
        course_list = []
        address_list = []
        tel_list = []
        student_crs_list = []
        try:
            for crs in college.courseList:
                unit=crs.Unit
                name=crs.Name
                id=crs.id

                if id not in crs_id and name not in crs_name:
                    course_list.append((id,name,unit))
                    crs_id.append(id)
                    crs_name.append(name)
                else:
                    log("ERROR DATA",dt.now(),"collgeAPI","COURSE ENCODING",F"DATA MISSING - Duplicate id {id}")
            for st in college.studentList:
                if st.National_id not in st_id:
                    st_id.append(st.National_id)
                    birthday = F"{st.BirthDay.year}_{st.BirthDay.mount}_{st.BirthDay.day}"
                    st_list.append((st.National_id, st.Name, st.Gender, birthday))
                    for ad in st.Address:
                        address_list.append((st.National_id, ad.country, ad.city, ad.street))
                    for ph in st.phones:
                        tel_list.append((st.National_id, ph.number, ph.type))
                    for crs in  st.Courses:
                        if crs.id in crs_id:
                            student_crs_list.append((st.National_id,crs.id, 8,0))
                        else:
                            log("ERROR DATA", dt.now(), "collgeAPI", "STUDENT_COURSE ENCODING", F" DATA MISSING _ EMPTY COURSE REF_id {id}")
                else:
                    log("ERROR DATA", dt.now(), "collgeAPI", "Student ENCODING", F"DATA MISSING _ Duplicate id {st.National_id}")
        except Exception:
            log("ERROR PRTOC",dt.now(),"COLLEGEAPI","READ",Exception)
            exit()
        self.fixDataToDb(Student_model,st_list,)
        self.fixDataToDb(Course_model,course_list,)
        self.fixDataToDb(Address_model,address_list,)
        self.fixDataToDb(Telephon_model,tel_list,)
        self.fixDataToDb(Student_course_Model,student_crs_list,)
        self.fixDataToDb(Log_model,log.list_)

    def fixDataToDb (self,modelname,list,):
        model=modelname()
        model.savemany(list)

    def readBinaryDataFile(self,filename):
        data=""
        #in this part we read binary file and make protoc instace of them and save them in the database
        try:
            with open(filename, "rb") as f:
                data=f.read()
                log("SUCCESS FILE", dt.now(), "collegeAPI", "READ", filename)
        except IOError:
            log("ERROR FILE",dt.now(),"collegeAPI","READ",IOError)
            exit()
        return data



