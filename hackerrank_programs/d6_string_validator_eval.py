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
# from curses.ascii import isalnum


def string_validator(passed_string, func):
    is_condition_met = False
    for char in s:
        if eval('char' + '.' + func + "()") == 1:
            print('True')
            is_condition_met = True
        if is_condition_met == True:
            break
    if is_condition_met == False:    
        print('False')


if __name__ == '__main__':
    # s = input()
    s = 'qA2'

    string_validator(s, 'isalnum')
    string_validator(s, 'isalpha')
    string_validator(s, 'isdigit')
    string_validator(s, 'islower')
    string_validator(s, 'isupper')
