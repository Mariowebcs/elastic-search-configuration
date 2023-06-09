from elastic_data import get_client, ELASTIC_PASSWORD
from file_reader_upload import upload_file_data

client = get_client()
print(client.info())

data_1 = {"city": "Cosenza", "country": "Italy"}
data_2 = {"city": "Rende", "country": "Italy"}
data_3 = {"city": "Praga", "country": "Belgium"}
data_4 = {"name": "Mario"}
new_data = {"name": "Prova"}

client.index(index="cities", id="1", document=data_1)
client.index(index="cities", id="2", document=data_2)
client.index(index="cities", id="3", document=data_3)
client.index(index="prova", id="1", document=data_4)
client.update(index="prova", id="1", doc=new_data)
res = client.get(index="cities", id="1")
print(res)
print(client.ping())

upload_file_data()


"""response = requests.get('https://localhost:9200', auth=('elastic', 'root356595'))
data = response.json()
for row in data:
    print(row)"""
