import pymongo

CLIENT = pymongo.MongoClient('mongodb+srv://ahaseko:aaseko100465@cluster0.hqm02.mongodb.net/WebsiteDjango?retryWrites=true&w=majority')
WebsitePribady = CLIENT['websitePribady']