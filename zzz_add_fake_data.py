'''
This file i will run it will cause the fake data will insert in my db
zzz_add_fake_data.py
'''
import random


from db_codes.database_make import engine
from db_codes.db_functions import add_new_user, add_new_note
from db_codes.models_table import UserData, NoteData

print("I will add code here for insert fake data")