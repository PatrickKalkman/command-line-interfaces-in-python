from datetime import date, timedelta
import json
import cryptocode
import typer


def create_license_file(
        mac_address: str, system_id: str,
        start_date: str = date.today().strftime('%Y%m%d'),
        end_date: str = (date.today() + timedelta(days=365)
                         ).strftime('%Y%m%d'),
        features: str = 'all',
        version: str = 'v1.0.0'):

    licence = {'system_id': system_id,
               'mac_address': mac_address,
               'start_date': start_date,
               'end_date': end_date,
               'features': features,
               'version': version}

    licence_json = json.dumps(licence)
    encrypt_key = f'2020license{mac_address}'
    encrypted_json = cryptocode.encrypt(licence_json, encrypt_key)

    with open(f'{system_id}.lic', 'w') as f:
        f.write(encrypted_json)


if __name__ == '__main__':
    typer.run(create_license_file)
