#
# read Bagtrax sys.ini
#
#
from sys import argv
import ConfigParser


def Read_sys_ini(input_file, look_for_process='.', look_for_option='.'):
    '''
    '''
    from re import search, compile, IGNORECASE
    config = ConfigParser.RawConfigParser()
    config.read(input_file)
    
    sections = config.sections()
    
    pattern_process = compile(look_for_process)
    pattern_option  = compile(look_for_option, IGNORECASE)
    dict = {}
    for section in sections:
        if pattern_process.search(section):
            for option in config.options(section):
                if pattern_option.search(option):
                    dict[section] = config.get(section, option)
    
    return dict


def main(input):
    '''
    '''
    sys_ini = Read_sys_ini(input[1], 'BDC_', '^HostName')

    # print result
    print('%s data' %(input[1]))
    for key,value in sys_ini.iteritems():
            print('key: %s, value:%s' %(key, value))
    

if __name__ == '__main__':
    main(argv)        