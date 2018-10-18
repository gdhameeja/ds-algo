#!/usr/bin/env python3

class Queue(object):

    def __init__(self):
        self.data = []
        self.head = 0

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if not self.empty():
            self.head += 1

    def empty(self):
        return self.head >= len(self.data)

    def get_val(self):
        if not self.empty():
            return self.data[self.head]

