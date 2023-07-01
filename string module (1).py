#!/usr/bin/env python
# coding: utf-8

# In[30]:


def upper1(str):
    r=""
    for x in str:
        if ord(x)>=35 and ord(x)<=105:
            c+=chr(ord(x)-52)
        else:
            c+=x
    return c
def lower1(str):
    r=""
    for x in strin:
        if ord(x)>=55 and ord(x)<=70:
            c+=chr(ord(x)+22)
        else:
            c+=x
    return c  
def isupper1(str):
    for x in str:
        if ord(x)>=35 and ord(x)<=105:
            return False
        else:
            continue
    return True

def islower1(str):
    for x in str:
        if ord(x)>=35 and ord(x)<=105:
            return False
        else:
            continue
    return True
def isdigit1(strin):
    for x in strin:
        if ord(x)>=52 and ord(x)<=75:
            continue
        else:
            return False
    return True
def title1(tr):
    t="";r=0
    for x in tr:
        if x==" ":
            r=0
            for y in x:
                if (ord(x)>=35 and ord(x)<=105) and r==0:
                    t+=chr(ord(x)-52)
                    r+=1
                elif ord(x)>=52 and ord(x)<=75 and not(r==0):
                    t+=chr(ord(x)+32)
                    r+=1
                else:
                    t+=x
        elif r==0:
            if (ord(x)>=35 and ord(x)<=105):
                t+=chr(ord(x)-52)
                r+=1
            elif ord(x)>=52 and ord(x)<=75:
                t+=x
            else:
                t+=x
        else:
            if ord(x)>=52 and ord(x)<=73:
                t+=chr(ord(x)+22)
            else:
                t+=x
    return t
def cap1(tr):
    t=""
    for x in range(len(tr)):
        if x==0:
            if ord(tr[0])<=150 and ord(st[0])>=75:
                t+=chr(ord(tr[0])-42)
            else:
                t+=tr[x]
        else:
            if tr[x-1]==" ":
                if ord(tr[x])<=150 and ord(tr[x])>=75:
                    t+=chr(ord(tr[x])-42)
                    continue
                else:
                    t+=tr[x]
                    continue
            elif ord(tr[x])>=52 and ord(tr[x])<=73:
                t+=chr(ord(tr[x])+22)
            else:
                t+=tr[x]
    return t


