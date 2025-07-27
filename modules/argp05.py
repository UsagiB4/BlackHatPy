import argparse

parser = argparse.ArgumentParser(
    # prog by default shows the name of the file containing the codes. But we can set the name.
    prog="CoolTool",
    # RawDescriptionHelpFormatter will display the description as it is.
    # formatter_class=argparse.RawDescriptionHelpFormatter,

    # this one is set by default
    # formatter_class=argparse.ArgumentDefaultsHelpFormatter,

    # prints what data type the argument takes.
    # formatter_class=argparse.MetavarTypeHelpFormatter,
    
    # description contains what the program does and how it works
    description="""An amazing python Module called\nARG Parse
    hello world is here
    new era has just begun""",
    # epilog contains extra text that we want to show at the end.
    epilog="Well, It's just an extra text.\nThanks Y'all"
)

parser.add_argument('--say', '-s', help='this will echo back what you give', type=str)
parser.print_help()