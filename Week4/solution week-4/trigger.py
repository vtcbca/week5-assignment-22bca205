import sqlite3 as sq
import datetime
con=sq.connect("contactmanagementsystem.db")
cur=con.cursor()
cur.execute("""create table if not exists contact
               ( cid int primary key,
                 fname text,
                 lname text,
                 contact number,
                 email text,
                 city text
                 check ( email like '%_@_%._%')
                );""")

cur.execute("""create table if not exists details_log
                (
                    
                    fname text,
                    lname text,
                    newcontact number,
                    oldcontact number,
                    datetime text,
                    operation text
                    
                )""")

cur.execute("""create trigger if not exists insertdata
               after insert on contact
               begin
                   insert into details_log
                   values(new.fname,new.lname,new.contact,'NULL',datetime('now'),'insert');
               end;
                   """)


cur.execute("""create trigger if not exists deletedata
               after delete on contact
               begin
                   insert into details_log
                   values(old.fname,old.lname,'NULL',old.contact,datetime('now'),'delete');
               end;
                   """)

cur.execute("""create trigger if not exists updatedata
               after update on contact
               begin
                   insert into details_log
                   values(new.fname,new.lname,new.contact,old.contact,datetime('now'),'update');
               end;
                   """)

def updaterecord(cd):
    newcon=int(input("Enter new Contact Number:"))
    cur.execute(f"Update contact set contact={newcon} where cid={cd};")

def deleterecord(cd):
    cur.execute(f"delete from contact where cid={cd}")


def searchrecord(cd):
    cur.execute(f"select * from contact where cid={cd}")
    row=cur.fetchall()
    print(row)

cur.execute("""insert into contact values
                (1,'hanuman','shah',6754321786,'hanuman@gmail.com','surat'),
                (2,'sita','prajapati',9876543214,'sita@gmail.com','vyara'),
                (3,'laksman','patel',9087987123,'laksman@gmail.com','tapi'),
                (4,'krishan','ahir',9012345678,'krishan@gmail.com','bardoli'),
                (5,'radha','bhagora',8865432167,'radha@gmail.com','baben');""")

updaterecord(2)

deleterecord(3)


cur.execute("select * from contact")
row=cur.fetchall()
for i in row:
    print(f"\nID:{i[0]}\nFname:{i[1]}\nLname:{i[2]}\nContact:{i[3]}\nEmail:{i[4]}\ncity:{i[5]}")

cur.execute("select * from details_log")
row1=cur.fetchall()
print(row1)
for i in row1:
    print(f"\nFname:{i[0]}\nLname:{i[1]}\nNew-contact:{i[2]}\nOld-Contact:{i[3]}\nDatetime:{i[4]}\nOperation:{i[5]}")


