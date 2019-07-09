class ArrayStack:
    def __init__(self,S):
        self.stack = S
    def length(self):
        return len(self.stack)
    def is_empty(self):
        return len(self.stack) == 0
    def top(self):
        if self.is_empty():
            print("stack is empty")
        else:
            return self.stack[-1]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if self.is_empty():
            print( "Stak is empty")
        else:
            return self.stack.pop()

print(ArrayStack([1,2]).length())

#reversing using stack
rev = ArrayStack([])
s = list("Divya")
for i in s: rev.push(i)
while rev.length()!=0:
    print(rev.pop(),end="")
print('\n')
#matching parenthesis
left = list('{([<')
right = list('})]>')
s = list("[{<<(>}]")
par = ArrayStack([])
#for i in s: par.push(i)
for ch in s:
    if ch in left:
        par.push(ch)
    elif ch in right:
        idx = right.index(ch)
        if par.top() == left[idx]:
            par.pop()
        else:
            print("incorrect parenthessis")
            break
    
if par.is_empty():
    print("perfect")
        
    
