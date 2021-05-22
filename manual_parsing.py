from datetime import date, timedelta
from typing import List
import json
import cryptocode
import sys
import collections


class LicenseInformation:
    def __init__(self,
                 mac_address='',
                 system_id='',
                 start_date=date.today().strftime('%Y%m%d'),
                 end_date=(date.today() + timedelta(days=365)
                           ).strftime('%Y%m%d'),
                 features='all',
                 version='v1.0.0'):
        self.mac_address = mac_address
        self.system_id = system_id
        self.start_date = start_date
        self.end_date = end_date
        self.features = features
        self.version = version


def create_license_file(licenseInformation: LicenseInformation):
    licence = {'system_id': licenseInformation.system_id,
               'mac_address': licenseInformation.mac_address,
               'start_date': licenseInformation.start_date,
               'end_date': licenseInformation.end_date,
               'features': licenseInformation.features.split(','),
               'version': licenseInformation.version}

    licence_json = json.dumps(licence)
    encrypt_key = f'2020license{licenseInformation.mac_address}'
    encrypted_json = cryptocode.encrypt(licence_json, encrypt_key)

    with open(f'{licenseInformation.system_id}.lic', 'w') as f:
        f.write(encrypted_json)


USAGE = f"""manual_parsing.py - create a software license [version 1.0.0]

Usage: python {sys.argv[0]} -m 00:1B:44:11:3A:B7 -s SYS_000001

-m (required) The MAC address of the machine running the software;
-i (required) The identification of the system running the software;
-s (optional) 'YYYYMMDD' The start date of the license (default today);
-e (optional) 'YYYYMMDD' The end date of the license (default a year from now);
-f (optional) The set of features allowed (default all);
-v (optional) The version of the software that use the license (default v1.0.0);"""


def parse(args: List[str]) -> LicenseInformation:

    if len(args) == 0:
        print(USAGE)
        exit(0)

    license = LicenseInformation()
    argument_from_queue = collections.deque(args)
    while argument_from_queue:
        argument = argument_from_queue.popleft()
        if argument in ['-h', '--help']:
            print(USAGE)
            sys.exit(0)
        elif argument == '-m':
            license.mac_address = argument_from_queue.popleft()
        elif argument == '-i':
            license.system_id = argument_from_queue.popleft()
        elif argument == '-s':
            license.start_date = argument_from_queue.popleft()
        elif argument == '-e':
            license.start_date = argument_from_queue.popleft()
        elif argument == '-f':
            license.features = argument_from_queue.popleft()
        elif argument == '-v':
            license.version = argument_from_queue.popleft()

    return license


def main():
    license = parse(sys.argv[1:])
    create_license_file(license)


if __name__ == '__main__':
    main()
