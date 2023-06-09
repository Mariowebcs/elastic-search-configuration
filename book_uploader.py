from elastic_data import get_client
import csv


def upload_file_data():
    client = get_client()
    print('Connected to elastic search cluster : {}'.format(client.info().body['cluster_name']))
    f = None
    try:
        with open('./book.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for i, line in enumerate(reader):
                data = {
                    "author": line[0],
                    "title": line[1],
                    "preface": line[2]
                }
                client.index(index="books", document=data, id=i)
                print(data)
    except Exception as e:
        print('L\'errore è : {}'.format(e))
    except FileNotFoundError as e:
        print('File non trovato, si prega di verificare e riprovare!')
    finally:
        if f is not None:
            f.close()
    book = client.get(index='books', id='1')
    print(book)


upload_file_data()
