import pymongo

from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem
from logging import log

class MongoDBPipeline(object):
    def __init__(self):
        settings = get_project_settings()
        
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )

        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
    
    def process_item(self, item, spider):
        valid = True

        for data in item:
            if not data:
                valid = False

                raise DropItem(f'Missing {data}!')
        if valid:
            self.collection.insert(dict(item))
            log('Question added to MongoDB database!', level = log.DEBUG, spider=spider)
        
        return item