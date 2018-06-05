from elasticsearch import Elasticsearch

es = Elasticsearch(['elasticsearch:9200'])

log1 = { 'outpost': 'Endor', 'datetime': '33 ABY 4AM DST', 'title':'Endor Corps 1: Morning Drill', 'notes': '5100 PRESENT; 15 ABSENT; 130 CODE-RED BELOW PAR PERFORMANCE' }

print("Uploading Stormtroopers Performance Logs")

res = es.index(index="troop_logs", doc_type="log", id=1, body=log1)

print(res['result'], ": ", res)
