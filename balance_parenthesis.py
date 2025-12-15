
"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #3 (25 points)
Filename: balance_parenthesis.py

Complete the bracket balancing function below. It checks if (  and  ) brackets are balanced, using a stack.

Function returns 0 if brackets are balanced,
-1 if there are more closing brackets than needed,
and x otherwise, where x is the index of the most recent
unbalanced left bracket.

Examples:
"--(---(------)--"  returns  2 
"()----)" returns -1
"-----() -- ( () )" returns 0

"""
# from node_stack import node
from node_stack import node

def balance_parenthesis(a_string):
    th_stack = node()
    for i in range(len(a_string)):
        if a_string(i) == '(':
            th_stack.push(a_string(i))
        elif a_string(i) ==  ")":
         try:    
            th_stack.pop()
         except IndexError:
            return -1
            

    if th_stack.is_empty():
        return 0 
    else: 
        return th_stack
    

def main():     
    a_string = input("enter parenthesis: ")
    print(balance_parenthesis(a_string))

if __name__ == "__main__":    main()