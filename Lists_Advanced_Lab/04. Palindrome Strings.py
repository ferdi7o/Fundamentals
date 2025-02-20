words = input().split()
palindrome_word = input()
counter = 0

def palindrome_founder(poli_list):
    polindrome_words_list = []
    for poli in poli_list:
        if poli == poli[::-1]:
            polindrome_words_list.append(poli)
    return polindrome_words_list


def palindrome_counter(po_word, list_):
    counter = len([word for word in list_ if po_word == word])
    return counter


def program_starter():
    polindroms = palindrome_founder(words)
    count = palindrome_counter(palindrome_word, words)
    return polindroms, count


palindroms, count = program_starter()
print(palindroms)
print(f"Found palindrome {count} times")