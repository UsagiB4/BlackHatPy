import argparse

# this tells the program to treat any value that starts with '@' will be treated as 
# prefix_chars says that the arguments will strat with + instead of -
parser = argparse.ArgumentParser(fromfile_prefix_chars='@', prefix_chars='+')

parser.add_argument('+say', type=str, help="print some", required=False)
parser.add_argument('+num1', type=int, help='insert a number', required=False)
parser.add_argument('+num2', type=int, help='enter a number', required=False)
parser.add_argument('+reader', type=argparse.FileType('rt'), required=False)

args = parser.parse_args()
if args.say:
    print(f'f said {args.say}')
if args.num1 and args.num2:
    print(f'total is {args.num1 + args.num2}')
if args.reader:
    print(f'file has:\n{type(args.reader)}')
if args.say == 'getout':
    parser.exit(status=0, message='ok bye!')