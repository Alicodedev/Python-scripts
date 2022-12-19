import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.Stack()
print(s.is_empty())

# Your solution here.

for char in string:
    s.push(char) # pushes characters from string list to stack list 

while not s.is_empty():
    reversed_string += s.pop() #! removes elements from topmost to first element in (LIFO ORDER) last element added is first one to output(taken out of the list)

print(reversed_string) # prints each element from the last one added to the first one which was adde in reverse 
