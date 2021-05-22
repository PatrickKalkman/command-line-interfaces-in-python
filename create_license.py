from datetime import datetime, date
import json
import cryptocode

def create_license_file(system_id, mac_address, start_date, end_date,
                        features, version):
    licence = {'system_id': system_id,
               'mac_address': mac_address,
               'start_date': start_date.strftime('%Y%m%d'),
               'end_date': end_date.strftime('%Y%m%d'),
               'features': features.split(','),
               'version': version}

    licence_json = json.dumps(licence)

    encrypt_key = f'2020license{mac_address}'

    encrypted_json = cryptocode.encrypt(licence_json, encrypt_key)

    with open(f'{system_id}.lic', 'w') as f:
        f.write(encrypted_json)

def main():
    create_license_file('SYS_000001', '00:1B:44:11:3A:B7',
                        datetime(2021, 6, 1), datetime(2022, 6, 1),
                        'feature1,feature2', 'v1.0.0')

if __name__ == '__main__':
    main()
