#!/usr/bin/python3

# Plagiarism Detector

## Project Description
A plagiarism detector that reads two essay files and looks for common and unique words. It compares the two essays and calculates a plagiarism percentage to determine if plagiarism has occurred.

## Features
1. **Read Two Essays** - Loads two text files (essay1.txt and essay2.txt)
2. **Clean Text** - Converts text to lowercase and removes punctuation
3. **Count Words** - Counts the frequency of each word in both essays
4. **Compare Essays** - Analyzes word frequencies across both documents
5. **Find Common and Unique Words** - Identifies words that appear in both essays (intersection) and all unique words (union)
6. **Calculate Plagiarism Percentage** - Uses set operations to determine plagiarism level
7. **Search for Specific Words** - Allows users to search for words and see their frequency in each essay

## How to Use

### Requirements
- Python 3.x
- Two text files: `essay1.txt` and `essay2.txt`

### Running the Program
```bash
python3 plagiarism_detector.py
```

### Example Workflow
1. The program reads and cleans both essays
2. It displays common words between the essays
3. It calculates the plagiarism percentage using the formula:
4. It determines the verdict:
   - **≥ 50%** = PLAGIARISM DETECTED
   - **< 50%** = NO PLAGIARISM DETECTED
5. Users can search for specific words to see how many times they appear in each essay
6. Type `quit` to exit

## Python Concepts Used
- **File Handling** - Reading and processing text files
- **Lists** - Storing words from essays
- **Dictionaries** - Counting word frequencies
- **Sets** - Finding intersection (common words) and union (all unique words)
- **Loops** - Iterating through words for counting and comparison
- **Functions** - Organizing code into reusable blocks
- **String Manipulation** - Converting to lowercase and removing punctuation
- **Conditional Logic** - Determining plagiarism verdict

## Example Output
Number of common words is: 22
Number of all unique words is: 115
Plagiarism percentage: 19.130434782608695
No plagiarism detected
--- Word Search ---
Enter a word to search (or 'quit' to exit): programming
'programming' appears 5 times in Essay 1
'programming' appears 4 times in Essay 2
Found: True

## Learning Outcomes
- Understanding file I/O operations in Python
- Working with data structures (lists, dictionaries, sets)
- String preprocessing and text manipulation
- Set operations for data comparison
- Writing functions and organizing code
- Implementing user input/output interactions
- Using conditional statements for decision-making
