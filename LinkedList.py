# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 07:36:27 2021

@author: ishus
"""

class Node:
    def __init__(self ,x=0, nxt = None, prev=None):
        self.val=x
        self.next=nxt
        self.prev=prev
    
class Linkedlist:
    def __init__(self, l):
        self.head, self.tail=self.__createlist(l)
       
    
    def __createlist(self,l):
        """
        Create LindekList
        Parameters : List  
        returns: Head of the LinkedList
        """
        if not l:
            return None, None
        i=1
        newNode=Node()
        head=newNode
        newNode.val=l[0]
        while i<len(l):
            newNode.next=Node()
            prevNode=newNode
            newNode=newNode.next
            newNode.val=l[i]
            newNode.prev=prevNode
            i+=1
        return head, newNode
    
    
    @property
    def length(self):
        """
        Length of LindekList
        Parameters :   
        returns: length of the LinkedList
        """
        count=0
        nodetraverse=self.head
        while nodetraverse!=None:
            count+=1
            nodetraverse=nodetraverse.next
        return count
    
    
    def reverse(self):
        """
        Reverse LindekList
        Parameters :   
        returns: head of the reversed LinkedList
        """
        revtraverse=self.head
        while True:
            revtraverse.next, revtraverse.prev=revtraverse.prev, revtraverse.next
            if revtraverse.prev is None:
                return revtraverse
            else:
                revtraverse=revtraverse.prev
   
    def deleteNth(self, n:int):
        """
        Delete Nth element LindekList
        Parameters :  n:int,  Nth element
        returns: head of the LinkedList with deleted element
        """ 
        root =self.head
        if n==1:
            self.head.next.prev= None
            self.head=self.head.next
        else :
            for _ in range(1,n):
                root=root.next
            root.prev.next=root.next
        
    def __add__(self, l2):
        """
        Add newList to original LindekList
        Parameters : l2:List, new List
        returns: head of the LinkedList with newly added list
        """ 
        self.headl1=self.head
        l1root=self.headl1
        while l1root.next!=None:
            l1root=l1root.next
        l1root.next=l2.head
        return self.headl1
    
    
