"""
Program: Word Analyzer
Author: Mervyn S. Philip
Purpose: This program analyze a text file and count the frequency of each word,
         excluding common stop words.
Date: 2026-07-03
"""

from pathlib import Path
import string

#To analyze a text file and count the frequency of each word 
class WordAnalyzer:

    #to store the file path and initialize the word frequency dictionary
    def __init__(self, filepath, stop_words = None):
        self.filepath = Path(filepath)
        self.frequencies = {}
        self.stop_words = set(stop_words) if stop_words is not None else set()

    #to read the selected file and count each word
    def process_file(self):
        try:
            if not self.filepath.exists():
                raise FileNotFoundError
            
            punctuation_table = str.maketrans('', '', string.punctuation)

            with self.filepath.open('r', encoding='utf-8') as file:
                for line in file:
                    cleaned_line = line.translate(punctuation_table).lower()
                    words = cleaned_line.split()
                    
                    for word in words:
                        if word not in self.stop_words:
                            self.frequencies[word] = (self.frequencies.get(word, 0) + 1)
            
            return True
        except FileNotFoundError:
            print(f"Error: The file '{self.filepath}' could not be found.")
            return False
        
    #To print the word count report in alphabetical order
    def print_report(self):
        sorted_words = sorted(self.frequencies.keys())
        
        for word in sorted_words:
            print(f"{word:<12}:: {self.frequencies[word]}")


#To display the main menu of files and the exit option.
def display_menu(file_options):
    print("\nWord Analyzer Menu:")
    print("Please select a file to analyze:")
    
    for choice, file_info in file_options.items():
        print(f"{choice}. {file_info['title']}")
    
    print(f"5. Exit")

#To run the menu-driven word analyzer program
def main():
    base_path = Path(__file__).parent

    file_options = {
        "1": {"title": "Princess Mars",
            "path": base_path / "princess_mars.txt"},

        "2": {"title": "Tarzan",
            "path": base_path / "Tarzan.txt"},

        "3": {"title": "Treasure Island",
            "path": base_path / "treasure_island.txt"},

        "4": {"title": "Monte Christo",
            "path": base_path / "monte_cristo.txt"}}
    
    choice = ""

    while choice != "5":
        display_menu(file_options)
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "5":
            print("\nGoodbye!")
        elif choice in file_options:
            selected_file = file_options[choice]["path"]
            print(f"\nProcessing '{selected_file.name}'...\n")

            analyzer = WordAnalyzer(selected_file)

            if analyzer.process_file():
                analyzer.print_report()

            input("\nPress Enter to return to the menu...")
        else:
            print("\nInvalid choice. Please select from 1-5.")
            input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()