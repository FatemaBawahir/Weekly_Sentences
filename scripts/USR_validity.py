import sys
import re
import os
USR_row_info = ['root_words', 'index_data', 'seman_data', 'gnp_data', 'depend_data', 'discourse_data', 'spkview_data',
                'scope_data']
OUTPUT_FILE = '../input_output/USR_validity_report.csv'  # temporary for presenting
file_name_lst = []
logtype_lst = []
msg_lst = []
def log(msg, file_name, logtype='OK'):
    '''Generates log message in predefined format.'''

    # Format for log message
    if logtype in ('ERROR'):
        file_name_lst.append(file_name)
        logtype_lst.append(logtype)
        msg_lst.append(msg)

def read_file(file_path, file_name):
    '''Returns array of lines for data given in file'''

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            file_rows = []
            for i in range(len(lines)):
                lineContent = lines[i].strip()
                if lineContent != '':
                    file_rows.append(lineContent)
                elif lineContent == '' and i < 10:
                    log('Invalid USR : has empty lines in between', file_name, 'ERROR')
                elif lineContent == '' and i == 10:
                    break

    except FileNotFoundError:
        log('No such File found', file_name, 'ERROR')

    return lines

def generate_rulesinfo(file_data, file_name):
    '''Return list all 10 rules of USR as list of lists'''

    if len(file_data) < 10:
        log('Invalid USR : does not contain 10 lines.', file_name, 'ERROR')

    src_sentence = file_data[0].strip().strip('"')
    if not src_sentence.startswith('#'):
        log('Invalid USR : source sentence does not begin with # ', file_name, 'ERROR')
    root_words = file_data[1].strip().split(',')
    index_data = file_data[2].strip().split(',')
    seman_data = file_data[3].strip().split(',')
    gnp_data = file_data[4].strip().split(',')
    depend_data = file_data[5].strip().split(',')
    discourse_data = file_data[6].strip().split(',')
    spkview_data = file_data[7].strip().split(',')
    scope_data = file_data[8].strip().split(',')
    sentence_type = file_data[9].strip().strip('"')
    construction_data = ''
    if len(file_data) > 10:
        construction_data = file_data[10].strip().strip('"')

    return [src_sentence, root_words, index_data, seman_data, gnp_data, depend_data, discourse_data, spkview_data,
            scope_data, sentence_type, construction_data]

def write_output(file_name_lst, logtype_lst, msg_lst):
    with open(OUTPUT_FILE, 'w') as file:
        if len(file_name_lst) == 0:
            file.write("All USRs are valid" + '\t')
        else:
            for i in range(len(file_name_lst)):
                file.write(file_name_lst[i] + '\t')
                file.write(logtype_lst[i] + '\t')
                file.write(msg_lst[i] + '\t')
                file.write('\n')

def is_USR_valid(rules_info, file_name):
    # taking length of root_words as our base of evaluation
    root_words = rules_info[1]
    index_data = [int(x) for x in rules_info[2]]
    dependency_data = rules_info[5]
    len_root = len(root_words)
    len_index = len(index_data)
    is_valid = True
    if len_root > len_index:
        log(f'{USR_row_info[1]} has lesser enteries as compared to {USR_row_info[0]}', file_name, 'ERROR')
        is_valid = False
        #sys.exit()
    elif len_root < len_index:
        log(f'{USR_row_info[1]} has more enteries as compared to {USR_row_info[0]}', file_name, 'ERROR')
        is_valid = False
        #sys.exit()

    # once the lengths of root_words and index_data are equal check value of each index
    if len_root == len_index:
        for i in range(1, len_root + 1):
            if index_data[i - 1] == i:
                continue
            else:
                index_data[i - 1] = i
                log(f'{USR_row_info[1]} has wrong entry at position {i}', file_name, 'ERROR')
                is_valid = False
                #sys.exit()

    # Checking all tuples have same number of enteries except for first, 10th and 11th
    for i in range(len(rules_info)):
        if i == 0 or i >= 9:
            continue
        row = rules_info[i]
        len_row = len(row)
        if len_row < len_root:
            log(f'Invalid USR : number of entries less in {USR_row_info[i-1]} as compared to {USR_row_info[0]}', file_name, 'ERROR')
            is_valid = False

        elif len_row > len_root:
            log(f'Invalid USR : number of entries more in {USR_row_info[i-1]} as compared to {USR_row_info[0]}', file_name, 'ERROR')
            is_valid = False

    # Dependency row has 0:main, also no special character other than ':'
    HAS_MAIN = False
    for element in dependency_data:
        #regex to match all alphanumeric characters, and exactly one colon
        element = element.strip()
        if re.match(r'^\w+:\w+$', element):
            if element == '0:main':
                HAS_MAIN = True
            continue
        else:
            log(f'Invalid USR : Dependency row has some special character or no/more than one colon or in between unwanted space, or empty value', file_name, 'ERROR')
            is_valid = False
    if not HAS_MAIN:
        log(f'Invalid USR : Dependency row does not contain 0:main', file_name, 'ERROR')
        is_valid = False

    return is_valid

if __name__ == "__main__":
    # Reading filename as command-line argument
    try:
        folder_path = sys.argv[1]
    except IndexError:
        log("No argument given. Please provide path for input folder as an argument.", "", "ERROR")

    files = os.listdir(folder_path)

    # Loop through the list of files and print their names
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)

        file_data = read_file(file_path, file_name)  # Reading USR
        if len(file_data) == 0:
            log('Invalid USR : input file is empty', file_name, 'ERROR')

        rules_info = generate_rulesinfo(file_data, file_name)  # Extracting Rules from each row of USR

        if is_USR_valid(rules_info, file_name):
            log('Valid USR', file_name, 'SUCCESS')

    write_output(file_name_lst, logtype_lst, msg_lst)



