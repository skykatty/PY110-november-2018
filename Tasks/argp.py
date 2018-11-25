import sys
import argparse
import json

def seqencer(start):
    n = start
    while True:
        data = yield n
        if data is None:
            n += 1
        else:
            n = data

print(sys.argv)
parser = argparse.ArgumentParser(description="Арифметическая прогрессия")
parser.add_argument('-start', dest='start', action='store', type=int, required=True, help='начальное значение')
parser.add_argument('-step', dest='step', action='store', type=int, required=True, help='шаг')
parser.add_argument('-count', dest='count', action='store', type=int, required=True, help='количество')
# subparser = parser.add_subparsers(dest='cmd')
# parser.add_argument('-output', dest='out', action='store', type=str, help='имя файла')

subparsers = parser.add_subparsers(dest='cmd') # choices=['save', 'show']
fs_parser = subparsers.add_parser('save')
fs_parser.add_argument('-i', dest='fname', required=True)
show_parser = subparsers.add_parser('show')


args = parser.parse_args(sys.argv[1:])

print('start {} step {} count {} cmd {}'.format(args.start, args.step, args.count, args.cmd))

g = seqencer(0)
g.send(None)

cou = 1
st = 0
lst = []
lst.append(g.send(args.start))
while cou < args.count:
    st += 1
    if st == args.step:
        lst.append(g.send(None))
        st = 0
        cou += 1
    else:
        g.send(None)


if args.cmd == 'show':
    print(lst)
else:
    print('fname {}'.format(args.fname))
    with open(args.fname, 'wt') as f:
        f.write(json.dumps(lst))
