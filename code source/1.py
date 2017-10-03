from re import *
from sqlite3 import *

elemcode={}
codeelem={}
fullformula={}

conn=connect('C:\sqlite\sword.db')
print 'open database'
db=conn.cursor()

def GetElemCode():
    global elemcode
    global codeelem
    fin=open('defination.txt')
    raw=fin.read().split()
    for i in xrange(0,75):
        name = raw[5*i]
        typ=eval(raw[5*i+1])
        ID=eval(raw[5*i+2])
        num1=eval(raw[5*i+3])
        num2=eval(raw[5*i+4])
        elemcode[name]=ID
        codeelem[ID]=name
        
def elim(filename):
    fin=open(filename)
    text=fin.read()
    newstring=' '
    regex=r'\([^()]*\)'
    res,num=subn(regex,newstring,text)
    g=res.split()
    fin.close()
    return g

def getSpecialformula():

    global fullformula
    out=elim('3.txt')
    in1=elim('1.txt')
    in2=elim('2.txt')
    print len(in1),len(in2),len(out)
    j=0
    for i in in1:
        curdict=fullformula[i]
        curdict[in2[j]]=out[j]
        j+=1

def Write():
    fout=open(r'0.txt','w')
    fout.write('\t')
    
    for i in codeelem:
        name= codeelem[i]
        fout.write(name)
        fout.write('\t')
    fout.write('\n')
    for i in codeelem:
        name=codeelem[i]
        fout.write(name)
        fout.write('\t')
        curdict=fullformula[name]
        for j in codeelem:
            name2=codeelem[j]
            if curdict.has_key(name2):
                fout.write(curdict[name2])
                fout.write('\t')
            else:
                fout.write(r'NO\t')
        fout.write('\n')
    fout.close()

GetElemCode()
for curname in elemcode:
    curcode=elemcode[curname]
    curdict={}
    #get curtype and curnum1 curnum
    
    cursor=db.execute("SELECT * FROM ingre WHERE ID=?",(curcode,))
    for c in cursor:
        curtype=c[1]
        curnum1=c[2]
        curnum2=c[3]
    print codeelem[curcode],curtype
    for tmpname in elemcode:
        tmpcode=elemcode[tmpname]
        #get tmptype tmpnum1 tmpnum2
        cursor=db.execute("SELECT * FROM ingre WHERE ID=?",(tmpcode,))
        for c in cursor:
            tmptype=c[1]
            tmpnum1=c[2]
            tmpnum2=c[3]

        curformula=db.execute("SELECT * FROM formula WHERE IN1= ? AND IN2= ?",(curtype,tmptype))
        for c in curformula:
            outtype=c[2]
            outres=c[3]
        
        if abs(outres)==1000:
            if tmpnum1>=curnum1:
                outres=curnum1+tmpnum2
            else:
                outres=curnum2+tmpnum1
        else:
            outres+=max(curnum1,tmpnum1)

        #print codeelem[tmpcode],tmptype

        cursor=db.execute("SELECT * FROM ingre WHERE type=? AND num1 <= ? ORDER BY num1 DESC LIMIT 1",(outtype,outres))
        cursor=cursor.fetchall()
        if cursor==[]:
            curdict[tmpname]=""
            continue
        else:
            outid=cursor[0][0]

        #print codeelem[outid],outtype

        
        outname=codeelem[outid]
        curdict[tmpname]=outname

    fullformula[curname]=curdict

getSpecialformula()
Write()

 
