import csv
from django.core.management.base import BaseCommand
from faker import Faker


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Configuração do Faker
        fake = Faker()

        # Configuração do arquivo CSV
        csv_filename = 'dados_fake.csv'
        fieldnames = ['name', 'birthday', 'nationality']
        num_registros = 20  # Escolha o número desejado de registros

        # Gera dados fake e escreve no arquivo CSV
        with open(csv_filename, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for _ in range(num_registros):
                name = fake.name()
                birthday = fake.date_of_birth().strftime('%Y-%m-%d')
                nationality = fake.country()

                writer.writerow({'name': name, 'birthday': birthday, 'nationality': nationality})

        print(f'Arquivo CSV "{csv_filename}" gerado com sucesso.')
