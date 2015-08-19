#
# Read the LHR bagtrax process.db
#
from sys import argv


def read_process_db(input_file, look_for='.'):
    '''
    Objective : Read the processes from the process.db file
    Input     : process.db file, which process to look for.
    Output    : 
    '''
    from sys import exit
    from re import search, compile
    
    output = list()
    try:
        process_db = open(input_file, 'r')
    except Exception as error:
        print('Could not open %s due to %s' %(input_file, error))
        exit(-1)
    else:
        pattern = compile(look_for)
        for line in process_db:
            if pattern.search(line):
                output.append(line.rstrip().split(','))
        process_db.close()
    return output
    

def main(input):
    '''
    '''

    # read the process db file into a list    
    processes = read_process_db(input[1], 'BDC_.*_05_')
    #processes = read_process_db(input[1])
    
    # print the result
    for line in processes:
        print line



if __name__ == '__main__':
    main(argv)