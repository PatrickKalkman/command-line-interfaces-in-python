from datetime import date, timedelta
import json
import cryptocode
import sys
import argparse


# def create_license_file(args):
#     licence = {'system_id': licenseInformation.system_id,
#                'mac_address': licenseInformation.mac_address,
#                'start_date': licenseInformation.start_date,
#                'end_date': licenseInformation.end_date,
#                'features': licenseInformation.features.split(','),
#                'version': licenseInformation.version}

#     licence_json = json.dumps(licence)
#     encrypt_key = f'2020license{licenseInformation.mac_address}'
#     encrypted_json = cryptocode.encrypt(licence_json, encrypt_key)

#     with open(f'{licenseInformation.system_id}.lic', 'w') as f:
#         f.write(encrypted_json)


USAGE = f"""manual_parsing.py - create a software license [version 1.0.0]

Usage: python {sys.argv[0]} -m 00:1B:44:11:3A:B7 -s SYS_000001

-m (required) The MAC address of the machine running the software;
-i (required) The identification of the system running the software;
-s (optional) 'YYYYMMDD' The start date of the license (def today);
-e (optional) 'YYYYMMDD' The end date of the license (def a year from now);
-f (optional) The set of features allowed (def all);
-u (optional) The version of the software that use the license (def v1.0.0);
"""


def parse():
    parser = argparse.ArgumentParser(
        usage=USAGE,
        description='Create a software license based on the given options')

    parser.add_argument('-m', action='store', type=str, required=True)
    parser.add_argument('-i', action='store', type=str, required=True)
    parser.add_argument('-s', action='store', type=str, required=False,
                        default=date.today().strftime('%Y%m%d'))
    parser.add_argument('-e', action='store', type=str, required=False,
                        default=(date.today() + timedelta(days=365)
                                 ).strftime('%Y%m%d'))
    parser.add_argument('-f', action='store', type=str, required=False,
                        default='all')
    parser.add_argument('-u', action='store', type=str, required=False,
                        default='V1.0.0')

    return parser.parse_args()


def main():
    args = parse()
    #create_license_file(args)


if __name__ == '__main__':
    main()
