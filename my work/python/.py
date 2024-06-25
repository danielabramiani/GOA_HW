#pop
fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)

def pop_blocks(lst):
    stack = []
    i = 0
    while i < len(lst):
        if stack and stack[-1] == lst[i]:
            while i < len(lst) and stack[-1] == lst[i]:
                i += 1
            stack.pop()
        else:
            stack.append(lst[i])
            i += 1
    return stack

#remove

def remove_every_other(my_list):
    return my_list[::2]

#reverse

def solution(string):
    return string[::-1]

def solve(s):
    chars = [c for c in s if c != ' ']
    chars.reverse()
    
    result = []
    
    char_iter = iter(chars)
    
    for c in s:
        if c == ' ':
            result.append(' ')
        else:
            result.append(next(char_iter))
    
    return ''.join(result)