attribute=['sid','sname','city','contect']
records=[[1,'om','Bardoli',1234567890],
         [2,'sai','Surat',9987654321],
         [3,'ram','Vyara',112233445],
         [4,'gopal','Navsari',566778899],
         [5,'kishan','Vapi',119384758],]
li=[]
for i in range(5):
    sid=int(input("Enter Student Id:"))
    sname=input("Enter Student Name:")
    city=input("Enter Student's City:")
    contect=int(input("Enter Student Contect Number:"))
    l=[sid,sname,city,contect]
    li.append(l)
import csv
with open('student.csv','w',newline='')as csvfile:
    file=csv.writer(csvfile)
    file.writerow(attribute)
    file.writerows(records)
    file.writerows(li)

import csv
with open('student.csv','r')as read_obj:
    all_records=csv.reader(read_obj)
    for records in all_records:
        print(records)


