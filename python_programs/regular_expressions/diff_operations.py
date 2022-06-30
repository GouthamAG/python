import re



###---------------------------re.search------------------------------------
if re.search("inform", "we neeed to inform him with latest imformation"):
    print("There is word inform")
'''
OUTPUT
-----
There is word inform
'''




###---------------------------re.findall------------------------------------
all_inform = re.findall("inform", "we neeed to inform him with latest information")
for i in  all_inform:
    print(i)
'''
OUTPUT
-----
inform
inform
'''





###---------------------------re.finditer------------------------------------
temp_str = "we neeed to inform him with latest information"
iterator = re.finditer("inform", temp_str)
print(iterator)
for i in iterator:
    print(i.span())
'''
OUTPUT
-----
<callable_iterator object at 0x01E23190>
(12, 18)
(35, 41)
'''