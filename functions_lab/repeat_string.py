def string_repeater(word, count):
    for iterations in range(count):
        print(word, end="")


word_to_repeat = input()
number_of_repeat = int(input())

string_repeater(word_to_repeat, number_of_repeat)