             DROP DATABASE IF EXISTS studentInfo;
             CREATE DATABASE studentInfo;
             USE studentInfo;

			 CREATE TABLE if NOT exists COURSE (
             ID INTEGER , 
             CNAME VARCHAR(255),
             UNIT INTEGER , 
             PRIMARY KEY (ID) ,
             CONSTRAINT U_C UNIQUE (CNAME));

             CREATE TABLE if NOT exists STUDENT (
             ID integer ,
             SNAME VARCHAR (255),
             BIRTHDAY VARCHAR (32),
             GENDER int,
             PRIMARY KEY (ID));

             CREATE TABLE if NOT exists TELEPHON (
             STUDENT_ID INTEGER ,
             TNUMBER VARCHAR (32),
             TTYPE int,
             FOREIGN KEY (STUDENT_ID) REFERENCES STUDENT(ID) ON DELETE CASCADE,
             CONSTRAINT U_PH UNIQUE (TNUMBER ));

             CREATE TABLE if NOT exists ADDRESS (
             STUDENT_ID INTEGER ,
             COUNTRY VARCHAR(255),
             CITY VARCHAR(255),
             STREET VARCHAR(255),
             FOREIGN KEY (STUDENT_ID) REFERENCES STUDENT(ID) ON DELETE CASCADE);

             CREATE TABLE if NOT exists STUDENT_COURSE (
             STUDENT_ID INTEGER ,
             COURSE_ID INTEGER ,
             TERM INTEGER ,
             SCORE INTEGER ,
             FOREIGN KEY (STUDENT_ID) REFERENCES STUDENT(ID) ON DELETE CASCADE,
             FOREIGN KEY (COURSE_ID) REFERENCES COURSE(ID) ON DELETE CASCADE ,
             CHECK (SCORE<=20));


             CREATE TABLE  IF NOT EXISTS DB_LOG(
                 LOG_TYPE varchar (32),
                 ACTION_MODULE VARCHAR (32),
                 ACTION_TYPE VARCHAR (32),
                 ACTION_DATE TIME ,
                 MESSAGE VARCHAR(255)
             );