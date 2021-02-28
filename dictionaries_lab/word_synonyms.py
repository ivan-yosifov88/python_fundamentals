number_of_words = int(input())

dictionary_with_synonyms = {}
for _ in range(number_of_words):
    word = input()
    synonym = input()
    if word not in dictionary_with_synonyms:
        dictionary_with_synonyms[word] = []
    dictionary_with_synonyms[word].append(synonym)

for key in dictionary_with_synonyms:
    print(f"{key} – {', '.join(dictionary_with_synonyms[key])}")
