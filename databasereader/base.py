discs = [
    # ['id', 'name']
    [101, 'Discrete Math'],
    [102, 'ЭВМ'],
    [103, 'Линейная алгебра'],
    [104, 'Английский язык']
]

groups = [
    # ['id', 'name']
    [201, 'M3100'],
    [202, 'M3102'],
    [203, 'М3105'],
    [204, 'АЯ-16/С1'],
    [205, 'АЯ-132в/В2.2'],
]

students = [ 
    #['id', 'name', 'number_ISU']
    [301, 'Злоделовая Марина', 333333], 
    [302, 'Сазонов Георгин', 333334],
    [303, 'Ухов Илья', 433333],
    [304, 'Струнная Екатерина', 333363],
    [305, 'Котик Андрей', 383333],
    [306, 'Ботт Борис', 333343],
    [307, 'Гениусов Гений', 336333],
]

students_in_groups = [
    # ['group_id', 'student_id']
    [201, 301], # Марина в М3100
    [201, 302], # Георгин в М3100
    [201, 303], # Илья в М3100
    [201, 304], # Екатерина в М3100
    [202, 305], # Андрей в М3102
    [202, 306], # Борис в М3102
    [203, 307], # Гений в М3105
    [204, 302], # Георгин в АЯ-16/С1
    [204, 305], # Андрей в АЯ-16/С1
    [205, 303]  # Илья в АЯ-132в/В2.2
]

teachers = [ 
    # ['id', 'name', 'number_ISU']
    [401, 'Чухарев Константин Игоревич', 666666],
    [402, 'Left Euclidian Function Biective', 000000],
    [403, 'Повыш Повыш Повыш', 555555],
    [404, 'Злоумышь Мария Александровна', 555355],
    [405, 'Блаблабланова Учительница Английскоговна', 555552],
    [406, 'Jack The Carrier', 789012]
]

group_disc = [ 
    # ['id', 'group_id', 'disc_id']
    [501, 201, 101], # Дискретка в М3100
    [502, 201, 102], # ЭВМ в М3100
    [503, 201, 103], # Линал в М3100
    [504, 202, 101], # Дискретка в М3102
    [505, 202, 102], # ЭВМ в М3102
    [506, 202, 103], # Линал в М3102
    [507, 203, 101], # Дискретка в М3105
    [508, 203, 102], # ЭВМ в М3105
    [509, 204, 104], # Англ в АЯ-16/С1
    [5010, 205, 104] # Англ в АЯ-132в/В2.2
]

teacher_gd = [ 
    #['teacher_id', 'group_disc_id']
    [401, 501], # Константин преподаёт Дискретку в М3100
    [401, 504], # Константин преподаёт Дискретку в М3102
    [402, 507], # Function преподаёт Дискретку в М3105
    [403, 502], # Повыш преподаёт ЭВМ в М3100
    [403, 505], # Повыш преподаёт ЭВМ в М3102
    [404, 503], # Мария Александровна преподаёт Линал в М3100
    [404, 506], # Мария Александровна преподаёт Линал в М3012
    [405, 509], # Блаблабланова преподаёт Англ в АЯ-16/С1
    [406, 5010] # Jack The Carrier преподаёт Англ в АЯ-132в/В2.2
]

labs = [ 
    #['id', 'name', 'content']
    [601, 'Homework 3', 'Some sort of content about Fitch-notation.\nС переводом на русский?..'],
    [602, 'Homework 4', 'Binary logic. Sounds breathtaking...'],
    [603, 'Домашняя работа по дискретной математике №1', 'Дам то, что рассказывал лектор, а не что-то своё..'],
    [604, 'Лабка по ЭВМ 1', 'Разберите и соберите аккумулятор..\n'],
    [605, 'Домашка по ЭВМ 1', 'Соберите\n1000\nаккумуляторов..'],
    [606, 'Коллоквиум', 'Ну, что ж, дети. Все задания из д/з!...'],
    [607, 'Домашка 6', 'Посчитайте ФСР для СЛАУ из линейных оболочек из операторов из линейной алгебры...'],
    [608, 'Writing 2', 'What shouldn\'t be improved in your area?\nWrite an essay'],
    [609, 'Homework 4', 'Yep, all tasks from pages 34 til 134...'],
]

lab_gd = [ 
    #['lab_id', 'gd_id', 'is_available', 'deadline']
    [601, 501, 1, '22.11.2021'], # Открыта Homework 3 по Дискретке в М3100
    [601, 504, 1, '22.11.2025'], # Открыта Homework 3 по Дискретке в М3102
    [602, 501, 0, '21.12.2021'], # Закрыта Homework 4 по Дискретке в М3100
    [602, 504, 1, '27.12.2021'], # Открыта Homework 4 по Дискретке в М3102
    [603, 507, 1, '01.12.2031'], # Открыта Домашняя работа по дискретной... по Дискретке в М3105
    [604, 502, 1, '01.01.2022'], # Открыта Лабка по ЭВМ 1 по ЭВМ в М3100 
    [604, 505, 1, '29.12.2021'], # Открыта Лабка по ЭВМ 1 по ЭВМ в М3102
    [605, 502, 0, '01.02.2022'], # Закрыта Домашка по ЭВМ 1 по ЭВМ в М3100
    [606, 505, 1, '29.11.2021'], # Открыта Домашка по ЭВМ 1 по ЭВМ в М3102
    [607, 506, 1, '29.11.2021'], # Открыта Домашка 6 по Линалу в М3012
    [606, 503, 0, '22.12.2021'], # Закрыт Коллоквиум по Линалу в М3100
    [606, 506, 0, '22.12.2021'], # Закрыт Коллоквиум по Линалу в М3102
    [608, 509, 1, '21.12.2021'], # Открыт Writing 2 по Англу в АЯ-16/С1
    [609, 509, 1, '21.12.2021']  # Открыта Homework 4 по Англу в АЯ-16/С1
]

del_labs = [ 
    #['id', 'student_id', 'content', 'mark', 'comm', 'date']
    [701, 301, 'Лень придумывать 1', '5', 'No SQRT', '01.11.2021'],
    [702, 301, 'Лень придумывать 2', '10', '', '01.11.2021'],
    [703, 302, 'Лень придумывать 3', '4.3', 'С sqrt исправлением', '01.11.2021'],
    [704, 302, 'Лень придумывать 4', '9', '', '01.11.2021'],
    [705, 302, 'Лень придумывать 5', '10', '', '01.11.2021'],
    [706, 302, 'Лень придумывать 6', '8', '', '01.11.2021'],
    [707, 305, 'Лень придумывать 7', '10', '', '01.11.2021'],
    [708, 305, 'Лень придумывать 8', '', '', '01.11.2021'],
    [709, 306, 'Лень придумывать 9', '', '', '01.11.2021'],
]

lab_del_lab = [
    #['del_lab_id', 'lab_id']
    [701, 601],
    [702, 604],
    [703, 601],
    [704, 604],
    [705, 604],
    [706, 608],
    [707, 604],
    [708, 606],
    [709, 607]
]
