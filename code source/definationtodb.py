from sqlite3 import *
conn=connect('C:\sqlite\sword.db')
print 'open database'
db=conn.cursor()
db.execute('''CREATE TABLE ingre
              ( ID INT PRIMARY KEY,
                type INT,
                num1 INT,
                num2 INT  
               );''')
fin=open('defination.txt')
raw=fin.read().split()
for i in xrange(0,75):
    name = raw[5*i]
    typ=eval(raw[5*i+1])
    ID=eval(raw[5*i+2])
    num1=eval(raw[5*i+3])
    num2=eval(raw[5*i+4])
#(name typ ID num1 num2)
    db.execute("INSERT INTO ingre (ID,type,num1,num2) \
      VALUES (?,?,?,?)",(ID,typ,num1,num2))
conn.commit()
conn.close()
