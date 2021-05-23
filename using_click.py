from datetime import date, timedelta
import json
import cryptocode
import click

@click.command()
@click.option('-m', help='The MAC address of the machine running the software', required=True)
@click.option('-i', help='The system id of the machine running the software', required=True)
@click.option('-s', help='The start date of the license', default=date.today().strftime('%Y%m%d'))
@click.option('-e', help='The end date of the license', default=(date.today() + timedelta(days=365)).strftime('%Y%m%d'))
@click.option('-f', help='The features of the license', default='all')
@click.option('-u', help='The version of the software using the license', default='v1.0.0')
def create_license_file(m, i, s, e, f, u):
    licence = {'system_id': i,
               'mac_address': m,
               'start_date': s,
               'end_date': e,
               'features': f,
               'version': u}

    licence_json = json.dumps(licence)
    encrypt_key = f'2020license{m}'
    encrypted_json = cryptocode.encrypt(licence_json, encrypt_key)

    with open(f'{i}.lic', 'w') as f:
        f.write(encrypted_json)


def main():
    create_license_file()


if __name__ == '__main__':
    main()
