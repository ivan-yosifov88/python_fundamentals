list_of_words = input().split()
word_to_check = input()
palindrome_list = [word for word in list_of_words if word == word[::-1]]
print(palindrome_list)
occurrence = palindrome_list.count(word_to_check)
print(f"Found palindrome {occurrence} times")