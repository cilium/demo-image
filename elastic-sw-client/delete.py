from elasticsearch import Elasticsearch

es = Elasticsearch(['elasticsearch:9200'])

print("Deleting Spaceship Diagnostics")

res = es.delete(index="spaceship_diagnostics", doc_type="stats", id=1)

print("Deleting Stormtrooper Performance Log")

res = es.delete(index="troop_logs", doc_type="log", id=1)
