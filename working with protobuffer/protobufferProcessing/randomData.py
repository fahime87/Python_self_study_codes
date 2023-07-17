import configparser
import random
import college_pb2 as buAPI
from Models import  *
db = db_connector()




def createaRandomProtocData():
    college = buAPI.college()
    student_list = []
    course_list=[]
    for c in range(100):
        crs=buAPI.CollegCourse()
        crs.Unit=random.randint(1,3)
        crs.Name=F"Crs_name{c}"
        crs.id=c
        course_list.append(crs)
    for i  in range(5000):

        student1 = buAPI.Student()
        student1.National_id = i
        student1.Name = f"name{i}"
        student1.Gender = random.randint(1,2)

        student1.BirthDay.day = random.randint(1, 30)
        student1.BirthDay.mount = random.randint(1, 12)
        student1.BirthDay.year = 1400

        for p in range(3):
            phone = student1.phones.add()
            phone.number = f"num_{i}_{p}"
            phone.type = random.randint(0,2)

        for ad in range(2):
            add = student1.Address.add()
            add.country = f"country{i}-{ad}"
            add.city = f"city {i}-{ad}"
            add.street = f"street{i}-{ad}"

        n=random.randint(2,6)
        crs=random.choices(course_list,k=n)
        student1.Courses.extend(crs)

        student_list.append(student1)
    college.courseList.extend(course_list)
    college.studentList.extend(student_list)
    with open('college.bin', "wb") as f:
        f.write(college.SerializeToString())
        f.close()
    print (college)



if __name__ == "__main__":
    createaRandomProtocData()