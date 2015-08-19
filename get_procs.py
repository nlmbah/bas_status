#
#
#
#
#


def timestamp(input_line):

    month_nr = {'Jan':'01', 'Aug':'08'}

    lst = input_line.split(',')
    year  = lst[6]
    month = month_nr[lst[3]]
    day   = lst[4]
    time  = lst[5]

    return year + '-' + month + '-' + day + ' ' + time

def user(input_line):

    lst = input_line.split(',')
    return lst[0]

def cmd(input_line):
    lst = input_line.split(',')
    tmp = lst[7:]
    return ' '.join(tmp)

def pid(input_line):
    lst = input_line.split(',')
    return lst[1]


def get_procs(look_for='.'):
    from os import popen
    from re import sub, search, compile

    process_status = 'ps -eo user,pid,lstart,command'

    ps = popen(process_status)
    for line in ps:
        if not search('^USER', line) and search(look_for, line):
            line = sub('  *',',',  line.strip() )
            print('%20s, %5s, %20s, %s' %(user(line), pid(line), timestamp(line),cmd(line) ))




def main():
    get_procs('Google')


if __name__ == '__main__':
    main()