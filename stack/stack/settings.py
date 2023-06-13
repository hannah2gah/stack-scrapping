BOT_NAME = "stack"

SPIDER_MODULES = ["stack.spiders"]
NEWSPIDER_MODULE = "stack.spiders"

ITEM_PIPELINES = {'stack.pipelines.MongoDBPipeline':300}

MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'stackoverflow'
MONGODB_COLLECTION = 'questions'