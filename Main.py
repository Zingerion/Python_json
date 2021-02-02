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

all_users_info = []


def get_all_tasks(todos, users):
    total_task_amount = {}
    for user in users:
        individual_tasks = []
        for todo in todos:
            try:
                if todo["userId"] == user["id"]:
                    individual_tasks.append(todo["title"])
            except KeyError:
                pass
        total_task_amount[user["id"]] = individual_tasks
    return total_task_amount


# pprint.pprint(get_all_tasks(todos, users))

def total_amount_task(taskt_list):
    for key in taskt_list:
        task_amount_per_user = len(taskt_list[key])
        all_users_info.append({key : {"amount": task_amount_per_user}})
    return all_users_info

def compl_amount_tasks(taskt_list):
    for key in taskt_list:
        kk

xx = get_all_tasks(todos, users)

# pprint.pprint((xx))
# pprint.pprint(total_amount_task(xx))
total_amount_task(xx)


def test_func(a, b, c):
    print(a + b + c)


LIST = ["Test_Company", "Luis Costa", "BigDick", "gaymail@rot.com", 10, 9, [
    "С другой стороны постоянное информационно-пропагандистское обеспечение нашей деятельности обеспечивает широкому кругу (специалистов) участие в формировании позиций, занимаемых участниками в отношении поставленных задач.",
    "2", "Разнообразный и богатый опыт консультация с широким активом обеспечивает широкому кругу"], 1,
        [
            "С другой стороны постоянное информационно-пропагандистское обеспечение нашей деятельности обеспечивает широкому кругу (специалистов) участие в формировании позиций, занимаемых участниками в отношении поставленных задач.",
            "С другой стороны постоянное информационно-пропагандистское обеспечение нашей деятельности обеспечивает широкому кругу (специалистов) участие в формировании позиций, занимаемых участниками в отношении поставленных задач."]]
test_list = {"arg1": 1, "arg3": 3, "arg2": 2}

test_obj = TEST.TEST(**test_list)
# print(test_obj.arg3)

test_user2 = User_Info.User_Info(*LIST)
# test_user = User_Info.User_Info("Test_Company", "Luis Costa", "BigDick", "gaymail@rot.com", 10, 9, [
#     "С другой стороны постоянное информационно-пропагандистское обеспечение нашей деятельности обеспечивает широкому кругу (специалистов) участие в формировании позиций, занимаемых участниками в отношении поставленных задач.",
#     "2", "Разнообразный и богатый опыт консультация с широким активом обеспечивает широкому кругу"], 1,
#                                 [
#                                     "С другой стороны постоянное информационно-пропагандистское обеспечение нашей деятельности обеспечивает широкому кругу (специалистов) участие в формировании позиций, занимаемых участниками в отношении поставленных задач.",
#                                     "С другой стороны постоянное информационно-пропагандистское обеспечение нашей деятельности обеспечивает широкому кругу (специалистов) участие в формировании позиций, занимаемых участниками в отношении поставленных задач."])
