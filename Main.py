import requests
import json
import os
import User_Info
import API_func


# create dir if it doesn't exist
if not os.path.isdir("tasks"):
    os.mkdir("tasks")


# go to dir if we are not there
if not "tasks" in os.getcwd():
    os.chdir("tasks")


# get json files to work with them
todos_json = requests.get("https://json.medrating.org/todos")
todos = json.loads(todos_json.text)


users_json = requests.get("https://json.medrating.org/users")
users = json.loads(users_json.text)


# global structure to store user's data for output
all_users_info = {}


# fields we need to get
personal_info = ["name", "username", "email"]


API_func.get_all_tasks_info(todos, users,all_users_info)


for field in personal_info:
    API_func.get_personal_info(users, all_users_info, field)


API_func.get_company_name(users, all_users_info)


# create files with every user' info from the global structure
for user_info in all_users_info:
    try:
        User_Info.User_Info(**all_users_info[user_info])
    except TypeError:
        pass