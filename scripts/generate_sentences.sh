#!/bin/sh

# Copy all the USRs to input.txt
input_file="../input.txt"
# Edit name of the output_folder as per choice
output_folder="../weekly_sentences/week3"

# Check if the output_folder exists, if not, create it
if [ ! -d "$output_folder" ]; then
  mkdir -p "$output_folder"
fi

# execute USR_separator.py script to generate output_folder with all USRs as separate files
python3 USR_separator.py "$input_file" "$output_folder"

filenames=$(ls "$output_folder")

# Iterate over the list of filenames and call another script for each one
for filename in $filenames; do
  # Call USR_validity.py script, passing the filename as an argument
  python USR_validity.py $output_folder/$filename

done