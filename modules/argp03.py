# A little deep dive into argparse
import argparse

parser = argparse.ArgumentParser()
# showes version number. will print the file name here.
parser.add_argument('-ver','--version', action='version', version='%(prog)s 2.0', help='Showing version')
# Storing a constant. the "const" is set to 'None' by default.
parser.add_argument('--ourconst', action='store_const', const=32, help='we have a constant. Default value is 32')
# storing true. we also can use 'sotre_false' to store 'false'
parser.add_argument('--truth', action='store_true', help='True is here')
# appends multiple values of a single argument
parser.add_argument('--apnnum', action='append', type=int, help='takes multiple intiger value and stores them.\n e.g: --apnnum 33 --apnnum 354 --apnnum 221')
# this will count how many time the argument has been used
parser.add_argument('--verbose', '-v', action='count', help='verbose mode. use multiple time to increase the result.')
args = parser.parse_args()

numberList = args.apnnum

if args.verbose == 1:
    if numberList != None:
        for i in numberList:
            print(i)
    else:
        print('verbose mode 1')
    

elif args.verbose == 2:
    if numberList != None:
        for i in numberList:
            print(f'The number is: {i}')
    else:
        print('verbose mode 2')
elif args.verbose == 3:
    if numberList != None:
        print(f'The complete list is {numberList}')
        for i in numberList:
            print(f'we have {i} in position of {numberList.index(i)}')
    else:
        print('verbose mode 3')
else:
    if numberList != None:
        print(numberList)
    else:
        print('non verbose mode')
        