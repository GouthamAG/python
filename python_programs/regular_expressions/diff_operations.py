import re



# ###---------------------------re.search------------------------------------
# if re.search("inform", "we neeed to inform him with latest imformation"):
#     print("There is word inform")
# '''
# OUTPUT
# -----
# There is word inform
# '''




# ###---------------------------re.findall------------------------------------
# all_inform = re.findall("inform", "we neeed to inform him with latest information")
# for i in  all_inform:
#     print(i)
# '''
# OUTPUT
# -----
# inform
# inform
# '''


# str_ = "Sat, hat, mat, cat"
# list_of_str = re.findall("[Shmc]at", str_)
# for i in list_of_str:
#     print(i)
# '''
# OUTPUT
# -----
# Sat
# hat
# mat
# cat
# '''


# str_ = "Sat, hat, mat, cat"
# list_of_str = re.findall("[a-z]at", str_)
# for i in list_of_str:
#     print(i)
# '''
# OUTPUT
# -----
# hat
# mat
# cat
# '''



# str_ = "Sat, hat, mat, cat"
# list_of_str = re.findall("[^h-m]at", str_)
# for i in list_of_str:
#     print(i)
# '''
# OUTPUT
# -----
# Sat
# cat
# '''



# ###---------------------------re.finditer------------------------------------
# temp_str = "we neeed to inform him with latest information"
# iterator = re.finditer("inform", temp_str)
# print(iterator)
# for i in iterator:
#     print(i.span())
# '''
# OUTPUT
# -----
# <callable_iterator object at 0x01E23190>
# (12, 18)
# (35, 41)
# '''





# # ###---------------------------re.compile------------------------------------
# str_ = "hat rat mat pat"
# pattern_object = re.compile("[r]at")
# print(pattern_object)
# food = pattern_object.sub("food", str_)
# print(food)
# '''
# # OUTPUT
# # -----
# re.compile('[r]at')
# hat food mat pat
# '''





random_str = '''
keep the blue glag
flying high
chelsa
'''
print(random_str)
'''
OUTPUT
------
keep the blue glag
flying high       
chelsa
'''
pattern_object = re.compile("\n")
result_str = pattern_object.sub(" ", random_str)
print(result_str)
'''
OUTPUT
------
 keep the blue glag flying high chelsa 
'''



