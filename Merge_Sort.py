# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 08:32:45 2021

@author: ishus
"""
import time
import random

class Mergesort:
    def __init__(self):
        pass
    
    def mergesortedlist(self, list1,list2):
        i,j, l3=0,0,[]
        len1, len2=len(list1), len(list2)
        while i<len1 and j<len2:
            if list1[i]<=list2[j]:
                l3.append(list1[i])
                i+=1
            else:
                l3.append(list2[j])
                j+=1
        if j<len2:
            l3.extend(list2[j:])
        elif i<len1:
            l3.extend(list1[i:])
        return l3
    
    def mergesort(self, l):
        lenl=len(l)
        if not l:
            return []
        elif lenl==1:
            return l
        else :
            mid=(lenl//2)
            l1= self.mergesort(l[:mid]) 
            l2= self.mergesort(l[mid:])
            
            return self.mergesortedlist(l1,l2)
    
    def mergesortloop(self, l):
        n=len(l)
        mid=(n//2)
        for j in range(mid+1):
            k=2**j
            i=0
            while i<n:
                if i+k<n:
                    l1=l[i:i+k]
                    if (i+k+k)<=n:
                        l2=l[i+k:i+k+k]
                        l3=self.mergesortedlist(l1,l2)
                        l[i:i+k+k]=l3
                    else :
                        l2=l[i+k:]
                        l3=self.mergesortedlist(l1,l2)
                        l[i:]=l3
                i+=i+k+k
        return l
        
   
obj=Mergesort()
l=[random.randint(1,100) for i in range(1000000)]
start=time.time()     
obj.mergesort(l)
end=time.time()-start
print('recusrsion end time', end)

start=time.time()     
obj.mergesortloop(l)
end=time.time()-start
print('loop end time', end)