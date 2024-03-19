class Queue:
    def __init__(self):
        self.s1 = []  
        self.s2 = []  

    def enqueue(self, item):
        self.s1.append(item)

    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2.pop()

    def is_empty(self):
        return not self.s1 and not self.s2