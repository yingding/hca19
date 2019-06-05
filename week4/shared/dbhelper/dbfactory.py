# Tutorial for pymongo 3 http://api.mongodb.com/python/current/tutorial.html
from pymongo import MongoClient, database;
# import datetime as dt


class DBFactory:

    @classmethod
    def getDB(cls, host: str, db: str, user: str, password: str) -> database.Database:
        uri = "mongodb://{0}:{1}@{2}:27017/{3}?authMechanism=SCRAM-SHA-1".format(user, password, host, db)
        client = MongoClient(uri)
        db = client.get_default_database()
        return db

    @classmethod
    def test(cls, db: database.Database):
        for name in db.list_collection_names():
            print(name)


# def getComputedStressList(examInfo, user, shift=0, pospond=0, db=getDB()):
#     # user = examSession.getUser()
#     gmt_begin = examInfo.startDate - dt.timedelta(minutes=shift)
#     gmt_end = examInfo.endDate + dt.timedelta(minutes=pospond)
#     # convert GMT datetime to GMT timestamp
#     timestamp_begin = unix_time_secs(gmt_begin)
#     timestamp_end = unix_time_secs(gmt_end)
#
#     cs_results = list(db[user.getMatrNr() +'_hrvdata'].find({
#             '_id.timestamp':{
#                 '$gt':timestamp_begin,
#                 '$lt':timestamp_end
#             }
#     }))
#     return cs_results
#
# def getHeartRateList(examInfo, user, shift=0, pospond=0, db=getDB()):
#     # user = examSession.getUser()
#     gmt_begin = examInfo.startDate - dt.timedelta(minutes=shift)
#     gmt_end = examInfo.endDate + dt.timedelta(minutes=pospond)
#     # convert GMT datetime to GMT timestamp
#     timestamp_begin = unix_time_secs(gmt_begin)
#     timestamp_end = unix_time_secs(gmt_end)
#
#     hr_results = list(db[user.getMatrNr() + '_heartrate'].find({
#             '_id.timestamp':{
#                 '$gt':timestamp_begin,
#                 '$lt':timestamp_end
#             }
#     }))
#     return hr_results