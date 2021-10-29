from sys import argv as args
import os
from website.config import EDITOR
import subprocess as sp

if args[1] in ['add', '-a', 'a', 'make', '-m'] and len(args) > 3:
    with open('website/serverless_functions.py', 'a') as f:
        with open(f"functions/{args[4]}", 'r') as f2:
            f.write(f"""
def {args[2]}({args[3]}):
{f2.read()}""")
elif args[1] in ['help', '-h', 'h', 'commands', 'c', '-c']:
    print("""Commands
    add - to add a new function to the file (this cant be undone through the cdn for now) | aliases = ['add', '-a', 'a', 'make', '-m']
    following add enter the function name and args for the function and enter the file which contains the code for the function(just the code without function name)
    Intendation : 4 spaces
    Example : python3 cdn.py add sum a,b sumcode.py""")

elif args[1] in ['edit']:
    os.system(
        f"gnome-terminal --execute bash -c '{EDITOR} website/serverless_functions.py'")
