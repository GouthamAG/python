def count_substring(string, sub_string):
    count_of_substing = 0
    if string.find(sub_string) == 0:
        return 0
    else:
        for index in range(0, len(string) - len(sub_string) + 1):
            if string.find(sub_string, index , len(sub_string)+index) != -1 :
                count_of_substing += 1
    return count_of_substing

if __name__ == '__main__':
    string = "ABCDCDC"
    sub_string = "CDC"
    
    count = count_substring(string, sub_string)
    print(count)