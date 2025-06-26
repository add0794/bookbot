# from collections import Counter
from pathlib import Path

class Book:
    def __init__(self, filepath):
        base_dir = Path(__file__).parent.absolute()
        self.full_path = base_dir / filepath
        self.text = ""  # Initialize text
    
    def get_book_text(self):
        with open(self.full_path) as f:
            self.text = f.read()
            return self.text

    def count_words(self):
        self.num_words = len(self.text.split())
        return f"{self.num_words} words found in the document"
    
    def count_characters(self):
        # characters = list(self.text)
        # counted_characters = Counter(characters)
        # return counted_characters
        self.char_counts = {}
        for char in self.text.lower():
            if char in self.char_counts:
                self.char_counts[char] += 1
            else:
                self.char_counts[char] = 1
        return self.char_counts

    def sort_characters(self):
        characters = [{"char": char, "num": num} for char, num in self.char_counts.items() if char.isalpha()]        
        characters.sort(reverse=True, key=lambda item: item["num"])
        self.rows = [f"{d['char']}: {d['num']}" for d in characters]
        return self.rows

    def report(self):
        # Join the rows with newlines for a clean output
        char_report = "\n".join(self.rows)
        return f"""
============ BOOKBOT ============
Analyzing book found at {self.full_path}...
----------- Word Count ----------
Found {self.num_words} total words
--------- Character Count -------
{char_report}
============= END ===============
"""