def load_file():
    """Loads .txt file as per the user given path"""
    filename = input("Ente file name:")

    try: 
        with open(filename,"r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print("File no found. Please check the name and try again.")

    return text

def count_character(text):
    """Counts the character in the text file and returns """
    characters_count = len(text)
    words_count = len(text.split())
    return characters_count, words_count

def main():
    words = load_file()
    characters_count, words_count = count_character(words)
    print(f"The number of character in the file is {characters_count}")
    print(f"The number of words in the files is {words_count} ")

if __name__ == "__main__":
    main()
    
        