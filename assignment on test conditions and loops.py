#!/usr/bin/env python
# coding: utf-8

# In[1]:


num=int(input('enter a number'))
if num%2==0:
 print('even number')
else:
        print('odd number')


# In[1]:


num=int(input('enter a number'))
if num==0:
    print('it is a 0')
elif num<0:
    print('it is a negative num')
else:
    print('it is a postive num')


# In[2]:


num1=int(input('enter a number1'))
num2=int(input('enter a number2'))
num3=int(input('enter a number3'))
if num1>=num2 and num1>=num3:
    print('number1 is greater')
elif num2>=num1 and num2>=num3:
    print('number2 is greater')
else:
    print('number3 is greater')

    


# In[4]:


year = int(input('enter a year'))
if year%4==0 and year%100!=0 or year%400==0:
    print('it is a leap year')
else:
    print('it is not a leap year')


# In[7]:


character=str(input('enter the character'))
if character=='a' and 'e' and 'i' and 'o' and 'u':
    print('character is a vowle')
else:
    print('constant')


# In[2]:


num=int(input('enter a number'))
if num%3==0 and num%5==0:
    print('it is divisible by 3 and 5')
else:
    print('it is not divisible by 3 and 5' )


# In[3]:


for i in range(1,21):
    print(i)


# In[7]:


print('number from 1 to 50')

for num in range(1,51):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)


# In[22]:


total = 0
for i in range(1,101):
    total += i
print('sum of num',total)


# In[26]:


num=int(input('enter the number'))
print('mulplication table of number')
for i in range(1,11):
    print(num, 'x',i,'=',num*i)
    


# In[3]:


num=int(input('enter the number'))
fact=1
if num<0:
    print('it does not have a factorial')
elif num==0:
    print('factorial is 1')
else:
    for i in range(1,num+1):
        fact*=i
    print('factorial of num',num,'=',fact)
        


# In[7]:


l=[1,2,3,4,50,66,77,80,5]
for i in l:
    if i>10:
        print(i)
        


# In[16]:


i=1
while True:
    print(i)
    if i>10:
        break
    i+=1


# In[2]:


for i in range(1,16):
    if i%3!=0 and i%5!=0:
        print(i)
        


# In[18]:


for i in range(1,6):
    for j in range(i):
          print('*',end='')
    print()


# In[19]:


name=str(input('enter the name'))
for i in name:
    if name=='':
        print('enter the name again')
else:
    if name=="exit


# In[1]:


while True:
    enter_word=str(input('enter the word,type exit to stop'))
    if enter_word=='exit':
        print('program stopped')
        break
    else:
        print('enter the word')
    

    


# In[15]:


num=int(input('enter the num'))
if num>1:
        for i in range(2,num):
            if num%i==0:
                print('it is not prime number')
                break
        else:
            print('it is  a prime number')
else:
    print('not prime')
                
            


# In[2]:


marks=int(input('enter marks'))
if marks<60:
    print('fail')
elif 90 <= marks <= 80:
    print('grade a')
elif 80 <= marks <= 89:
    print('grade b')
elif 70 <= marks <= 79:
    print('grade c')
elif 60 <= marks <= 69:
    print('grade c')
else:
    print('invaild marks')


# In[10]:


num1=int(input('enter the number1'))
num2=int(input('enter the number2'))
num3=int(input('enter the number3'))
num4=int(input('enter the number4'))
num5=int(input('enter the number5'))
smallest=num1
if num2 < smallest:
    smallest = num2
if num3 < smallest:
    smallest = num3
if num4 < smallest:
    smallest = num4
if num5 < smallest:
    smallest = num5
print('smallest:',smallest)


# In[17]:


char=str(input('enter the character:'))
if (char >= 'a' and char<='z') or (char>='A' and char<='Z'):
    print('it is a alpha character')
else:
    print('it is not a alpha character')


# In[2]:



N = int(input("Enter number of terms: "))

a = 0
b = 1
if N <= 0:
    print("Enter a positive number")
elif N == 1:
    print(a)
else:
    print(a, b, end=" ")

    for i in range(2, N):
        c = a + b
        print(c, end=" ")
        a = b
        b = c


# In[3]:


num = int(input("Enter a number: "))

reverse_num = 0

while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num //= 10

print("Reversed number:", reverse_num)


# In[ ]:




