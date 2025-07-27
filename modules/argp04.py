import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--slot', '-s', help='Select a slot number from 1 to 10', choices=range(1, 10), type=int, metavar='num', required=False)
parser.add_argument('--date', '-d', help='Specify date', choices=range(1, 31), type=int, metavar='DD')
parser.add_argument('--month', '-m', help="Specify Month", choices=range(1, 12), type=int, metavar='MM')
parser.add_argument('--year', '-y', help='Specify Year', type=int, metavar='YYYY')
args = parser.parse_args()
if args.slot == 1:
    print('Slot level one is selected.')
elif args.slot == 2:
    print('Slot level two is selected.')
elif args.slot == 3:
    print('Slot level three is selected')
elif args.slot == 4:
    print("Slot level four is selected.")
else:
    print(f'Slot level {args.slot} is selected')