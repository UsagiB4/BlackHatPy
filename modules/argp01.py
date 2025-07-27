# basic of argpurse
import argparse

parser = argparse.ArgumentParser()

'''
these are positional arguments
both arguments must be supplied during execution.
there will be error otherwise.
'''
parser.add_argument("echo") # simple argumnet
parser.add_argument("cool_name", help="say your name!") # argument with help mesg.
parser.add_argument("num", help="Enter a number and see magic", type=int) # type hinting
args = parser.parse_args()
print(f'you said {args.echo}')
print(f'{args.cool_name} is a cool name')
print(f'{args.num} power 2 = {args.num**2}')

# next optional arguments