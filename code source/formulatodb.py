from sqlite3 import *
conn=connect('C:\sqlite\sword.db')
print 'open database'
db=conn.cursor()

db.execute('''CREATE TABLE formula
              ( IN1 INT ,
                IN2 INT ,
                OUT1 INT,
                res INT ,
                primary key (In1,in2)
               );''')

fin=open('formula.txt')
raw=fin.read().split()
for i in xrange(0,121):
    in1 = eval(raw[4*i])
    in2=eval(raw[4*i+1])
    out=eval(raw[4*i+2])
    res=eval(raw[4*i+3])
#(name typ ID num1 num2)
    db.execute("INSERT INTO formula (IN1,IN2,OUT1,res) \
      VALUES (?,?,?,?)",(in1,in2,out,res))
conn.commit()
conn.close()
