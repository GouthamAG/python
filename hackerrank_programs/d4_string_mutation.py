def mutate_string(string, position, character):
    s = string
    list_of_char = list(string)
    list_of_char[position] = character
    result_str = "".join(list_of_char)
    return result_str

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)