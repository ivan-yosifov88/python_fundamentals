sting_line = input()

for index in range(len(sting_line)):
    emoticon = ""
    if sting_line[index] == ":":
        emoticon += sting_line[index] + sting_line[index + 1]
        print(emoticon)
