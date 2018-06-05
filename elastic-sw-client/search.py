from elasticsearch import Elasticsearch

es = Elasticsearch(['elasticsearch:9200'])

print("Searching for Spaceship Diagnostics")
res = es.search(index="spaceship_diagnostics", body={"query": {"match_all": {}}})

print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print(hit)

print("Searching for Stormtroopers Performance Logs")
res = es.search(index="troop_logs", body={"query": {"match_all": {}}})

print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print(hit)
