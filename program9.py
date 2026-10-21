
# Program 9: Text Anagram and Pattern Matcher Tool

from collections import Counter

def clean_text(text):
    # Remove spaces and special characters, and convert to lowercase
    return ''.join(ch.lower() for ch in text if ch.isalnum())


def are_anagrams(word1, word2):
    # Sort characters and compare
    return sorted(clean_text(word1)) == sorted(clean_text(word2))


def count_characters(text):
    # Count frequency of each character
    return dict(Counter(clean_text(text)))


def create_pattern_key(text):
    # Create an immutable tuple key
    return tuple(sorted(clean_text(text)))


# Input words and phrases
word1 = input("Enter first word or phrase: ")
word2 = input("Enter second word or phrase: ")

# Check anagram
if are_anagrams(word1, word2):
    print("The given texts are anagrams.")
else:
    print("The given texts are not anagrams.")

# Display character frequencies
print("Character frequency of first text:", count_characters(word1))
print("Character frequency of second text:", count_characters(word2))

# Create tuple keys
key1 = create_pattern_key(word1)
key2 = create_pattern_key(word2)

print("Pattern key 1:", key1)
print("Pattern key 2:", key2)

# Compare tuple keys
print("Pattern match:", key1 == key2)
