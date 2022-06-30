'''
Input Format

A single line containing a string .

Constraints


Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
'''

if __name__ == '__main__':
    s = input()
    is_condition_met = False
    for char in s:
        if char.isalnum():
            print('True')
            is_condition_met = True
        if is_condition_met == True:
            break
    if is_condition_met == False:    
        print('False')
        
        
        
    is_condition_met = False
    for char in s:
        if char.isalpha():
            print('True')
            is_condition_met = True
        if is_condition_met == True:
            break
    if is_condition_met == False:    
        print('False')
        

        
    is_condition_met = False
    for char in s:
        if char.isdigit():
            print('True')
            is_condition_met = True
        if is_condition_met == True:
            break
    if is_condition_met == False:    
        print('False')
        

        
    is_condition_met = False    
    for char in s:
        if char.islower():
            print('True')
            is_condition_met = True
        if is_condition_met == True:
            break
    if is_condition_met == False:    
        print('False')
        
        
        
    is_condition_met = False
    for char in s:
        if char.isupper():
            print('True')
            is_condition_met = True
        if is_condition_met == True:
            break
    if is_condition_met == False:    
        print('False')