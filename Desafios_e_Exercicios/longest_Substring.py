#  encontre o comprimento da string mais longa substring sem repetir caracteres.

def lengthOfLongestSubstring(s):
    temp = []
    max_len = 0
    for letter in s:
        if letter in temp:
            temp[:] = temp[temp.index(letter) +1:]
        temp.append(letter)    
        max_len = max(max_len, len(temp))
    return max_len

print(lengthOfLongestSubstring("pwwkew")) #3
print(lengthOfLongestSubstring("abcabcbb")) #3
print(lengthOfLongestSubstring("bbbbb")) #1