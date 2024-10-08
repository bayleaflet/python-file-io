import re
import argparse
import os

def find_words_in_file(input_file, output_file, word_pattern):
    """
    Reads an input file, searches for occurrences of words that match a given pattern,
    and writes the line number and word to an output file.

    Args:
        input_file (str): Path to the file to search.
        output_file (str): Path to the file to write results.
        word_pattern (str): Regular expression pattern to find the words.
    """
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Skip first 8 lines to ignore Project Gutenberg
        for line_num, line in enumerate(infile, start=8):
            # Find all words that match the given pattern in the line
            matches = re.findall(word_pattern, line, re.IGNORECASE)
            for match in matches:
                # Write the line number and the found word to the output file
                outfile.write(f"{line_num}\t{match}\n")

if __name__ == '__main__':
    # Adding argument pattern for pest practices, defaults to herit words.
    parser = argparse.ArgumentParser(
        prog="find_herit.py",
        description="Finds words based on the provided pattern"
    )
    parser.add_argument('-i', '--input', default='origin.txt', help='Provide input file (default: origin.txt)')
    parser.add_argument('-o', '--output', default='output.txt', help='Provide output filename (default: output.txt)')
    parser.add_argument('-p', '--pattern', default=r'\b(inherit(?:able|ance|ed|ing)?|heritable|heredity)\b',
                        help='Regex pattern to search for (default: heritability-related words)')

    args = parser.parse_args()

    # Call the function to process the file with user-provided arguments
    find_words_in_file(args.input, args.output, args.pattern)
    print(f"Searching {args.input}, outputting to {args.output}, and using this pattern: {args.pattern}")

