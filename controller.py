import venw

main_dict = {}
student_name = []
lesson = []
def start():
    while True:
        op = venw.get_op()
        if op == 1:
            student = venw.input_student()
            main_dict[student] = {}
            student_name.append(student)
            if lesson:
                for less in lesson:
                    main_dict[student][less] = []

        if op == 2:
            less = venw.input_less()
            lesson.append(less)
            for name in student_name:
                main_dict[name][less] = []

        if op == 3:
            name, less, mark = venw.input_mark()
            main_dict[name][less].append(mark)

        if op == 4:
            print(main_dict)

        if op == 5:
            name = venw.get_name_to_show()
            print(main_dict[name])

        if op == 6:
            break

