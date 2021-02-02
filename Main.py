import re
import requests
import datetime
import json
import pprint
import User_Info
import os
import libs
import TEST

if not os.path.isdir("tasks"):
    os.mkdir("tasks")

if not "tasks" in os.getcwd():
    os.chdir("tasks")

todos_json = requests.get("https://json.medrating.org/todos")
todos = json.loads(todos_json.text)

users_json = requests.get("https://json.medrating.org/users")
users = json.loads(users_json.text)

all_users_info = {}


def get_all_tasks(todos, users):
    for user in users:
        completed_task_list = []
        remain_task_list = []
        total_task_amount = []
        for todo in todos:
            try:
                if todo["userId"] == user["id"]:
                    if todo["completed"]:
                        completed_task_list.append(todo["title"])
                    else:
                        remain_task_list.append(todo["title"])
            except KeyError:
                pass
        all_users_info[user["id"]] = {}
        all_users_info[user["id"]]["amount"] = len(completed_task_list) + len(remain_task_list)
        all_users_info[user["id"]]["compl_tasks"] = completed_task_list
        all_users_info[user["id"]]["compl_amount"] = len(completed_task_list)
        all_users_info[user["id"]]["remain_tasks"] = remain_task_list
        all_users_info[user["id"]]["remain_amount"] = len(remain_task_list)
    return all_users_info


get_all_tasks(todos, users)

personal_info = ["name", "username", "email"]


def get_personal_info(users, all_users_info, search_info):
    for user in users:
        try:
            all_users_info[user["id"]][search_info] = user[search_info]
        except KeyError:
            pass


for i in personal_info:
    get_personal_info(users, all_users_info, i)


def get_company_name(users, all_users_info):
    for user in users:
        try:
            all_users_info[user["id"]]["company"] = user["company"]["name"]
        except KeyError:
            pass


get_company_name(users, all_users_info)

for i in all_users_info:
    try:
        User_Info.User_Info(**all_users_info[i])
    except TypeError:
        pass
