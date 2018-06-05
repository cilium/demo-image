import time
from elasticsearch import Elasticsearch

es = Elasticsearch(['elasticsearch:9200'])

fd1 = { 'spaceshipid': '3459B78XNZTF', 'type': 'tiefighter', 'title': 'Engine Diagnostics', 'stats':'[OK] [ENGINE OK @SPEED 5000 km/s]' }

print("Uploading Spaceship Diagnostics")

res = es.index(index="spaceship_diagnostics", doc_type="stats", id=1, body=fd1)

time.sleep(2)
res = es.search(index="spaceship_diagnostics", body={"query": {"match_all": {}}})
for hit in res['hits']['hits']:
    print(hit)


