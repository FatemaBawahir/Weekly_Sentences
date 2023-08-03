## Assumption for USR validity##
1. The number of concepts in the (concept row) USR are correct and thus our base of evaluation

## Features covered For USR validity ##
1. USR is not empty
2. It has 10 or more lines
3. It does not start or end with quotes
4. It does not have any empty lines in between
5. Elements in each row do not contain extra spaces around them - not done
6. length of index row to match no. of concepts
7. index row to have numbers from first onwards
8. All rows except for sentence_type and construction to have same commas 
9. no special characters other than the ones allowed - not done
10. USR source sentence begins with a hash with no space between them
11. Checks for dependency row - 
    - USR to have 0:main
    - dependency value of the format **alphanum:alphanum** i.e it allows exactly one colon and no other special characters, no empty values and no in between space. For eg.
    valid entries - 2:k1, 5:rblsk, 0:main
    invalid entries - :, 44:, :kj, 2 :kj, 3:: kj$%


##  Input ##
1. Copy the list of USRs in input_output/input.txt.

## Output ##
1. The generated USR folder appears within weekly_sentences folder
2. The USR_validity_report.csv appears within input_output folder.

## Steps of execution ##
1. Copy the input list of USRs in input_output/input.txt
2. Mention the name of the desired folder as argument and run the following script - 
   - **sh generate_sentences.sh <folder_name>**
   - for eg. **sh generate_sentences.sh week6**
3. Check the weekly_sentences folder, it has a folder with mentioned folder_name and all USRs as separate files within.
4. Also, check the input_output/USR_validity_report.csv for a comprehensive view of all USRs with errors if any.
5. If any USR has error, the csv file contains entry in this format -
   - "file_name" "ERROR" "comment"
    
    Where:
    
    file_name: Name of the file in the folder.

    ERROR: Tags the USR to be reviewed by Annotator.

    comment: The reason for ERROR.
6. Now the Annotator can edit the USRs as per the errors pointed out in the csv file.
7. To validate if all USRs have been corrected run the following command -
    - **python USR_validity.py ../weekly_sentences/<folder_name>**
    - for eg. - **python USR_validity.py ../weekly_sentences/week6**
8. Check the input_output/USR_validity_report.csv, if the file has more errors, correct the mentioned USRs and re-run the above command. When all the errors are resolved the csv file has "All USRs are valid	" message printed in it.


