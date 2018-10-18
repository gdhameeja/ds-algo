#!/usr/bin/env python3

class Queue(object):
    def __init__(self):
        self.data = []
        self.head = 0

    def enque(self, data):
        self.data.append(data)

    def deque(self):
        if not self.empty():
            self.head += 1

    def getData(self):
        if not self.empty():
            return self.data[self.head]

    def empty(self):
        return self.head >= len(self.data)

