# author: Chengkun Li
# date: May, 15, 2023
# file: A calculator to calculate an expression
# input: math expression
# output: result of expression or postfix

from stack import Stack
from tree import *


def infix_to_postfix(infix):
    current_number= ''
    s = Stack()
    operators = {'+':0,'-':0,'/':1,'*':1,'^':2,'(':3}
    symbols = ['+','-','*','/','^']
    infix = '('+infix.replace(' ','')+')'
    calculation_list= []

    # loop all the all characters in infix
    for i in infix:
        # if the character is a "("
        if i == "(":
            s.push(i)

        # if the character is a number
        elif i.isdigit():
            current_number += i

        # if the character is a "."
        elif i == '.':
            current_number += i
        
        # if te character is a symbols
        elif i in symbols:
            # if current_number is not empty, then add the character to the calculation_list
            if current_number != '':
                calculation_list.append(current_number)
            # reset the current_number
            current_number=''

            # while True, keeping popping from the stack
            while True:
                item = s.pop()
                # if the item is a '(', then push the variable bush and break
                if item =="(":
                    s.push(item)
                    break
                # if next item have a bigger or higher precedence(operator priority)
                elif operators[item] > operators[i]:
                    calculation_list.append(item)
                # else push the item back and break
                else:
                    s.push(item)
                    break
            # push the current operator in to the stack.
            s.push(i)
        
        # if the character is a ")"
        elif i == ")":
            # if current_number is not empty, then add the character to the calculation_list
            if current_number != '':
                calculation_list.append(current_number)
            # reset the current_number
            current_number=''

            # while True, keep popping from stack
            while True:
                item = s.pop()

                # if item is a "(", then break 
                if item =="(":
                    break
                else:# else append to postfix
                    calculation_list.append(item)
    
    # if current_number still have something, add it to calculation_list
    if current_number: 
        calculation_list.append(current_number)

    # while stack is not empty, add it all to calculation_list
    while not s.isEmpty():
        calculation_list.append(s.pop())
    # return a joined calculation_list string
    return ' '.join(calculation_list)


def calculate(infix):
    # get the input_list from infix_to_postfix() function
    input_list = infix_to_postfix(infix).split()
    # make a tree from make_tree() in ExpTree, and change all the '^' with '**' in the output string
    calculation_process = ExpTree.inorder(ExpTree.make_tree(input_list)).replace('^','**')
    # evaluate the expression using the original eval built-in function
    calculated_number = eval(calculation_process)
    # return the result value as a float 
    return float(calculated_number)

# a driver to test calculate module
if __name__ == '__main__':

    # test infix_to_postfix function
    assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    assert infix_to_postfix('5+2*3') == '5 2 3 * +'

    # test calculate function
    assert calculate('(5+2)*3') == 21.0
    assert calculate('5+2*3') == 11.0

    print("Welcome to Calculator Program!")
    while True:
        user_input = input("Please enter your expression here. To quit enter 'quit' or 'q':\n")
        if user_input.lower() == 'quit' or user_input.lower() == 'q':
            break
        print(calculate(user_input))
    print("Goodbye!")
    

    
    
