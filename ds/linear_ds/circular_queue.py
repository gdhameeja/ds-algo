#!/usr/bin/env python3

"""
Note:
we use (pointer + 1)%length of queue as the formula to move our pointers
this helps us as we dont have to reset pointers to 0
Example: if len = 5
head/tail = 0
(0 + 1)%5 = 1    and hence the pointer moves by one

head/tail = 4   # end of the queue to check if it is reset to 0
(4 + 1)%5 = 5%5 = 0   # hence the pointer is reset. This is awesome technique I learned.

"""

class Queue(object):

    def __init__(self, max_number=5):
        self.data = [None] * max_number
        self.head = -1
        self.tail = -1

    def isEmpty(self):
        """
        Beginning pos of head and tail is -1.
        Also if there is only one element left in the queue we reset head and tail to -1
        We use this property to check if head = -1 we say that queue is empty.
        """
        return self.head == -1   # beginning pos of head & tail is -1. 

    def isFull(self):
        """
        For the queue to be full the tail has to taverse to the point that
        it fills all the empty spaces in the queue and hence come till head
        so if the queue is full always tail + 1 will be equal to head
        """
        return ((self.tail + 1)%len(self.data)) == self.head

    def enqueue(self, value):
        """
        When queue is empty head will point to -1.
        We need to make it to point to 0. Because if queue is dequeued if head is -1 
        it will only move to pos 0 and hence actually no element will be dequeued
        """
        if not self.isFull():
            if self.isEmpty():
                self.head = 0
            self.tail = (self.tail + 1)%len(self.data)
            self.data[self.tail] = value
        else:
            return "Queue full"

    def dequeue(self):
        """
        In the case when only last element is left both pointers head and tail
        should be returned to -1.
        """
        if not self.isEmpty():
            if self.head == self.tail:
                self.head = -1
                self.tail = -1
            else:
                self.head = (self.head + 1)%len(self.data)


    def get_front(self):
        if not self.isEmpty():
            return self.data[self.head]

    def get_back(self):
        if not self.isEmpty():
            return self.data[self.tail]
