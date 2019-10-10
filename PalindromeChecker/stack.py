# Stack Functions Program


def getStack():
    '''Creates and returns an empty stack'''
    return []

def isEmpty(s):
    '''Returns True if stack empty, otherwise returns False'''
    if s == []:
        return True
    else:
        return False

def top(s):
    '''Returns the top item of stack, item not removed'''
    if isEmpty(s):
        raise Exception
    else:
        return s[len(s) - 1]

def push(s,item):
    '''Pushes item on the top of stack'''
    
    s.append(item)


def pop(s):
    '''Removes and returns top item of stack.
       If stack empty, raises a ValueError.
    '''
    if isEmpty(s):
        raise Exception
    else:
        item = s[len(s) -1]
        del s[len(s) - 1]
        return item


