import sys
import argparse


def main(argv):
    opt = argparse.ArgumentParser()
    opt.add_argument('filename', type=str, help='masukan alamat file [./]')
    opt.add_argument('-v', '--version', action='version', version='beta tester [0.1]')
    args = opt.parse_args()

    def replace(file):
        with open(file) as lists:
            for list in lists:
                # data = '{0}{1}{2}'.format('zone "', line.rstrip(), '" IN {type master;file "/usr/local/etc/namedb/data/blocking/haramsite.db";allow-transfer { 124.40.250.253;};};\n')
                base1 = 'zone "'
                base2 = '" IN {type master;file "/usr/local/etc/namedb/data/blocking/haramsite.db";allow-transfer { 124.40.250.253;};};\n'
                data = base1 + list.rstrip() + base2
                x = open('jal.txt', 'a')
                x.write(data)
                x.close

    if args.filename:
        replace(args.filename)
    else:
        none


if __name__ == '__main__':
    if len(sys.argv[1:]) == 0:
        print("Usage: thisapp.py [filename] || more [--help]")
        exit
    else:
        main(sys.argv[1:])