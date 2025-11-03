#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sum(a,b):
    return a+b


# In[2]:


sum(3,4)


# In[15]:


def name(s):
    return s[::-1]


# In[16]:


name('srikanth')


# In[18]:


def even_odd(a):
    if a%2==0:
        print('it is a even number')
    else:
        print('it is a odd number')


# In[19]:


even_odd(3)


# In[27]:


def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
        return fact


# In[31]:


factorial(9)


# In[2]:


lst=[1,2,3,4,5]


# In[7]:


def large_ele(lst):
    max_ele=lst[0]
    for num in  lst:
        if num > max_ele:
            max_ele=num
    return max_ele


# In[8]:


large_ele(lst)


# In[11]:


for i in range(1,11):
    print(i)


# In[12]:


str1='srikanth'
for i in (str1):
    print(i)


# In[18]:


lst1=[1,2,3,4,5,6,7]
sum=0
for i in lst1:
    sum+=i
print(sum)
    
    


# In[25]:


def sum_num(*args):
    sum=0
    for i in args:
        sum+=i
    return sum


# In[26]:


sum_num(1,2,3,4,5,6)


# In[27]:


num=int(input('enter the number'))
print('mulplication table of number')
for i in range(1,11):
    print(num, 'x',i,'=',num*i)


# In[28]:


print('number from 1 to 50')

for num in range(1,51):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)


# In[30]:


i=1
while True:
    print(i)
    if i>9:
        break
    i+=1


# In[33]:


while True:
    enter_word=str(input('enter the word,type exit to stop'))
    if enter_word=='exit':
        print('program stopped')
        break
    else:
        print('enter the word')


# In[1]:


nums = [1, 2, 3, 4, 5]
a, *b = nums
print('a:',a)
print('b:',b)


# In[8]:


def multiply_num(num, n):
    result = 1
    for i in range(n):
        result *= num
    return result


# In[9]:


multiply_num(3,4)


# In[10]:



a = [1, 2]
b = [3, 4]

combined = [*a, *b]
print(combined)


# In[13]:


def pali(a):
    word=a
    if word==word[::-1]:
        print('it is a palindrome')
    else:
        print('it is not a palindrome')
        


# In[14]:


pali('srikanth')


# In[15]:


pali('racecar')


# In[21]:


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count


# In[22]:


count_vowels('srikanth')


# In[23]:


def even(l):
     for i in l:
        if i%2==0:
            print(i)


# In[24]:


even([1,2,3,4,6])


# In[ ]:




