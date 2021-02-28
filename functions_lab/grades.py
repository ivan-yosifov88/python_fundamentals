def grade_in_word(grade):
    word_grade = None
    if 2.00 <= grade <= 2.99:
        word_grade = "Fail"
    elif 3.00 <= grade <= 3.49:
        word_grade = "Poor"
    elif 3.50 <= grade <= 4.49:
        word_grade = "Good"
    elif 4.50 <= grade <= 5.49:
        word_grade = "Very Good"
    elif 5.50 <= grade <= 6.00:
        word_grade = "Excellent"
    return word_grade


grade_value = float(input())

print(grade_in_word(grade_value))