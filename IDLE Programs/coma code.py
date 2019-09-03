def commas(list):
    seperator = ', '
    ender = 'and '
    i = 0
    sentence = []
    com_list = "Comma'd list: "
    print(len(list))
    while i < len(list):
        if i < len(list) - 1:
            word = list[i] + seperator
        if i == len(list) - 1:
            word = ender + list[i] 
        sentence.append(word)
        i += 1
    i = 0
    while i < len(list):
        com_list += sentence[i]
        i += 1
    print(com_list)



