
ff=open('0.txt')
nameID={}
IDname=[]
update=[]
prev=0
tail=0


name=ff.readline().split()
full=[]
j=0
for i in name:
    nameID[i]=j
    j+=1
    IDname.append(i)

l= len(IDname)
print "current number of ingre: "+str(l)

for i in xrange(0,l):
    tmp=[]
    name=ff.readline().split()
    for j in xrange(1,l+1):
        tmp.append(name[j])
    full.append(tmp)

ff.close()

price=l*[1000000]
record=l*[(-1,-1)]

fprice=open('price.txt')
raw=fprice.read().split()
rawname=raw[::2]
rawprice=raw[1::2]
j=0
for i in rawname:
    price[nameID[i]]=eval(rawprice[j])
    update.append(nameID[i])
    record[nameID[i]]=(0,0)
    j+=1
    tail+=1

for i in xrange(0,l):
    print IDname[i]+str(price[i])
def Update(cur):
    global update
    global tail
    global price
    global record
    global full
    global l
    for i in xrange(0,l):
        
        targetname=full[cur][i]
        targetID=nameID[targetname]
        
        if price[targetID]>price[cur]+price[i]:
            price[targetID]=price[cur]+price[i]
            record[targetID]=(cur,i)
            update.append(targetID)
            tail+=1
            
    for i in xrange(0,l):
        targetname=full[i][cur]
        targetID=nameID[targetname]
        if price[targetID]>price[cur]+price[i]:
            price[targetID]=price[cur]+price[i]
            record[targetID]=(i,cur)
            update.append(targetID)
            tail+=1






while tail!=prev:
    cur=update[prev]
    prev+=1
    Update(cur)

for i in xrange(0,l):
    print IDname[i]+'\t',
    if record[i]==(-1,-1):
        print '\tCannot Get'
    elif record[i]==(0,0):
        print str(price[i])+'\tBuy it'
    else:
        print str(price[i])+'\t'+IDname[record[i][0]]+'+'+IDname[record[i][1]]
        

        
    
        

        
    
        
