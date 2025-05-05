from stats import get_word_count
from stats import character_count
from stats import sort_characters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main(filepath):
    text = get_book_text(filepath)
    
    # Get word count
    word_count = get_word_count(text)
    
    # Get character counts and sort them
    char_counts = character_count(text)
    sorted_chars = sort_characters(char_counts)
    
    # Build the report string
    report = "============ BOOKBOT ============\n"
    report += f"Analyzing book found at {filepath}...\n"
    report += "----------- Word Count ----------\n"
    report += f"Found {word_count} total words\n"
    report += "--------- Character Count -------\n"
    
    # Add each character count to the report
    for char_data in sorted_chars:
        char = char_data["char"]
        # Only include alphabetical characters
        if char.isalpha():
            report += f"{char}: {char_data['num']}\n"
    
    report += "============= END ==============="
    
    print(report)

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])