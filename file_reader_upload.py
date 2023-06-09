import csv
import uuid
import elasticsearch
from elastic_data import get_client


def upload_file_data():
    client = get_client()
    print('Connected to elastic search cluster : {}'.format(client.info().body['cluster_name']))
    f = None
    try:
        with open('./ford_escort.csv', 'r') as f:
            reader = csv.reader(f)
            for i, line in enumerate(reader):
                data = {
                    "year": line[0],
                    "price": line[2]
                }
                client.index(index="cars", document=data, id=uuid.uuid1())
                print(data)
    except Exception as e:
        print('L\'errore è : {}'.format(e))
    except FileNotFoundError as e:
        print('File non trovato, si prega di verificare e riprovare!')
    finally:
        if f is not None:
            f.close()
    car = client.get(index="cars", id="6")
    print(car)

upload_file_data()
