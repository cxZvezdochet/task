
#Задача практика 5 со стеком, стек - пирамидка из детства пока не вытащишь верхний элемент не сможешь взять нижний.

from collections import deque #deque - стек

def bracket(s):
    stack = deque()
    d =  {'(':')','{':'}', '[':']'}

    for i in s:
        if i in d.keys():
            stack.append(i)
        else:
            a = stack.pop()
            if d[a] != i:
                return False
    return True