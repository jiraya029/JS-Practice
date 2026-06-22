#print("Hello World")
#val=int(input("Enter the value"))
#print("The value is",val)
#a=int(input("Enter the value of a"))
#b=int(input("Enter the value of b"))
#print("Sum",a+b)
#print("Sub",a-b)
#print("Mul",a*b)
#print("Div",a/b)
#print("Mod",a%b)
#print("Expo",a**2)
#print("Floor div",a//b)
#print(a>b)
#print(a<b)
#print(a==b)
#print(a>=b)
#print(a<=b)
#print(a!=b)
#print(a>b or a<b)
#print(a>b or a>=b)
#print(not a>b)
#x=1
#x+=100
#print(x)
#x-=100
#print(x)
#x*=100
#print(x)
#x/=100
#print(x)
#x%=100
#print(x)
#x**=100
#print(x)
#x//=100
#print(x)
#a=0b1010;
#b=100;
#c=0o310;
#d=0x12c;
#print(a,b,c,d)
#float_1=1.5e2
#print(float_1)
#x=1.32+1;
#print(x)
#string="Hello World"
#char='C'
#mutiline_str='''Hi,This the first day of revising python'''
#print(string)
#print(char)
#print(mutiline_str)
#print("\\Hello")
#print("Hello\'w")
#print("Hello\"w")
#rint("Hello","\n","World")
#print("Hello","\t","World")
#age=int(input("Enter The Age"))
#if age>18:
#    {
#        print("You're Eligible")
#        
#    }
#else:
#    {
#        print("You're Not Eligible")
#    }
#i=1
#while (15>=i):
#    
#        print(i,"\t")
#        i=i+1
#for i in range(1,30,2):
#     print(i)
#for i in range(2,30,2):
#     print(i)
#for i in range(30,2,-3):
#     print(i)
#n=100
#sum=0
#for i in range(1,n+1):
#    sum=sum+i
#print("output %d:%d"%(n,sum))
#i=1
#while(i<=6):
#  for j in range(1,i):
#       print(j,end='\t')
#  print(end='\n')
#  i+=1
  
#i=1
#while(i<=6):
#  for j in range(1,i):
#       print('*',end='\t')
#  print(end='\n')
#  i+=1

#for i in range(5,0,-1):
#    for j in range(1,i+1):
#       print(j,end='\t')
#    print(end='\n')k=
#str1="Computer"
#inde=len(str1)
#for i in str1:
#   print(str1[0:inde],end="\t")
#    inde-=1
#print(end="\n")
#for i in range (1,inde+1):
#     print(str1[0:i],end="\t")
#     print(end="\n")
#for i in "ABCDEF":
#    if i=="E":
#        #break
#        continue
#    print(i,end=" ")
#for i in range(2,10,2):
#    print(i,end="\t")
#else:
#    print("\nEnd of the loop")
#i=0
#if(i==0):
#     pass
#else:
#     print("a")
#def hello():
#    print("Hello Python")
#    return
#hello()
#def area(w,h):
#    return w*h
#w=5
#h=6
#print(area(w,h))
#def printstring(str):
#   print("This is print function")
#    print(str)
#    return
#printstring("Hello Python")
#def sum(x,y,z):
#    print("Sum",x+y+z)
#    return
#sum(3,4,5,6,7)
#def printnos(*nos):
#    for n in nos:
#        print(n)
#   
#printnos(1,2,3)
#sum=lambda arg1,arg2:arg1+arg2
#print("The sum is",sum(30,40))
#print("The sum is",sum(-30,40))
#def numbfunc(n):
#    if 0<=n:
#        return n
#    else:
#        return -n
#num=int(input("Enter the number"))
#print(numbfunc(num))
#c=1
#def scope():
#    global c
#    c=c+2
#    print(c)
#scope()
#print(c)
#x=20
#y=-20.3
#print(abs(x))
#print(abs(y))
#c='a'
#d='D'
#print(ord(c))
#print(ord(d))
#e=65
#f=43
#print(chr(e))
#print(chr(f))
#x=15
#print(bin(x))
#k=15.2
#q='a'
#j=True
#print(type(k))
#print(type(q))
#print(type(j))
#x=15
#y="jng"
#print(id(x))
#print(id(y))
#MyList=[1,2,3,4]
#print(min(MyList))
#print(max(MyList))
#print(sum(MyList))
#x=14
#y=25
#print(format(x,'b'))
#print(format(y,'o'))
#print(format(y,'f'))
#x=25.2
#y=56.64
#print(round(x))
#print(round(y))
#print(round(y,1))
#a=5
#b=2
#print(pow(5,2))
#import math
#x=26.7
#y=26.7
#z=23.2
#print(math.floor(x))
#print(math.floor(y))
#print(math.floor(z))
#print(math.ceil(x))
#print(math.ceil(y))
#print(math.ceil(z))
#print(math.sqrt(x))
#print(math.sqrt(y))
#print(math.sqrt(z))
#def fact(n):
#    if n==0:
#      return 1
#    else:
#        return n*fact(n-1)
#print(fact(5))
#str1=input("Enter the String")
#index=0
#for i in str1:
#    print("subcript",index," ",i)
#    index+=1
#str1="Hello"
#print(str1[-1])
#print(str1.replace("o","O"))
#del str1
#print(str1)
#str1="Hello"+"World"
#print(str1)
#str1+="Python"
#print(str1)
#print(str1*5)
#str1="Python"
#print(str1[0])
#print(str1[0:3])
#print(str1[:3])
#print(str1[3:])
#str1="ASSAM!"
#index=0
#for i in str1:
#    print(str1[:index+1])
#    index+=1
#str1="Welcome to learn python"
#print(str1[::-2])
#name="Sivaji"
#marks=90
#print("Student Name %s and Mark %d"%(name,marks))
#num1=int(input("Enter the num 1"))
#num2=int(input("Enter the num 2"))
#print("The sum of {} and {} is {}".format(num1,num2,(num1+num2)))
#str1="welcome"
#print(len(str1))
#print(str1.capitalize())
#print(str1.center(15,'*'))
#print(str1.find('el',4))
#str1=input("ENter the string")
#str2="Welcome"
#if str2 in str1:
#    print("Found")
#else:
#    print("Not found")
#str1="RajaRajaChozhan"
#print(str1.count('Raja'))
#print(str1.count('R'))
#print(str1.count('r'))
#print(str1.count('a'))
#print(str1.count('a',0,5))
#print(str1.count('a',11))
#str1=input("Enter a String")
#str2=''
#index=-1
#for i in str1:
#    str2+=str1[index]
#    index-=1
#print("The give string {} The reversed String {}".format(str1,str2))
#if (str1==str2):
#    print("Its a palindrome")
#else:
#    print("Its not a palindrome")
#str1='*'
#i=1
#while i<=100:
#    print(str1*i)
#    i+=1
#str1=input("Enter the String")
#str2="aAeEiIoOuU"
#v,c=0,0
#for i in str1:
#    if i in str2:
#        v+=1
#    elif i.isalpha():
#        c+=1
#print("vowels: ",v,"\n","Consonants: ",c)
#MyList=[1,2,3,4,5,6]
#print(MyList[-4])
#MyList.append(90)
#i=0pytho
#while i<7:
#    print(MyList[i])
#    i+=1
div4=[]
x=21
for i in range(x):
    if (i%4==0):
        div4.append(i)
print(div4)
    
