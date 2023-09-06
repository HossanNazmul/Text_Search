import sys
import os
import json
import re
from collections import defaultdict

def count_occurrences_in_text(text_content, predefined_texts, verbose=False):
    occurrences = defaultdict(list)
    lines = text_content.splitlines()

    for line_num, line in enumerate(lines, start=1):
        for text_info in predefined_texts:
            text = text_info["text"]
            is_regex = text_info.get("is_regex", False)

            if is_regex:
                pattern = re.compile(text, re.IGNORECASE)
                match = pattern.search(line)
                if match:
                    occurrences[text].append(line_num)
                    if verbose:
                        print(f"Line {line_num}: {line}")
            else:
                if text.lower() in line.lower():
                    occurrences[text].append(line_num)
                    if verbose:
                        print(f"Line {line_num}: {line}")

    return occurrences

def process_text_file(log_file, keyword_file, verbose=False):
    try:
        with open(keyword_file, 'r', encoding='utf-8') as file: 
            predefined_texts = json.load(file)
    except Exception as e:
        print(f"Error reading the keyword file '{keyword_file}': {e}")
        return

    try:
        with open(log_file, 'r', encoding='utf-8', errors="ignore") as file:
            text_content = file.read()

        occurrences = count_occurrences_in_text(text_content, predefined_texts, verbose)

        found_texts = {text: line_numbers for text, line_numbers in occurrences.items() if line_numbers}
        if found_texts:
            print(f"Occurrences in log file: '{log_file}':")
            for text, line_numbers in found_texts.items():
                print(f" - '{text}': {len(line_numbers)} occurrences")
                # print line numbers if necessary
                #print(f" - '{text}': {len(line_numbers)} occurrences at line(s) {', '.join(map(str, line_numbers))}")
            print()
        else:
            print(f"No predefined texts were found in the log file '{log_file}'.")

    except Exception as e:
        print(f"Error processing the log file '{log_file}': {e}")

def process_folder(folder_path, keyword_file, verbose=False):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith((".txt", ".text", ".log")):
                log_file = os.path.join(root, file)
                process_text_file(log_file, keyword_file, verbose)

def main():
    log_file_or_folder = None
    keyword_file = "keywords.json"  # Updated default keyword file name
    verbose = False

    # Parse command-line arguments to get the log file/folder, keyword JSON file, and verbose mode
    args = sys.argv[1:]
    while args:
        arg = args.pop(0)
        if arg == '-l' and args:
            log_file_or_folder = args.pop(0)
        elif arg == '-k' and args:
            keyword_file = args.pop(0)
        elif arg == '-v':
            verbose = True

    if not log_file_or_folder:
        print("Usage: python text_search.py -l log_file_or_folder [-k keyword_file.json] [-v]")
        sys.exit(1)

    if os.path.isdir(log_file_or_folder):
        process_folder(log_file_or_folder, keyword_file, verbose)
    else:
        process_text_file(log_file_or_folder, keyword_file, verbose)

if __name__ == "__main__":
    main()
