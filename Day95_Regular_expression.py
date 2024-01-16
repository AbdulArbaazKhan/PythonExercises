# TODO: For Regular Expression import re
import re

# pattern = 'go'
#TODO: raw sting can not parse escape sequences r""
pattern = r'[A-Z]+yclone'
text = '''
I am stuck on the part of this CS data structures assignment where you implement an AVL tree class,
the AVL class Cyclone inherits the BST class, i have provided both as attachments. I am stuck on the two
methods within the AVL class, which are def add and def remove. Please keep in mind the special rules for
this assignment, which are that NO built in python data structures can be used, this means you cannot use
a python list, or even a tuple. You must use the structures provided in the classes. 
Dyclone
Cyclone
I will attach the full assignment details, but in summary I need the add and remove methods working with
some comments explaining your method/process in the avl.py file. bst.py and queue_and_stack.py are included 
as helpers, bst and queue_and_stack should not be edited at all. Only the add and remove methods in
avl.py. That being said, there are a handful of optional helper methods in avl.py that can be edited anyway
you see fit, and more than likley need to be edited in order to be used in add and remove. Do not mess with 
anything else, especially parts that say do not edit. 

There are printed test cases if you run avl.py, use them in accordance with the attached
assignment pdf to see if you correctly got add and remove working. queue_and_stack is included
as an optional helper as well, but you cannot edit anything within it, only use its prewritten
methods to aid in add and remove, or their helper methods. 

'''

# match = re.search(pattern, text) #stops at first match
matches = re.finditer(pattern, text) # for all occurrence
for match in matches:
    print(match)
    print(match.span())
    print(type(match.span()))
    print(text[match.span()[0]: match.span()[1]])

    # Website regexr