#!/usr/bin/python3

# A plagiarism detector that reads two essays and determines plagiarism percentage

import string

#1. Read Two Essays

def read_essay(filename):
    # Open the file and read its content
    with open(filename, "r") as f:
        content = f.read()
    return content

# Read both essays
essay1 = read_essay("essay1.txt")
essay2 = read_essay("essay2.txt")

print(essay1)
print(essay2)

# 2. Clean The Text

def clean_text(text):
    # Convert to lowercase
    text= text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Split into words
    text = text.split()
    # Return the list of words
    return text

# Clean both esssays
word1 = clean_text(essay1)
word2 = clean_text(essay2)

print(word1)
print(word2)

# 3. Count word frequencies

def count_words(words):
    # Create an empty directory
    word_counts = {}
    # Loop through each word
    for word in words:
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1 
        else:
            word_counts[word] = 1
    return word_counts

# Count word frequencies
counts1 = count_words(word1)
counts2 = count_words(word2)

print(counts1)
print(counts2)

# 4. Find Common Words
def find_common_words(counts1, counts2):
    # Convert dictionary keys to sets
    set1 = set(counts1.keys())
    set2 = set(counts2.keys())

    # Find words that appear in both essays (intersection)
    common_words = set1.intersection(set2)
    # Find all unique words from both essays (union)
    all_words = set1.union(set2)

    # Return both results
    return common_words, all_words

# Find common words and all unique words
common_words, all_words = find_common_words(counts1, counts2)
print("Common words:", common_words)
print("All words:", all_words)

# 5. Calculate Plagiarism Percentage
def calculate_plagiarism(common_words, all_words):
    # Number of common words
    num_common = len(common_words)
    print("Number of common words is:", num_common)

    # Number of unique words
    num_unique = len(all_words)
    print("Number of all unique words is:", num_unique)

    # Calculate percentage
    plagiarism_percentage = (num_common / num_unique) * 100

    return plagiarism_percentage

plagiarism_percentage = calculate_plagiarism(common_words, all_words)
print("Plagiarism percentage:", plagiarism_percentage)

# Determine result
if plagiarism_percentage >= 50:
    print("PLAGIARISM DETECTED!")
else:
    print("No plagiarism detected")

# 6. Search for a specific word
def search_word(word, counts1, counts2):
    # Convert word to lowercase
    word = word.lower()
    # Get counts
    count1 = counts1.get(word, 0)
    count2 = counts2.get(word, 0)

    # Print results
    print(f"'{word}' appears {count1} times in Essay 1")
    print(f"'{word}' appears {count2} times in Essay 2")

    # Return True if found, False if not
    found = count1 > 0 or count2 > 0
    return found

# Allow user to search for words
print("\n--- Word Search ---")
while True:
    user_word = input("Enter a word to search (or 'quit' to exit): ")

    if user_word.lower() == 'quit':
        print("Goodbye!")
        break

    result = search_word(user_word, counts1, counts2)
    print(f"Found: {result}\n")
