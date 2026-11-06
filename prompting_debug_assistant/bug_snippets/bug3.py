def is_palindrome(text):
    clean_text = text.lower()
    # Bug: Incorrect slicing step and logic
    reversed_text = clean_text[::-2]
    return clean_text == reversed_text

print(is_palindrome("racecar")) # Should return True
