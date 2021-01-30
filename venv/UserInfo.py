class UserInfo:
    def __init__(self):
        self.company = company
        self.name = name
        self.mail = mail
        self.time = time
        self.amount = amount
        self.compl_amount = compl_amount
        self.compl_tasks = compl_tasks
        self.remain_amount = remain_amount
        self.remain_tasks = remain_tasks
        self.make_top()
        self.make_second()
        self.make_total_amount()
        self.make_compl_amount()
        self.make_compl_list
        self.make_ramain_amount
        self.make_ramain_list()
        self.make_file()
        self.save_txt()

    def make_top(self):
        first_string = "Отчет" + ' ' + company + '.' + '\n'
        return first_string

    def make_second(self):
        today = datetime.datetime.today()
        proper_format_today = today.strftime("%d.%m.%Y %H:%M")
        second_string = name + ' ' + '<' + mail + '>' + proper_format_today + '\n'
        return second_string

    def make_total_amount(self):
        total_amount = "Всего задач: " + amount + '\n\n'
        return total_amount

    def make_compl_amount(self):
        compl_amount_str = "Завершенные задачи: " + '(' + compl_amount  + '):' + '\n'
        return compl_amount_str

    def make_compl_list(self):
        compl_tasks_list = ('\n'.join(compl_tasks))
        return compl_tasks_list

    def make_ramain_amount(self):
        remain_amount_str = "Оставшиеся задачи: " + '(' + remain_amount + '):' + '\n'
        return remain_amount_str

    def make_ramain_list(self):
        remain_tasks_list = ('\n'.join(remain_tasks))
        return remain_tasks_list

    def make_file(self):
        filed_file = make_top() + make_second() + make_total_amount() + make_compl_amount() + make_compl_list() + make_ramain_amount() + make_ramain_list()

    def save_txt(self):
        my_file = open(name + ".txt", "w")
        my_file.write(make_file())
        my_file.close()