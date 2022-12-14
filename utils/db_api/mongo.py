from pymongo import MongoClient
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from data.config import IP

client = MongoClient(IP)
storage = MongoStorage()

database = client["instagram"]

users_db = database["users"]
like_link_db = database["like_link_db"]
comment_link_db = database["comment_link_db"]