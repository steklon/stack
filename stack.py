class Stack:

    def __init__(self):
        self.stack_list = list()

    def is_empty(self):
        if self.stack_list:
            return False
        else:
            return True

    def push_(self, item):
        self.stack_list.append(item)

    def pop_(self):
        if not self.is_empty():
            return self.stack_list.pop()
        else:
            return True

    def peek(self):
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)
