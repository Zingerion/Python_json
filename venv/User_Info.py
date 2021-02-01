import datetime
class User_Info:
    def __init__(self,company,name,mail,amount,compl_amount,compl_tasks,remain_amount,remain_tasks):
        self.company = company
        self.name = name
        self.mail = mail
        self.amount = amount
        self.compl_amount = compl_amount
        self.compl_tasks = compl_tasks
        self.remain_amount = remain_amount
        self.remain_tasks = remain_tasks
        self.make_top()
        # self.create_time = create_time
        self.make_second()
        self.make_total_amount()
        self.make_compl_amount()
        self.make_compl_list()
        self.make_ramain_amount()
        self.make_ramain_list()
        self.make_file()
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

    def save_txt(self):
        my_file = open(self.name + ".txt", "w")
        my_file.write(self.make_file())
        my_file.close()