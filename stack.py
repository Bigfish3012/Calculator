# author: Chengkun Li
# date: May, 15, 2023
# file: A Stack class that can be used as Stack data structure
# input: Push in the nodes
# output: Pop out the nodes

class Stack:

    # make the stack as a list
    def __init__(self):
        self.items = [] 

    # if stack is empty, then return empty.
    def isEmpty(self):
        return self.items == []
    
    # add the item to the end of the list
    def push(self, item):
        self.items.append(item)

    # delete the item the item at the end of the list
    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()
    
    # return the value of the item at the end of the list
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.items[-1]

    # return the size of stack.
    def size(self):
        return len(self.items)

# a driver program for class Stack

if __name__ == '__main__':
    
    data_in = ['hello', 'how', 'are', 'you']
    s = Stack()
    for i in data_in:
        s.push(i)
           
    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]

    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())

    assert data_out == data_in[::-1]
    assert s.size() == 0
    assert s.peek() == None