# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 22:13:44 2021

@author: ishus
"""

class Heaps:
    def __init__(self, l):
        self.l=l
    
    def childindex(self,i):
        return i*2+1, i*2+2
    
    def __minindexvalue(self,i,c1,c2):
        mi=i
        if (self.l[c1]<self.l[i]) and (self.l[c1]<self.l[c2]):
            mi=c1
        elif (self.l[c2]<self.l[i]) and (self.l[c2]<self.l[c1]):
            mi=c2
        return mi
        
    def heapify(self,i):
        c1 ,c2= self.childindex(i)
        minindex=i
        if c1>=len(self.l) and c2>=len(self.l):
            return
        elif c2>=len(self.l):
            if self.l[c1]<self.l[i]:
                minindex=c1
        else:
           minindex = self.__minindexvalue(i,c1,c2)
        if minindex!=i:
            self.l[i], self.l[minindex]=self.l[minindex], self.l[i]
            self.heapify(minindex)
        
    def buildminheap(self):
        for i in range(len(self.l)-1, -1, -1):
            self.heapify(i)
        
    def heapsort(self):
        self.buildminheap()
        l1=[]
        while self.l:
            self.l[0], self.l[-1]=self.l[-1], self.l[0]
            l1.append(self.l.pop())
            if self.l:
                self.heapify(0)
        return l1