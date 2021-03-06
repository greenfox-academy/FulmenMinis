# Find the substring in the list
#    Create a function that takes a string and a list of string as a parameter
#    Returns the index of the string in the list where the first string is part of
#    Returns -1 if the string is not part any of the strings in the list
# Example
# input: "ching", ["this", "is", "what", "I'm", "searching", "in"]
# output: 4

def find_words(text, word):
    for i in range(len(text)):
        if word in text[i]:
            return i
    return -1

print(find_words(["this", "is", "what", "I'm", "searching", "in"], "ching"))
