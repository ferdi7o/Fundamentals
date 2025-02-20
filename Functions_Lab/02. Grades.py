# def grades(grade):
#     if 2.00 <= grade < 3.00:
#         print("Fail")
#     elif 3.00 <= grade < 3.50:
#         print("Poor")
#     elif 3.50 <= grade < 4.50:
#         print("Good")
#     elif 4.50 <= grade < 5.50:
#         print("Very Good")
#     elif 5.50 <= grade <= 6.00:
#         print("Excellent")
#
#
# grades(float(input()))

def grades_note(grade):
    if 2.00 <= grade < 3.00:
        return "Fail"
    elif 3.00 <= grade < 3.50:
        return "Poor"
    elif 3.50 <= grade < 4.50:
        return "Good"
    elif 4.50 <= grade < 5.50:
        return "Very Good"
    elif 5.50 <= grade <= 6.00:
        return "Excellent"


command = float(input())
print(grades_note(command))