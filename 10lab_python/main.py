import csv

class Student:
    def __init__(self, first_name, last_name, middle_name, course, field, subject, semester):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.course = course
        self.field = field
        self.subject = subject
        self.semester = semester

    def get_course(self):
        return self.course

    def print_data(self):
        print("\nФамилия: {}\nИмя: {}\nОтчество: {}\nКурс: {}\nГруппа: {}\nПредмет: {}\nСеместр: {}"
              .format(self.last_name, self.first_name, self.middle_name, self.course, self.field, self.subject, self.semester))


class ModuleMark(Student):
    def __init__(self, first_name, last_name, middle_name, course, field, subject, semester, mark):
        super().__init__(first_name, last_name, middle_name, course, field, subject, semester)
        self.mark = mark

    def print_data(self):
        super().print_data()
        print("Оценка: {}".format(self.mark))


class CourseworkMark(Student):
    def __init__(self, first_name, last_name, middle_name, course, field, subject, semester, coursework_title, mark):
        super().__init__(first_name, last_name, middle_name, course, field, subject, semester)
        self.coursework_title = coursework_title
        self.mark = mark

    def print_data(self):
        super().print_data()
        print("Курсовая работа: {}\nОценка за курсовую работу: {}".format(self.coursework_title, self.mark))


def read_module_marks_from_file(file_name):
    module_marks = []
    with open(file_name, newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if len(row) == 8:
                first_name, last_name, middle_name, course, field, subject, semester, mark = row
                module_marks.append(ModuleMark(first_name, last_name, middle_name, int(course), field, subject, int(semester), int(mark)))
    return module_marks


def read_coursework_marks_from_file(file_name):
    coursework_marks = []
    with open(file_name, newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if len(row) == 9:
                first_name, last_name, middle_name, course, field, subject, semester, coursework_title, mark = row
                coursework_marks.append(CourseworkMark(first_name, last_name, middle_name, int(course), field, subject, int(semester), coursework_title, int(mark)))
    return coursework_marks


def print_marks_for_course(course_num, module_marks, coursework_marks):
    for module_mark in module_marks:
        if module_mark.get_course() == course_num:
            module_mark.print_data()

    for coursework_mark in coursework_marks:
        if coursework_mark.get_course() == course_num:
            coursework_mark.print_data()                                                   

def main():
    module_marks = read_module_marks_from_file("module_marks.txt")
    coursework_marks = read_coursework_marks_from_file("coursework_marks.txt")
    num = int(input("Введите курс: "))
    print_marks_for_course(num, module_marks, coursework_marks)


if __name__ == '__main__':
    main()

#module_marks.txt:

#Иван	Иванов	Иванович	1	Группа1	Математика  1   4
#Петр	Петров	Петрович	1	Группа1	Математика  2   5
#Сидор	Сидоров	Сидорович	2	Группа2	Физика	1	3
#Иван	Иванов	Иванович	1	Группа1	Математика	1	4
#Петр	Петров	Петрович	1	Группа1	Математика	1	5
#Сидор	Сидоров	Сидорович	2	Группа2	Физика	1	3
#Иван	Иванов	Иванович	1	Группа1	Математика	1	4
#Петр	Петров	Петрович	1	Группа1	Математика	1	5
#Сидор	Сидоров	Сидорович	2	Группа2	Физика	1	3

#coursework_marks.txt
#Иван	Иванов	Иванович	1	Группа1	Математика	1	"Курсовая работа 1"	4
#Петр	Петров	Петрович	1	Группа1	Математика	1	"Курсовая работа 2"	5
#Сидор	Сидоров	Сидорович	2	Группа2	Физика	1	"Курсовая работа 3"	3
#Иван	Иванов	Иванович	1	Группа1	Математика	1	"Курсовая работа 1"	4
#Петр	Петров	Петрович	1	Группа1	Математика	1	"Курсовая работа 2"	5
#Сидор	Сидоров	Сидорович	2	Группа2	Физика	1	"Курсовая работа 3"	3
#Иван	Иванов	Иванович	1	Группа1	Математика	1	"Курсовая работа 1"	4
#Петр	Петров	Петрович	1	Группа1	Математика	1	"Курсовая работа 2"	5
#Сидор	Сидоров	Сидорович	2	Группа2	Физика	1	"Курсовая работа 3"	3
