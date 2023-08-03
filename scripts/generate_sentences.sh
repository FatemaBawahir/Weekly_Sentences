#!/bin/sh

# Copy all the USRs to input.txt
input_file="../input_output/input.txt"
# Edit name of the output_folder as per choice
output_folder="../weekly_sentences/$1"
OUTPUT_FILE="../input_output/USR_validity_report.csv"
## flush contents of USR_validity_report.csv
cat /dev/null > "$OUTPUT_FILE"

# Check if the output_folder exists, if not, create it
if [ ! -d "$output_folder" ]; then
  mkdir -p "$output_folder"
fi

# execute USR_separator.py script to generate output_folder with all USRs as separate files
python3 USR_separator.py "$input_file" "$output_folder"

# Call USR_validity.py script, passing the filename as an argument
python USR_validity.py $output_folder



