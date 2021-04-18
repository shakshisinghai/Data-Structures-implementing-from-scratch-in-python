# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:01:14 2021

@author: ishus
"""

from LinkedList import Linkedlist, Node


class Stack(Linkedlist):
    
    def __init__(self,l):
        stack= Linkedlist(l)
        self.l=l
        self.head=stack.head
        self.tail=stack.tail
    
    def push(self,element):
        """
        Push element in stack
        Parameters : element:int, new element to add
        returns: 
        """ 
        if not self.head:
            self.head=Node()
            self.head.val=element
            self.tail=self.head
        else :
            self.tail.next=Node()
            prevtail=self.tail
            self.tail= self.tail.next
            self.tail.prev=prevtail
            self.tail.val=element
        
    def pop(self):
        """
        Pop element in queue
        Parameters : 
        returns: 
        """ 
        if not self.head:
            return None
        self.tail.prev.next=None
        self.tail=self.tail.prev
    
class Queue(Linkedlist):
    
    def __init__(self,l):
        queue= Linkedlist(l)
        self.head=queue.head
        self.tail=queue.tail
        
    def push(self, element):
        """
        Push element in queue
        Parameters : element:int, new element to add
        returns: 
        """ 
        if not self.head:
            self.head=Node()
            self.head.val=element
            self.tail=self.head
        else:
            self.tail.next=Node()
            prevtail=self.tail
            self.tail= self.tail.next
            self.tail.prev=prevtail
            self.tail.val=element
        
    def pop(self):
        """
        Pop element in queue
        Parameters : 
        returns: 
        """ 
        if not self.head:
            return None
        self.head.next.prev=None
        self.head=self.head.next