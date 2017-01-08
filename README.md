# [ImageSearchEngine](http://ec2-54-171-138-164.eu-west-1.compute.amazonaws.com/_site/index.html)

indexImages.py : indexes Url's stored in the file "ImageSearchEngine/ImageSources/ImageURLs" into ElasticSearch.
settings_elasticSearch : Settings for ElasticSearch server are stored here

On any change in the query box, the function delayedSearch() is called. This function is located in js/controllers.js
This function calls search() which in turn calls loadResults().
The main call to ElasticSearch server is made from services.js

## How to run the code?
A running instance of ElasticSearch server is required. You can set up your own or use the one setup [here](http://ec2-54-171-138-164.eu-west-1.compute.amazonaws.com:9200).
You can use "indexImages.py" to index more url's.

Host the \_site folder somewhere and hit the page index.html. The search functionality is up and running. 
