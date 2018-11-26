import argparse
import sys
import os
parser = argparse.ArgumentParser(description="")
parser.add_argument('-start', dest='start', action='store', type=int, required=True)
parser.add_argument('-step', dest='step', action='store', type=int, required=True)

subparsers = parser.add_subparsers(dest='command')
save_parser = subparsers.add_parser('save')
save_parser.add_argument('-i', dest='path', required=True)
show_parser = subparsers.add_parser('show')

args = parser.parse_args(sys.argv[1:])
n = 10
lst = []
for i in range(n):
    next = args.start + i * args.step
    lst.append(next)
if args.command == 'show':
    print(lst)
if args.command == 'save':
    file_name = args.path
    dir_name = os.path.dirname(file_name)
    if os.path.exists(dir_name):
        with open(file_name, 'wt') as f:
            f.write(str(lst))
    else:
        print(f"такого каталога {dir_name} не существует!")
