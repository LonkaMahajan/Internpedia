import os
import string

# Function to count words in a given text
def count_words(text):
    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = text.split()
    return len(words)

# Function to read text from a file
def read_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found!")
    
    with open(file_path, 'r') as file:
        return file.read()

# Function to handle multiple text inputs in a single run
def handle_multiple_inputs():
    texts = []
    while True:
        text_input = input("Enter text or type 'done' to finish: ")
        if text_input.lower() == 'done':
            break
        texts.append(text_input)
    return texts

# Main function to get input and display word count
def main():
    while True:
        try:
            # User choice for input method
            choice = input("Enter '1' for text input, '2' for file input, '3' for multiple texts, or 'q' to quit: ")

            if choice == '1':
                text = input("Enter your text: ")
                word_count = count_words(text)
                print(f"Word count: {word_count}")

            elif choice == '2':
                file_path = input("Enter the file path: ")
                text = read_file(file_path)
                word_count = count_words(text)
                print(f"Word count in file: {word_count}")

            elif choice == '3':
                texts = handle_multiple_inputs()
                for idx, text in enumerate(texts, 1):
                    word_count = count_words(text)
                    print(f"Text {idx} word count: {word_count}")

            elif choice.lower() == 'q':
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Please try again.")
        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(f"An error occurred: {e}")

# Start the program
if __name__ == "__main__":
    main()
