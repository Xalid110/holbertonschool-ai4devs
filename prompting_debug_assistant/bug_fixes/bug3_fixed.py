def is_valid_palindrome(input_string):
    cleaned = "".join(char.lower() for char in input_string if char.isalnum())
    reversed_string = cleaned[::-1]
    return cleaned == reversed_string

word1 = "racecar"
word2 = "A man a plan a canal Panama"

print(f"Is '{word1}' palindrome?", is_valid_palindrome(word1))
print(f"Is '{word2}' palindrome?", is_valid_palindrome(word2))
assert is_valid_palindrome(word1) == True
