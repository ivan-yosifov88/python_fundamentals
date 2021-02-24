def string_multiplier(word_one, word_two, word, diff, iteration):
    result = 0
    for i in range(iteration):
        result += ord(word_one[i]) * ord(word_two[i])
    if not word == 0:
        for letter in word:
            result += ord(letter)
    return result


first_word, second_word = input().split()
difference = 0
number_of_iterations = 0
if len(first_word) > len(second_word):
    difference = len(first_word) - len(second_word)
    number_of_iterations = len(second_word)
    word_to_add = first_word[-difference:]
elif len(second_word) > len(first_word):
    difference = len(second_word) - len(first_word)
    number_of_iterations = len(first_word)
    word_to_add = second_word[-difference:]
else:
    number_of_iterations = len(first_word)
    word_to_add = 0

total_sum = string_multiplier(first_word, second_word, word_to_add, difference, number_of_iterations)
print(total_sum)



