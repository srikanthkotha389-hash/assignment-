#!/usr/bin/env python
# coding: utf-8

# In[10]:


num=int(input('enter a number'))
if num%2==0:
 print('even number')
else:
        print('odd number')


# In[17]:


num=int(input('enter a number'))
if num==0:
    print('it is a 0')
elif num<0:
    print('it is a negative num')
else:
    print('it is a postive num')


# In[22]:


age=int(input('enter age'))
if age>=18:
    print('eligible for voting')
else:
    print('not eligible')


# In[26]:


num1=int(input('enter number'))
num2=int(input('enter number'))
if num1>num2:
     print('num1 is greater')
elif num1==num2:
    print('both r equal')
else:
    print('num2 is greater')


# In[30]:


marks=int(input('enter marks'))
if marks<40:
    print('fail')
elif 40 <= marks <= 59:
    print('pass')
elif 60 <= marks <= 79:
    print('good')
elif 80 <= marks <= 100:
    print('excellent')
else:
    print('invaild marks')
    
    


# In[3]:


year=int(input('enter year'))
if (year%4==0 and year%100!=0) or year%400==0:
    print('it is a leap year')
else:
    print('its not a leap year')
 


# In[4]:


password=str(input('enter password'))
if password=='OpenAI123':
    print('Access granted')
else:
    print('incorrect password')
    


# In[12]:


num=int(input('enter number'))
if num%3 and 5==0:
    print('fizz buzz')
elif num%3==0:
    print('buzz')
elif num%5==0:
    print('fuzz')
else:
    print(num)
    


# In[15]:


side1=int(input('enter side1'))
side2=int(input('enter side 2'))
side3=int(input('enter side 3'))
if side1==side2==side3:
    print('Equilateral')
elif side1==side2!=side3:
    print('Isosceles')
else:
    print('Scalene')


# In[28]:


hour=int(input('enter hour(0-23)'))
if 5<=hour<=1:
    print('good morning')
elif  12<=hour<=16:
    print('good afternoon')
elif 17<=hour<=20:
    print('good evening')
else:
    print('good night')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




