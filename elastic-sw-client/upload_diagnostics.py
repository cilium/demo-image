from elasticsearch import Elasticsearch

es = Elasticsearch(['elasticsearch:9200'])


fd1 = { 'spaceshipid': '3459B78XNZTF', 'type': 'tiefighter', 'title': 'Engine Diagnostics', 'stats':'[CRITICAL] [ENGINE BURN @SPEED 5000 km/s] [CHANCE 80%]' }

print("Uploading Spaceship Diagnostics")

res = es.index(index="spaceship_diagnostics", doc_type="stats", id=1, body=fd1)

print(res['result'], ": ", res)


