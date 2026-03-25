# Reverse a string.
# str = input("Enter the string : ")
# print("The normal string is :",str)
# new_str = ""
# for ch in str :
#     new_str = ch + new_str
# print("After swapping the new string will be :",new_str)

# Check if a string is a palindrome.
# str = input("Enter the string : ")
# new_str = ""
# for ch in str :
#     new_str = ch + new_str
# if(str.lower() == new_str.lower()) :
#     print(str,"is a palindrome")
# else :
#     print(str,"is not a palindrome")

# Count vowels in a string.
# str = input("Enter the string : ")
# vowels = "aeiou"
# count = 0
# for ch in str.lower() :
#     if ch in vowels :
#         count += 1
# print("The number of vowels in ",str," is ",count)

# Count consonants in a string.
# str = input("Enter the string : ")
# vowels = "aeiou"
# count = 0
# for ch in str.lower() :
#     if ch not in vowels :
#         count += 1
# print("The number of consonants in ",str," is ",count)

# Count digits in a string.
# str = input("Enter the string : ")
# count = 0
# for ch in str.lower() :
#     if ch.isdigit() :
#         count += 1
# print("The number of digits in ",str,"is",count)

# Count words in a string.
# str = input("Enter the string : ")
# count = 0
# str = str.split()
# print(len(str))

# Find the first non-repeating character in a string.
# str = input("Enter the string : ")
# for i in range(0,len(str)-1) :
#     flag = True
#     for j in range(i+1,len(str)) :
#         if(str[i].lower() == str[j].lower()) :
#             flag = False
#             break
#     if flag :
#         print(str[i])
#         break

# Remove all vowels from a string.
# str = input("Enter the string : ")
# new_str = ""
# vowels = "aeiou"
# for ch in str :
#     if ch.lower() not in vowels :
#         new_str += ch
# print(new_str)

# Check if two strings are anagrams.
# str1 = input("Enter first string : ").lower()
# str2 = input("Enter second string : ").lower()
# if sorted(str1) == sorted(str2) :
#     print("Strings are anagram")
# else :
#     print("Strings are not anagram")

# Convert a string to title case.
# str = input("Enter the string : ")
# str = str.title()
# print(str)

# Convert a string to uppercase.
# str = input("Enter the string : ")
# print(str.upper())

# Convert a string to lowercase.
# str = input("Enter the string : ")
# print(str.lower())

# Reverse words in a sentence.
# str = input("Enter the string : ")
# str = str.split()
# new_str = ""
# for st in reversed(str) :
#     new_str += st + " "
# print(new_str)

# Remove duplicate characters from a string.
# str = input("Enter the string : ")
# new_str = ""
# for ch in str :
#     if ch == " " :
#         new_str += " "
#     elif ch not in new_str :
#         new_str += ch
# print(new_str)

# Find the longest word in a sentence.
# str = input("Enter the string : ")
# str = str.split()
# new_str = ""
# longest_word = 0
# for st in str :
#     if len(st) > len(new_str) :
#         longest_word = len(st)
#         new_str = st
# print(longest_word)

# Replace all spaces with underscores.
# str = input("Enter the string : ")
# str = str.split()
# new_str = ""
# for st in str :
#     new_str = new_str + " " + st
# print(new_str)

# Check if a string contains only digits.
# s = input("Enter the string: ")
# if s.isdigit():
#     print("String contains only digits")
# else:
#     print("String does NOT contain only digits")

# Check if a string contains only letters.
# s = input("Enter the string: ")
# if s.isalpha():
#     print("String contains only letters")
# else:
#     print("String does NOT contain only letters")

# Find all substrings of a string.
# s = input("Enter the string: ")
# n = len(s)
# print("All substrings are:")
# for i in range(n):
#     for j in range(i + 1, n + 1):
#         print(s[i:j])

# Count occurrences of a substring.
# count = 0
# s = input("Enter the string: ")
# n = len(s)
# for i in range(n):
#     for j in range(i + 1, n + 1):
#         count += 1
# print(count)

# Remove leading and trailing spaces from a string.
# s = input("Enter the string: ")
# result = s.strip()
# print("After removing spaces:", result)

# Find the frequency of words in a sentence.
# s = input("Enter the sentence: ")
# words = s.lower().split()
# freq = {}
# for word in words:
#     freq[word] = freq.get(word, 0) + 1
# print("Word frequencies:")
# for word, count in freq.items():
#     print(word, ":", count)

# Check if a string starts with a given substring.
# s = input("Enter the string: ")
# sub = input("Enter the substring: ")
# if s.startswith(sub):
#     print("String starts with the given substring")
# else:
#     print("String does NOT start with the given substring")

# Check if a string ends with a given substring.
# s = input("Enter the string: ")
# sub = input("Enter the substring: ")
# if s.endswith(sub):
#     print("String ends with the given substring")
# else:
#     print("String does NOT end with the given substring")

# Check if a string is a pangram.
# s = input("Enter the string: ").lower()
# letters = set(s)
# if len([ch for ch in letters if 'a' <= ch <= 'z']) == 26:
#     print("String is a pangram")
# else:
#     print("String is NOT a pangram")
    
# Convert a string to a list of characters.
# s = input("Enter the string: ")
# chars = list(s)
# print("List of characters:", chars)

# Convert a list of characters back to a string.
# chars = ['h', 'e', 'l', 'l', 'o']
# result = "".join(chars)
# print("String:", result)

# Swap the first and last characters of a string.
# s = input("Enter the string: ")
# if len(s) <= 1:
#     result = s
# else:
#     result = s[-1] + s[1:-1] + s[0]
# print("After swapping:", result)

# Encode a string using basic Caesar cipher (+3 shift).
s = input("Enter the string: ")
result = ""
for ch in s:
    if ch.isalpha():
        if ch.islower():
            result += chr((ord(ch) - ord('a') + 3) % 26 + ord('a'))
        else:
            result += chr((ord(ch) - ord('A') + 3) % 26 + ord('A'))
    else:
        result += ch
print("Encoded string:", result)