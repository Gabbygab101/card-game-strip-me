nil = []
"""QUEUE"""
#creates a queue
def newQueue():
    return ("queue", [])
#test if an object is a queue. returns true/false
def isQueue(queue):
    return type(queue) is tuple and len(queue) == 2 and \
           queue[0] == "queue" and type(queue[1]) is list
#return the contents of the queue
def queueContents(queue):
    if isQueue(queue):
        return queue[1]
    raise TypeError("Must be type queue, not " + type(queue).__name__)
#tells if the queue is empty
def emptyQueue(queue):
    return queueContents(queue) == nil
#returns the first element in a queue
def queueFront(queue):
    if not emptyQueue(queue):
        return queueContents(queue)[0]
    raise IndexError("Empty Queue")
#adds element to the que
def enqueue(queue,el):
    if isQueue(queue):
        queueContents(queue).append(el)
        return queue
#removes the first element from the queue
def dequeue(queue):
    if not emptyQueue(queue):
        queueContents(queue).pop(0)
        return queue

"""STACK"""
#creates a representation of a stack
def newStack():
       return ("stack", [])
#tells if an object is a stack
def isStack(stack):
    return type(stack) is tuple and len(stack) == 2 and \
           stack[0] == "stack" and type(stack[1]) is list
#returns stack contents
def stackContents(stack):
    if isStack(stack):
        return stack[1]
    raise TypeError("Must be type stack, not " + type(stack).__name__)
#tells if the stack is empty
def emptyStack(stack):
    return stackContents(stack) == nil
#returns the first element in the stack
def stackTop(stack):
    if not emptyStack(stack):
        return stackContents(stack)[0]
    raise IndexError("Empty Stack")
#adds element to stack
def push(stack, el):
    if isStack(stack):
        stackContents(stack).insert(0,el)
    return stack
#removes element from stack
def pop(stack):
    if isStack(stack):
        stackContents(stack).pop(0)
    return stack
