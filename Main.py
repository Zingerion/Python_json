import re

import requests
import datetime
import json
import pprint
import User_Info
import os


# var = ['www.pythonru', 'com']
# print ('\n'.join(var))
# today = datetime.datetime.today()
# print( today.strftime("%d.%m.%Y %H:%M") )


# url1 = 'https://json.medrating.org/todos'
# url2 = 'https://json.medrating.org/users'
# whole_json_1 = requests.get(url1)
# whole_json_2 = requests.get(url2)
# data = whole_json_1.json()
# data2 = whole_json_2.json()
# print(data, '\n', data2)


# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
#
# # Map of userId to number of complete TODOs for that user
# todos_by_user = {}
#
# # Increment complete TODOs count for each user.
# for todo in todos:
#     if todo["completed"]:
#         try:
#             # Increment the existing user's count.
#             todos_by_user[todo["userId"]] += 1
#         except KeyError:
#             # This user has not been seen. Set their count to 1.
#             todos_by_user[todo["userId"]] = 1
#
# # Create a sorted list of (userId, num_complete) pairs.
# top_users = sorted(todos_by_user.items(),
#                    key=lambda x: x[1], reverse=True)
#
# # Get the maximum number of complete TODOs.
# max_complete = top_users[0][1]
#
# # Create a list of all users who have completed
# # the maximum number of TODOs.
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
#
# max_users = " and ".join(users)
#
# # Define a function to filter out completed TODOs
# # of users with max completed TODOS.
# def keep(todo):
#     is_complete = todo["completed"]
#     has_max_count = str(todo["userId"]) in users
#     return is_complete and has_max_count
#
# # Write filtered TODOs to file.
# with open("filtered_data_file.json", "w") as data_file:
#     filtered_todos = list(filter(keep, todos))
#     json.dump(filtered_todos, data_file, indent=2)

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

