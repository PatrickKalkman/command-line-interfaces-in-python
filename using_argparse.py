from datetime import date, timedelta
import json
import cryptocode
import sys
import argparse


def create_license_file(args):
    licence = {'system_id': args.i,
               'mac_address': args.m,
               'start_date': args.s,
               'end_date': args.e,
               'features': args.f,
               'version': args.u}

    licence_json = json.dumps(licence)
    encrypt_key = f'2020license{args.m}'
    encrypted_json = cryptocode.encrypt(licence_json, encrypt_key)

    with open(f'{args.i}.lic', 'w') as f:
        f.write(encrypted_json)


USAGE = f'python {sys.argv[0]} -m 00:1B:44:11:3A:B7 -s SYS_000001'


def parse():
    parser = argparse.ArgumentParser(
        usage=USAGE,
        description='Create a software license based on the given options')

    parser.add_argument('-m', action='store', type=str, required=True,
                        help='The MAC address of the machine running the software')
    parser.add_argument('-i', action='store', type=str, required=True,
                        help='The system id of the system running the software')
    parser.add_argument('-s', action='store', type=str, required=False,
                        default=date.today().strftime('%Y%m%d'), 
                        help='The start date of the license')
    parser.add_argument('-e', action='store', type=str, required=False,
                        default=(date.today() + timedelta(days=365)).strftime('%Y%m%d'), 
                        help='The end date of the license')
    parser.add_argument('-f', action='store', type=str, required=False,
                        default='all', 
                        help='The features that the software should support')
    parser.add_argument('-u', action='store', type=str, required=False,
                        default='V1.0.0', 
                        help='The version of the software that the license should support')

    return parser.parse_args()


def main():
    args = parse()
    create_license_file(args)


if __name__ == '__main__':
    main()
