from pymongo import MongoClient
from domain.models.log import Log

class LogsRepository:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client["logs_db"]
        self.logs_collection = self.db["logs"]

    def save_log(self, log: Log):
        self.logs_collection.insert_one(log.dict())

    def get_logs(self):
        logs = []
        for log in self.logs_collection.find():
            log_dict = log
            log_dict['id'] = str(log_dict['_id'])
            del log_dict['_id']
            logs.append(Log(**log_dict))
        return logs