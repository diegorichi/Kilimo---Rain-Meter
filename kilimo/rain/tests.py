from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient

from django.test.client import encode_multipart, RequestFactory

client = APIClient()
response = client.get('/rains')
assert response.status_code == 200
response = client.get('/grounds')
assert response.status_code == 200

response = client.post('/grounds',
{
    'name': 'My Ground',
    'lat': '21',
    'lon': '11',
    'hectare': '15'
})
assert response.status_code == 201
ground_id = response.json()['id']
print (ground_id)
response = client.post('/rains',
{
    'rain_date': '2020-07-22',
    'rainfall': '5',
    'ground': ground_id
})
response = client.post('/rains',
{
    'rain_date': '2020-07-21',
    'rainfall': '11',
    'ground': ground_id
})
response = client.post('/rains',
{
    'rain_date': '2020-07-20',
    'rainfall': '5',
    'ground': ground_id
})

response = client.get('/grounds/{}/rains'.format(ground_id))
assert response.status_code == 200

response = client.get('/grounds/avg_rains?N=5')
assert response.status_code == 200

assert response.json()[0]['average'] == 7.0
response = client.get('/grounds/sum_rains?N=5')
assert response.status_code == 200
assert response.json()[0]['sum'] == 21

response = client.delete('/grounds/{}'.format(ground_id))
assert response.status_code == 204


response = client.get('/grounds/10000')
assert response.status_code == 404

response = client.post('/grounds',
{
    'name': 'Ssja Gslasnd',
    'lat': '21',
    'lon': '11',
    'hectare': '15'
})
assert response.status_code == 201

id = response.json()['id']

response = client.delete('/grounds/{}'.format(id))
assert response.status_code == 204
