from college import Human, Student, Group

# students_source =[
#     {
#         'first_name':'Петр',
#         'last_name':'Игнатьев',
#         'patronymic': 'Ильич',
#         'date_birth':'10.09.1998',
#         'gender': 'M'
#     },
#
# ]
#
#
# print( students_source[0])
#
# t_1 = Student(**students_source[0])
# student_1)
#
# t_2 = Student(first_name='Петр', last_name= 'игнатьев',)
# student_2)

# self.first_name = first_name
# self.last_name = last_name
# self.patronymic = patronymic
# self.date_birth = date_birth
# self.gender = gender



# student_1 = Student('Петр', 'Штим', 'Владимирович')
# student_2 = Student('Джейн', 'Путин', 'Анатльевич')
# student_3 = Student('Алеша', 'Рог', 'Папавич')
# student_4 = Student('Дмитрий', 'Иванов', 'Мамович')
# student_5 = Student('Ян', 'Тян', 'Ильич')
# print(student_1)
#
#
# group_1 = Group('33', 'Прикладная информатика 09.02.05')
# group_2 = Group('323', 'Прикладная информатика 09.02.05')
# #print(group_1)
#
#
# #student_1.set_group('33')
# student_1.set_group(group_1)
# student_2.set_group(group_1)
# student_3.set_group(group_2)
# student_4.set_group(group_1)
# student_5.set_group(group_2)

#students = [student_1, student_2, student_3, student_4, student_5]
students_source = open('students.src', 'r', encoding='utf-8').readlines()
students_source = list(map(lambda x: x.replace('\n', '').split(', '), students_source))
#print(students_source)

students_schema = students_source.pop(0)
#rint(students_schema)
#rint(students_source)
students_source_as_dict = list(map(lambda x: dict(zip(students_schema, x)), students_source))
#[print(el) for el in students_source_as_dict]

students = []
for student_dict in students_source_as_dict:
    _student = Student(**student_dict)
    students.append(_student)
[print(el) for el in students]
