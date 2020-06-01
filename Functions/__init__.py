from databank_mysql import *


def line():
    print('-' * 50)


def title(msg):
    line()
    print(msg.center(50))
    line()


def introduction(msg):
    print(msg.center(50))


def continuous():
    try:
        opt = str(input('Do you want to continue? [Y/N]:')).upper().strip()[0]
    except Exception:
        print('Insert only Y or N!')
        return line(), continuous()
    else:
        if opt == 'Y':
            pass
        elif opt == 'N':
            while True:
                print('See you soon!')
                break


def painel_menu():
    title('MENU')
    print('[1] - Login\n'
          '[2] - Register\n'
          '[3] - Exit')
    line()


def option_choosed():
    try:
        option = int(input('Which option: '))
        if type(option) != int or option > 3:
            print("It's not a valid option!")
            return line(), option_choosed()
    except:
        print("It's not a valid option!")
        return line(), option_choosed()
    else:
        if option == 1:
            def prof_student_login():
                try:
                    prof_student = str(input("You're a professor or student? [P/S]: ")).upper().strip()[0]
                    if prof_student not in "PS":
                        print("It's not a valid option!")
                        return prof_student_login()
                except:
                    print("It's not a valid option!")
                    return prof_student_login()
                else:
                    if prof_student == 'P':
                        login_professor()
                    elif prof_student == 'S':
                        login_student()
            prof_student_login()
        elif option == 2:
            def prof_student_register():
                try:
                    prof_or_student = str(input("You're a professor or student? [P/S]: ")).upper().strip()[0]
                    if prof_or_student not in "PS":
                        print("It's not a valid option!")
                        return prof_student_register()
                except:
                    print("It's no a valid option!")
                    return prof_student_register()
                else:
                    if prof_or_student == 'P':
                        register_professor()
                    elif prof_or_student == 'S':
                        register_student()
            prof_student_register()
        elif option == 3:
            while True:
                print('See you soon!')
                break
