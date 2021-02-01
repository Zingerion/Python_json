import datetime
import re
import os
import libs
class User_Info:
    def __init__(self,company,name,username,mail,amount,compl_amount,compl_tasks,remain_amount,remain_tasks):
        self.company = company
        self.name = name
        self.username = username
        self.mail = mail
        self.amount = amount
        self.compl_amount = compl_amount
        self.compl_tasks = compl_tasks
        self.remain_amount = remain_amount
        self.remain_tasks = remain_tasks
        self.save_txt()
    def make_top(self):
        first_string = "Отчет для" + ' ' + self.company + '.' + '\n'
        return first_string

    def make_second(self):
        today = datetime.datetime.today()
        proper_format_today = today.strftime("%d.%m.%Y %H:%M")
        second_string = self.name + ' ' + '<' + self.mail + '>' + ' ' + proper_format_today + '\n'
        return second_string

    def make_total_amount(self):
        total_amount = "Всего задач: " + str(self.amount) + '\n\n'
        return total_amount

    def make_compl_amount(self):
        compl_amount_str = "Завершенные задачи: " + '(' + str(self.compl_amount)  + '):' + '\n'
        return compl_amount_str

    def make_compl_list(self):
        compl_tasks_list = ''
        for task in self.compl_tasks:
            if len(task) > 48:
                compl_tasks_list += task[0:48] + '...' + '\n'
            else:
                compl_tasks_list += task + '\n'
        compl_tasks_list += '\n'
        return compl_tasks_list

    def make_ramain_amount(self):
        remain_amount_str = "Оставшиеся задачи: " + '(' + str(self.remain_amount) + '):' + '\n'
        return remain_amount_str

    def make_ramain_list(self):
        remain_tasks_list = ''
        for task in self.remain_tasks:
            if len(task) > 48:
                remain_tasks_list += task[0:48] + '...' + '\n'
            else:
                remain_tasks_list += task + '\n'
        remain_tasks_list += '\n'
        return remain_tasks_list

    def make_file(self):
        filed_file = self.make_top() + self.make_second() + self.make_total_amount() + self.make_compl_amount() + self.make_compl_list() + self.make_ramain_amount() + self.make_ramain_list()
        return filed_file

    def get_date_time(self):
        # if (os.path.isfile(self.username + ".txt")):
            with open(self.username + ".txt") as my_file:
                my_file = my_file.readlines()[1]
                date_from_file = re.search(r'\d{1,2}.\d{1,2}.\d{4}\s\d{2}:\d{2}', my_file)
                date_from_file = date_from_file.group(0)
                proper_format_date =  datetime.datetime.strptime(date_from_file,"%d.%m.%Y %H:%M")
                proper_date = proper_format_date.strftime("%Y-%m-%dT%H-%M")
                return proper_date

    def save_txt(self):
        file_name = str(self.username + ".txt")
        if not os.path.isfile(file_name):
            my_file = open(file_name, "w")
            my_file.write(self.make_file())
            my_file.close()
        else:
            os.rename(file_name,"old_" + self.username + "_" + self.get_date_time() + ".txt")

