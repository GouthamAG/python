import re


temp_str = "we neeed to inform him with latest information"
# iterator = re.finditer("q", temp_str)
# print(iterator)
# for i in iterator:
#     print(i.span())


result = re.findall("inform", temp_str)
print(result)
