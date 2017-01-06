from clarifai.rest import ClarifaiApp
from elasticsearch import Elasticsearch

#TODO : exception handling for clarify api call

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
app = ClarifaiApp("wulQvhs3_7b8rM1jmFZX1bNhm0OzjEV81OPNQPDR", "TdLSlWQka8XQS0t-YknGt0fUil_V49UyvdNdyt1P")

# get the general model
model = app.models.get("general-v1.3")

urls = []
file_path = "/Users/Vhagar/Codes/Artifacia/ImageSearchEngine/ImageSources/ImageURLs"

with open(file_path, "r") as f:
	for line in f:
		line = line.strip()
		urls.append(line)

i = 1
for url in urls:
	# predict with the model
	prediction = model.predict_by_url(url)

	tags = []
	for p in prediction['outputs'][0]['data']['concepts']:
		tags.append(p['name'])

	doc = {
	'url' : url,
	'tags' : tags
	}

	res = es.index(index="test-index", doc_type='images', id=i, body=doc)
	print(res['created'])
	i+=1




