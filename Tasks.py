# Q1 

one=1.0
two="1"
three=1
a=(one,two,three)
print(a,type(a))

# Q2 

SampleData= [
    {"V":"S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"}, 
    {"VII":"S005"},
    {"V":"S009"},
    {"VIII":"S007"}
     ]
i=0
lis =[]
while(i<len(SampleData)):
    for x in SampleData[i].values():
        if x not in lis:
            lis.append(x)
    i=i+1
lis= set(lis)    
print(lis)


# Q3 

Sampledata2= {
    '1': ['a', 'b'],
     '2': ['c', 'd']
     }
lis=[]
for x in Sampledata2.values():
    lis.append(x)      

for x in range(len(lis)):
    if x==0:
        print(lis[x][x]+lis[x+1][x])
        print(lis[x][x]+lis[x+1][x+1])
    else:
        print(lis[x-1][x]+lis[x][x-1])
        print(lis[x-1][x]+lis[x][x])

# Q4

def myfunc():
  return lambda a,b : a+b

mytripler = myfunc()
c=int( input("Enter the no of series = "))
a=-1
b=-1
temp=-1
for i in range(c):
    if(i<=1):
        a=0
        b=1
        temp=b
        print(b)
        b=mytripler(a,b)
        a=temp
    else:
        temp=b
        b=mytripler(a,b)
        print(b)
        a=temp





# Q5

fruits = ["APPLE", "BANANNA", "CHERRY", "KIWI", "MANGO"]
newfruits=[]
for x in fruits:
    if len(x)>5:
        newfruits.append(x.lower())  
    else:
        newfruits.append(x)  

print(newfruits)

# Q6(a)

D={
    "2016-CS-700": [
        ("DSA",3),
         ("Algo",2.5),
          ("AI",3)
          ], 
 "2016-CS-701":[
     ("LA",3),
      ("Algo",3),
       ("PF",2.8)
       ],
}
# With For loop
temp=0
gpas=[]
for i in D.values():
    temp=0
    for a in i:
        temp+=a[1]*3  
    gpas.append(temp/9)    
a=0

for i in D.keys():
    print(f"{i} :  {gpas[a]}")
    a=a+1

# without For loop

o=0
i=0
lis=list(D.keys())
temp=0
gpa2=[]
while o<len(D.values()):
    temp=0
    i=0
    while i<len(D[lis[o]]):
        temp=temp+D[lis[o]][i][1]*3
        i+=1
    o+=1
    gpa2.append(temp/9)

print(gpa2)    

# Q6 (b)

D2={
    "2016-CS-700": [
        ("DSA",3),
         ("Algo",2.5),
          ("AI",3)
          ], 
 "2016-CS-701":[
     ("DSA",4),
     ("LA",3),
      ("Algo",3),
       ("PF",2.8)
       ],
}

# With For loop

highest=[]
for o in D2.values():
    for i in o:
        if i[0]=="DSA":
            highest.append(i[1])

print(max(highest))

# Without For Loop

higest2=[]
roll=list(D2.keys())
o=0
i=0
while o<len(roll):
    i=0
    while i<len(D2[roll[o]]):
        if D2[roll[o]][i][0]=="DSA":
            higest2.append(D2[roll[o]][i][1])
        i+=1
    o+=1
print(max(higest2))      

# Q6 (c)

D3={
    "2016-CS-700": [
        ("DSA",3),
         ("Algo",2.5),
          ("AI",2.3)
          ], 
 "2016-CS-701":[
     ("DSA",4),
     ("LA",3),
     ("AI",2.2),
      ("Algo",3),
       ("PF",2.8)
       ],
}
les=0
for o in D3.values():
    for i in o:
        if i[0]=="AI":
            if i[1]<2.5:
                les+=1

print(f"Number of Students Having GPA less then 2.5 in AI = {les}")

rolls=list(D3.keys())
les2=0
o=0
i=0
while o<len(rolls):
    i=0
    while i<len(D3[rolls[o]]):
        if D3[rolls[o]][i][0]=="AI":
            les2+=1        
        i+=1
    o+=1 

print(f"Number of Students Having GPA less then 2.5 in AI = {les2}")



