def alphabetsCounting(file_path):
    # dict to count alphabets
    alphabet_dict = {}

    # read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        # read the file in each line
        for line in file:
            # observe evey character for each line
            for char in line:
                if char.isalpha():
                    # make capitals for every letter which is an alphabet
                    char_upper = char.upper()
                    alphabet_dict[char_upper] = alphabet_dict.get(
                        char_upper, 0) + 1

    alphabetList = list(alphabet_dict.items())

    # Sorting
    alphabetList.sort(key=lambda x: x[1], reverse=True)

    # alphabets from list
    sorted_list = [item[0] for item in alphabetList]
    return sorted_list


file_path = 'input_7_2.txt'

# print the result
result = alphabetsCounting(file_path)
print(result)
