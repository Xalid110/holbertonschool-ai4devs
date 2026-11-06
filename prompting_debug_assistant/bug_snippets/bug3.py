# Function to check if a word or phrase is a palindrome
# Intended behavior: Compare cleaned string with its reverse version

def is_valid_palindrome(input_string):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = "".join(char.lower() for char in input_string if char.isalnum())
    
    # Bug: Incorrect slicing step [::-2] skips characters during reversal
    reversed_string = cleaned[::-2]
    
    print(f"Cleaned: {cleaned}")
    print(f"Reversed: {reversed_string}")
    
    return cleaned == reversed_string


# Test cases
word1 = "racecar"
word2 = "A man a plan a canal Panama"

print(f"Is '{word1}' palindrome?", is_valid_palindrome(word1))
print(f"Is '{word2}' palindrome?", is_valid_palindrome(word2))
