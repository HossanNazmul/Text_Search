# Text Search and Count Application

The Text Search and Count application is a command-line Python program that allows users to search for predefined texts, including both plain texts and regular expressions, in one or multiple text files. The application provides users with the flexibility to specify the log file(s), keyword JSON file, and an optional verbose mode.

## Usage

To run the Text Search and Count application, use the following command-line syntax:

```
python texts_search.py -l log_file_or_folder [-k keyword_file.json] [-v]
```

- `-l log_file_or_folder`: Specifies the path to the log file or folder containing multiple log files. The application will search for predefined texts in the provided file or all log files in the specified folder.

- `-k keyword_file.json`: (Optional) Specifies the path to the JSON file containing predefined texts to search for. If not provided, the application will use the default `keywords.json` file located in the same directory as the program.

- `-v`: (Optional) Enables verbose mode, which prints the lines with line numbers where the predefined texts are found in the log files.

## Functionality

The Text Search and Count application performs the following functions:

1. **Search for Predefined Texts**: The application reads the specified log file(s) and searches for predefined texts, both plain texts and regular expressions, provided in the `keywords.json` file or a custom JSON file if specified.

2. **Count Text Occurrences**: The application counts the occurrences of each predefined text found in the log file(s) and displays the total count.

3. **Print Line Numbers (Optional)**: When verbose mode is enabled with the `-v` option, the application prints the lines with line numbers where each predefined text is found in the log file(s).

4. **Case-Insensitive Search**: The application performs case-insensitive searching for both plain texts and regular expressions. It matches the predefined texts regardless of the text's case.

## Using Regular Expressions

The Text Search and Count application supports the use of regular expressions for advanced text pattern matching. Regular expressions are powerful and versatile tools that allow users to define complex search patterns.

To use regular expressions in the `keywords.json` file, follow these guidelines:

1. Enclose the regular expression pattern within double quotes (`"`).
2. Prefix the regular expression with the letter 'r' (e.g., `r"\d+\.\d+\.\d+\.\d+"`).
3. Ensure that backslashes (`\`) within the regular expression are properly escaped by adding an additional backslash before each backslash (e.g., `"\\d+\\.\\d+\\.\\d+\\.\\d+"`).

Here's an example `keywords.json` file that includes regular expressions:

```json
[
    { "text": "ERROR", "is_regex": false },
    { "text": "WARNING", "is_regex": false },
    { "text": "\\d+\\.\\d+\\.\\d+\\.\\d+", "is_regex": true },
    { "text": "\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b", "is_regex": true }
]
```

In this example, the `keywords.json` file contains four entries:

- "ERROR" and "WARNING" are plain texts, which will be searched as they are (case-insensitive).
- `"\\d+\\.\\d+\\.\\d+\\.\\d+"` is a regular expression that matches IP addresses in the format `xxx.xxx.xxx.xxx`, where `xxx` represents one to three digits.
- `"\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b"` is a regular expression that matches email addresses.

Make sure to use the correct regular expression syntax in `keywords.json` to achieve the desired text matching behavior.

## Possible Use Cases

The Text Search and Count application can be useful in various scenarios, including but not limited to:

1. **Log Analysis**: Quickly search and count occurrences of specific error messages, warning messages, or patterns in log files to identify potential issues or anomalies.

2. **Text Mining**: Extract and analyze specific information or patterns from large text datasets, such as news articles, customer feedback, or social media posts.

3. **Data Validation**: Validate data files or configuration files by searching for specific patterns or keys to ensure the data conforms to the expected format.

4. **Debugging**: Identify occurrences of specific variables or patterns in source code files during debugging or code review processes.

5. **Security Analysis**: Search for potential security vulnerabilities or suspicious patterns in log files to enhance system security and monitor for unauthorized activities.

6. **Data Cleanup**: Use regular expressions to find and replace specific patterns in text files, aiding in data cleanup or formatting tasks.

## Conclusion

The Text Search and Count application provides a powerful and flexible tool for searching and counting predefined texts, both plain texts and regular expressions, in log files or any text-based data. Its capability to operate in verbose mode and perform case-insensitive matching makes it a valuable asset for various data analysis and text processing tasks.

For further details and examples, please refer to the code implementation and the provided `keywords.json` file.

---
