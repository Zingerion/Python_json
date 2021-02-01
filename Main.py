import re
import requests
import datetime
import json
import pprint
import User_Info
import os
import libs

if not os.path.isdir("tasks"):
    os.mkdir("tasks")

if not "tasks" in os.getcwd():
    os.chdir("tasks")

todos_json = requests.get("https://json.medrating.org/todos")
todos = json.loads(todos_json.text)

users_json = requests.get("https://json.medrating.org/users")
users = json.loads(users_json.text)


test_user = User_Info.User_Info("Test_Company", "Luis Costa", "BigDick","gaymail@rot.com", 10, 9, ["С другой стороны постоянное информационно-пропагандистское обеспечение нашей деятельности обеспечивает широкому кругу (специалистов) участие в формировании позиций, занимаемых участниками в отношении поставленных задач.", "2", "Разнообразный и богатый опыт консультация с широким активом обеспечивает широкому кругу"], 1,
                                ["С другой стороны постоянное информационно-пропагандистское обеспечение нашей деятельности обеспечивает широкому кругу (специалистов) участие в формировании позиций, занимаемых участниками в отношении поставленных задач.", "С другой стороны постоянное информационно-пропагандистское обеспечение нашей деятельности обеспечивает широкому кругу (специалистов) участие в формировании позиций, занимаемых участниками в отношении поставленных задач."])


# test_user.get_date_time()

