import college

class Human:
    def __init__(self, first_name, last_name, patronymic='', date_birth=None, gender=None):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.date_birth = date_birth
        self.gender = gender

    def __str__(self):
        if self.patronymic:
            return f'человек: {self.last_name} {self.first_name[0]}.{self.patronymic[0]}.'
        else:
            return f'человек: {self.last_name} {self.first_name[0]}.'



#human_1 = Human('Иван', 'Иванов', 'Иванович')

#print(human_1)
#print(human_1.first_name)
#print(human_31.last_name)
#print(human_1.patronymic)

#print(f'{human_1.last_name} {human_1.first_name} {human_1.patronymic}')

#human_2 = Human('John', 'Stookton')
#print(human_2)

class Student(Human):
    def set_group(self, group):
        self.group = group
    def __str__(self):
        if self.patronymic:
            return f'студент: {self.last_name} {self.first_name[0]}.{self.patronymic[0]}.'
        else:
            return f'чстудент: {self.last_name} {self.first_name[0]}.'

class Group:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def __str__(self):
        return f'Группа: {self.name} ({self.specialty.split()[-1]}) '



student_1 = Student('Петр', 'Штим', 'Владимирович')
student_2 = Student('Джейн', 'Путин', 'Анатльевич')
student_3 = Student('Алеша', 'Рог', 'Папавич')
student_4 = Student('Дмитрий', 'Иванов', 'Мамович')
student_5 = Student('Ян', 'Тян', 'Ильич')
print(student_1)


group_1 = Group('33', 'Прикладная информатика 09.02.05')
group_2 = Group('323', 'Прикладная информатика 09.02.05')
#print(group_1)


#student_1.set_group('33')
student_1.set_group(group_1)
student_2.set_group(group_1)
student_3.set_group(group_2)
student_4.set_group(group_1)
student_5.set_group(group_2)

students = [student_1, student_2, student_3, student_4, student_5]

#print(student_1.group)

print(f'\nВ мероприятии участвовали:')
for student in students:
    print(f'\t{students} ({student.group})')
