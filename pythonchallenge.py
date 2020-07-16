"""
Print out each element of the following array on a separate line:
```
["Joe", "2", "Ted", "4.98", "14", "Sam", "void *", "42", "float", "pointers", "5006"]
```
You may use whatever programming language you'd like. 
Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
"""
words = ["Joe", "2", "Ted", "4.98", "14", "Sam", "void *", "42", "float", "pointers", "5006"]
# list comprehension to print out each item's value
y = [print(i) for i in words]