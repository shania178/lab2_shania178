#!/usr/bin/python3

# A plagiarism detector that reads two essays and determines plagiarism percentage

import string

#1. Read Two Essays

def read_essay(filename):
    try:    
        # Open the file and read its content
        with open(filename, "r") as f:
            content = f.read()
        # Check if file is empty
        if not content.strip():
            print(f"Error: {filename} is empty!")
            return None
        return content
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return None

# Read both essays
essay1 = read_essay("essay1.txt")
essay2 = read_essay("essay2.txt")

# Check if essays were successfully loaded
if essay1 is None or essay2 is None:
    print("Error: Cannot proceed without both essays!")
    exit()

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

def display_common_words_with_counts(common_words, counts1, counts2):
    """
    Display each common word with its frequency count in both essays.

    Parameters:
    - common_words: A set of words that appear in both essays
    - counts1: Dictionary with word frequencies from essay1
    - counts2: Dictionary with word frequencies from essay2
    
    Sort the common words alphabetically for better readability
    sorted() converts the set to a sorted list

    """
    sorted_words = sorted(common_words)

    # Print a header section to separate this from other output
    print("\n--- Common Words and Their Frequencies ---")

    """
    Print column headers for the table
    '<20' means left-align and use 20 characters width
    '<10' means left-align and use 10 characters width

    """
    print(f"{'Word':<20} {'Essay 1':<10} {'Essay 2':<10}")

    # Print a separator line for visual clarity
    print("-" * 40)

    # Loop through each common word one by one
    for word in sorted_words:
        # Get the count of this word from essay1 dictionary
        # Use .get(word, 0) to return 0 if word not found
        count1 = counts1.get(word, 0)

        # Get the count of this word from essay2 dictionary
        count2 = counts2.get(word, 0)

        # Print the word and its counts in a formatted table row
        print(f"{word:<20} {count1:<10} {count2:<10}")

    # Print the total number of common words found
    print(f"\nTotal common words: {len(common_words)}")

display_common_words_with_counts(common_words, counts1, counts2)

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
    # Check if input is empty
    if not word.strip():
        print("Error: Please enter a word!")
        return False

    # Convert word to lowercase
    word = word.lower()

    # Remove punctuation
    word = word.translate(str.maketrans("", "", string.punctuation))

    # Check if word is empty after removing punctuation
    if not word:
        print("Error: Word contains only punctuation!")
        return False

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

    # Check for empty input
    if not user_word.strip():
        print("Warning: Please enter a word!\n")
        continue

    result = search_word(user_word, counts1, counts2)
    print(f"Found: {result}\n")
