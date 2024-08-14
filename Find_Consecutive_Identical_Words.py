import re, os
#Use Python 3

# Loops over all latex files
def main(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith('.tex'):
                file_path = os.path.join(root, file)
                print(f"Processing file: {file}")
                find_consecutive_identical_words(file_path)

# Looks for two consecutive identical words
def find_consecutive_identical_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = re.findall(r'\b(\w+)\b', content)  # Extract all words using regular expression

            for i in range(1, len(words)):
                if words[i] == words[i - 1]:
                    repeated_word = words[i]
                    previous_word = words[i - 1]
                    posterior_word = words[i + 1] if i + 1 < len(words) else None

                    message = "Consecutive words: "#'{repeated_wor}"
                    if previous_word:
                        message += f" '{previous_word}'"
                    message += f" '{repeated_word}'"
                    message += f" '{repeated_word}'"
                    if posterior_word:
                        message += f" '{posterior_word}'"
                    print(message)
                    return True
        return False
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False
    except Exception as e:
        print(f"Error while processing {file_path}: {e}")
        return False

if __name__ == "__main__":
    directory_path = "/Users/pablo/Desktop/tHq_Analysis/8-Thesis/Thesis/"
    main(directory_path)
