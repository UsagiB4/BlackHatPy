import argparse

parse = argparse.ArgumentParser()

'''
now we will learn to use optional arguments.
these arguments are not mandatory during execution and can be avoided.
'''

# uncoment this to run

# parse.add_argument("word", help="say something you like")
# parse.add_argument("--vsity", help="increase verbosity. WOW!") # this will be our optional argument
# args = parse.parse_args()
# if args.vsity:
#     print('you turned on verbosity. Good job')
# print(f'watch me printing the thing that you said: \n-----------\n{args.word}')


# a simple program

newPars = argparse.ArgumentParser()
newPars.add_argument('--num', help="Enter a number", type=int)
# below::: we have multiple option name "v" and "verbos" also we have set the default value of verbosity to "True" using "action".
#newPars.add_argument('-v', "--verbos", help="Increase output verbosity", action="store_true")

#below::: we have added values for our option using "choices"
#newPars.add_argument('-v', '--verb', help="increase verbos output.", type=int, choices=[0,1,2])

#below::: we have added an "action" called "count" which will the number of options used as like: "-v -vv -vvv"
newPars.add_argument('-v', '--verb', help="increase verbos output. use nothing for non verbose output -v, -vv", action="count")
newargs = newPars.parse_args()
numb = newargs.num
power = numb**2
if newargs.verb == 1:
    print(f'{numb} square is = {power}')
elif newargs.verb == 2:
    print(f'We have got your number.\nPlease wait for the result\nResult:\n{numb} square is = {power}')
else:
    print(power)


