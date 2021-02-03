import datetime
import re
import os
import libs
from threading import Thread
import shutil


class User_Info:
    """This class creates file with user's info """
    def __init__(self, company, name, username, email, amount, compl_amount, compl_tasks, remain_amount, remain_tasks):
        self.company = company
        self.name = name
        self.username = username
        self.email = email
        self.amount = amount
        self.compl_amount = compl_amount
        self.compl_tasks = compl_tasks
        self.remain_amount = remain_amount
        self.remain_tasks = remain_tasks
        self.save_txt()


    #creates string with company info
    def make_file_header (self):
        first_string = "Отчет для" + ' ' + self.company + '.' + '\n'
        return first_string


    #creates string with name, mail and current date info
    def make_second(self):
        today = datetime.datetime.now()
        proper_format_today = today.strftime("%d.%m.%Y %H:%M")
        second_string = self.name + ' ' + '<' + self.email + '>' + ' ' + proper_format_today + '\n'
        return second_string


    #creates string with total amount tasks per user
    def make_total_amount(self):
        total_amount = "Всего задач: " + str(self.amount) + '\n\n'
        return total_amount


    # creates string with amount of completed tasks per user
    def make_compl_amount(self):
        compl_amount_str = "Завершенные задачи: " + '(' + \
                           str(self.compl_amount) + '):' + '\n'
        return compl_amount_str


    # creates string with amount of remaining tasks
    def make_ramain_amount(self):
        remain_amount_str = "Оставшиеся задачи: " + '(' + \
                            str(self.remain_amount) + '):' + '\n'
        return remain_amount_str

    # creates string where all required tasks are listed
    def make_list(self,name, field):
        name = ''
        for task in field:
            if len(task) > 48:
                name += task[0:48] + '...' + '\n'
            else:
                name += task + '\n'
        name += '\n'
        return name


    # joins all strings with user info
    def join_user_info(self):
        filed_file = self.make_file_header() + self.make_second() + \
                     self.make_total_amount() + self.make_compl_amount() + \
                     self.make_list("compl_tasks_list", self.compl_tasks) + self.make_ramain_amount() +\
                     self.make_list("remain_tasks_list",self.remain_tasks)
        return filed_file


    # retrieves date and time creation info from the existing file
    def get_date_time(self, exist_file ):
        with open(exist_file) as my_file:
            my_file = my_file.readlines()[1]
            # looking for a sequence of characters
            # that fit the date format
            date_from_file = re.search(r'\d{1,2}.\d{1,2}.\d{4}\s\d{2}:\d{2}',
                                       my_file)
            date_from_file = date_from_file.group(0)
            # convert from string to the date format
            proper_format_date = datetime.datetime.strptime(date_from_file,
                                                            "%d.%m.%Y %H:%M")
            # convert to the date format we need
            proper_date = proper_format_date.strftime("%Y-%m-%dT%H-%M")
            return proper_date


    # create and save file with all user info
    def create_new_file(self, path, make_file_func):
        new_user_file = open(path, "w")
        new_user_file.write(make_file_func)
        new_user_file.close()
        return


    # if file exists, func creates copy and updates the file content
    # if file doesn't exist, func creates it
    def save_txt(self):
        file_name = str(self.username + ".txt")
        if os.path.isfile(file_name):
            shutil.copy(file_name, "old_" + self.username + "_" +
                        self.get_date_time(file_name) + ".txt")
        self.create_new_file(file_name, self.join_user_info())
        return
