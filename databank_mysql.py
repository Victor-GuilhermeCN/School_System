import pymysql

con = pymysql.connect(db='school', user='root', passwd='')
cursor = con.cursor()


def painel_student():
    print('Welcome to the student painel!'.center(50))
    print('-' * 50)
    print('[1] - Consult students notes\n'
          '[2] - Update your data\n'
          '[3] - Exit')

    def get_option_student():
        try:
            option_student = int(input('Which option: '))
            while option_student > 3:
                print("It's not a valid option!")
                return get_option_student()
        except:
            print('Only numbers are allowed!')
            return get_option_student()
        else:
            if option_student == 1:
                consult_notes_students()
            elif option_student == 2:
                update_student()
            elif option_student == 3:
                while True:
                    print('See you soon!')
                    break


def painel_professor():
    print('Welcome to the professor painel!'.center(50))
    print('-' * 50)
    print('[1] - Insert students notes\n'
          '[2] - Update students notes\n'
          '[3] - Update your data\n'
          '[4] - Exit')

    def get_option_professor():
        try:
            option = int(input('Which option: '))
            while option > 4:
                print("It's not a valid option!")
        except:
            print('Only numbers are allowed!')
            return get_option_professor()
        else:
            if option == 1:
                notes_students()
            elif option == 2:
                notes_students()
            elif option == 3:
                update_professor()
            elif option == 4:
                while True:
                    print('See you soon!')
                    break
    get_option_professor()


def consult():
    sql = 'SELECT * FROM professor'
    cursor.execute(sql)
    con.commit()
    for line in cursor.fetchall():
        print(line)
    con.close()


def register_professor():
    ssn_professor = int(input('Insert your SSN: '))
    name = str(input('Insert your full name: '))
    phone = input('Insert your phone number: ')
    email = str(input('Insert your email: '))
    id_class = input('Insert the article code: ')
    pass_access = str(input('Insert your password: '))
    if len(pass_access) > 18 or len(pass_access) < 6:
        print('Password must be between 6 and 18 characters!')
        return register_professor()

    def confirm_password_professor():
        confirm_pass = str(input('Confirm your password: '))
        if len(confirm_pass) > 18 or len(confirm_pass) < 6:
            print('Password must be between 6 and 18 characters!')
            return confirm_password_professor()
        else:
            if confirm_pass != pass_access:
                print("Passwords are not the same.")
                return confirm_password_professor()
            else:
                cursor.execute("""INSERT INTO professor (ssn_professor, name, pass_access, phone, email, id_class) 
                VALUES (%s, %s, %s, %s, %s, %s)""", (ssn_professor, name, pass_access, phone, email, id_class))
                # Commit the data in the databank
                con.commit()
                print('Professor registered successfully.')
                # Close the connection
                con.close()

    confirm_password_professor()


def update_professor():
    ssn_professor = int(input("What's your SSN: "))
    new_phone = input('Insert the new phone number: ')
    new_email = str(input('Insert your new email: '))
    new_pass_access = str(input('Insert the new Password: '))
    if len(new_pass_access) > 18 or len(new_pass_access) < 6:
        print('Password must be between 6 and 18 characters!')
        return update_professor()

    def confirm_new_password_professor():
        confirm_new_password = input('Confirm your new password: ')
        if len(confirm_new_password) > 18 or len(confirm_new_password) < 6:
            print('Password must be between 6 and 18 characters!')
            return confirm_new_password_professor()
        else:
            cursor.execute("""UPDATE professor SET pass_access = %s, phone = %s, email = %s WHERE ssn_professor = %s""",
                           (new_pass_access, new_phone, new_email, ssn_professor))

    confirm_new_password_professor()
    # Commit the data in the databank
    con.commit()
    print('Update successfully')
    # Close the connection
    con.close()


def delete_professor():
    ssn_professor = int(input("What's your SSN: "))
    cursor.execute('DELETE FROM professor WHERE ssn_professor = %s', (ssn_professor,))
    # Commit the data in the databank
    con.commit()
    print('Delete successfully')
    # Close the connection
    con.close()


def register_student():
    ssn_student = int(input('Insert your SSN: '))
    name = str(input('Insert your name: '))
    phone = input('Insert your phone number: ')
    email = str(input('Insert your email: '))
    id_class = int(input('Insert ID-class: '))
    pass_access = str(input('Insert your password: '))
    if len(pass_access) > 18 or len(pass_access) < 6:
        print('Password must be between 6 and 18 characters!')
        return register_student()

    def confirm_password_student():
        confirm_pass = str(input('Confirm your password: '))
        if len(confirm_pass) > 18 or len(confirm_pass) < 6:
            print('Password must be between 6 and 18 characters!')
            return confirm_password_student()
        else:
            if confirm_pass != pass_access:
                print("Passwords are not the same.")
                return confirm_password_student()
            else:
                print('Student registered successfully')
                cursor.execute(
                    'INSERT INTO student (ssn_student, name, phone, email, pass_access, id_class) VALUES (%s,%s,%s,'
                    '%s,%s,%s)',
                    (ssn_student, name, phone, email, pass_access, id_class))
                cursor.execute("INSERT INTO student_notes (ssn_student, id_class) VALUES (%s, %s)", (ssn_student,
                                                                                                     id_class))
                con.commit()
                con.close()
    confirm_password_student()


def update_student():
    ssn_student = int(input('Insert your SSN: '))
    new_phone = input('Insert your new phone number: ')
    new_email = input('Insert your new email: ')
    new_pass_access = input('Insert your new password: ')
    if len(new_pass_access) > 18 or len(new_pass_access) < 6:
        print('Password must be between 6 and 18 characters!')
        return update_student()

    def confirm_new_password_student():
        confirm_new_pass = input('Confirm your password: ')
        if len(confirm_new_pass) > 18 or len(confirm_new_pass) < 6:
            print('Password must be between 6 and 18 characters!')
            return confirm_new_password_student()
        else:
            if new_pass_access != confirm_new_pass:
                print('Passwords are not the same')
                return confirm_new_password_student()
            else:
                cursor.execute('UPDATE student SET pass_access = %s, phone = %s, email = %s WHERE ssn_student = %s',
                               (new_pass_access, new_phone, new_email, ssn_student))

    confirm_new_password_student()
    print('Update successfully.')
    # Commit the data in the databank
    con.commit()
    # Close the connection
    con.close()


def delete_student():
    ssn_student = int(input('Insert your SSN: '))
    cursor.execute('DELETE FROM student WHERE ssn_student = %s', (ssn_student,))
    print('Student deleted!')
    # Commit the data in the databank
    con.commit()
    # Close the connection
    con.close()


def login_professor():
    list_ssn = []
    list_pass = []
    try:
        ssn_professor = int(input('Insert your SSN: '))
        if type(ssn_professor) != int:
            print('Only numbers are allowed!')
            return login_professor()
        pass_professor = input('Password: ')
    except:
        print('Only numbers are allowed!')
        return login_professor()
    try:
        cursor.execute("""SELECT * FROM professor WHERE ssn_professor = %s """, (ssn_professor,))
    except:
        print('SSN or password is wrong!')
        return login_professor()
    try:
        for r in cursor.fetchall():
            list_ssn.append(r[0])
            list_pass.append(str(r[2]))
        if list_pass[0] == pass_professor:
            print('Access allowed!')
            painel_professor()
        else:
            print('SSN or password is wrong!')
            print('-' * 50)
            return login_professor()
    except:
        print('SSN or password is wrong!')
        print('-' * 50)
        return login_professor()


def login_student():
    list_ssn = []
    list_pass = []
    list_name = []
    try:
        ssn_student = int(input('Insert your SSN: '))
        if type(ssn_student) != int:
            print('Only numbers are allowed!')
            return login_student()
        pass_student = input('Password: ')
    except:
        print('Only number are allowed!')
        return login_student()
    try:
        cursor.execute("""SELECT * FROM student WHERE ssn_student = %s """, (ssn_student,))
    except:
        print('SSN or password is wrong!')
        return login_student()
    try:
        for r in cursor.fetchall():
            list_ssn.append(r[0])
            list_pass.append(str(r[4]))
            list_name.append(str(r[1]))
        if list_pass[0] == pass_student:
            print('Access allowed!')
            painel_student()
        else:
            print('SSN or password is wrong!')
            print('-' * 50)
            return login_student()
    except:
        print('SSN or password is wrong!')
        print('-' * 50)
        return login_student()


def notes_students():
    list_name = []
    try:
        ssn_student = int(input('Insert SSN student: '))
        if type(ssn_student) != int:
            print("Only numbers are allowed!")
            return notes_students()
    except:
        print('Only numbers are allowed!')
        return notes_students()
    else:
        try:
            cursor.execute("SELECT * FROM student WHERE ssn_student = %s", (ssn_student,))
            for i in cursor.fetchall():
                list_name.append(i[1])
                print('-' * 50)
                print(f'Student: {list_name[0]}')
        except:
            print('SSN Student is wrong!')
            return notes_students()
    print('[1] - 1º Quarter\n'
          '[2] - 2º Quarter\n'
          '[3] - 3º Quarter\n'
          '[4] - 4º Quarter\n'
          '[5] - All Quarters\n'
          '[9] - Exit')
    print('-' * 50)

    def choosing_quarter():
        try:
            quarter = str(input('Which quarter: '))
            while quarter not in "123459":
                print("It's not a valid option!")
                return choosing_quarter()
        except:
            print("It's not a valid option!")
            return choosing_quarter()
        else:
            pass
        if quarter == '1':
            def note1():
                try:
                    first_note = float(input('Note 1ª quarter: '))
                    if type(first_note) != float:
                        print('Only numbers are allowed!')
                        return note1()
                except:
                    print('Only numbers are allowed!')
                    return note1()
                else:
                    cursor.execute('UPDATE student_notes SET first_quarter = %s WHERE ssn_student = %s',
                                   (first_note, ssn_student))
                    con.commit()
                    print('Note successfully inserted.')
                    con.close()
            note1()
        elif quarter == '2':
            def note2():
                try:
                    second_note = float(input('Note 2º quarter: '))
                    if type(second_note) != float:
                        print('Only numbers are allowed!')
                        return note2()
                except:
                    print('Only numbers are allowed!')
                    return note2()
                else:
                    cursor.execute('UPDATE student_notes SET second_quarter = %s WHERE ssn_student = %s',
                                   (second_note, ssn_student))
                    con.commit()
                    con.close()
                    print('Note successfully inserted.')
            note2()
        elif quarter == '3':
            def note3():
                try:
                    third_note = float(input('Note 3º quarter: '))
                    if type(third_note) != float:
                        print('Only numbers are allowed!')
                        return note3()
                except:
                    print('Only numbers are allowed!')
                    return note3()
                else:
                    cursor.execute('UPDATE student_notes SET third_quarter = %s WHERE ssn_student = %s',
                                   (third_note, ssn_student))
                    con.commit()
                    con.close()
                    print('Note successfully inserted.')
            note3()
        elif quarter == '4':
            def note4():
                try:
                    fourth_note = float(input('Note 4º quarter: '))
                    if type(fourth_note) != float:
                        print('Only numbers are allowed!')
                        return note4()
                except:
                    print('Only numbers are allowed!')
                    return note4()
                else:
                    cursor.execute('UPDATE student_notes SET fourth_quarter = %s WHERE ssn_student = %s',
                                   (fourth_note, ssn_student))
                    con.commit()
                    con.close()
                    print('Note successfully inserted.')
            note4()
        elif quarter == '5':
            def all_notes():
                try:
                    note_1 = float(input('Note 1º quarter: '))
                    note_2 = float(input('Note 2º quarter: '))
                    note_3 = float(input('Note 3º quarter: '))
                    note_4 = float(input('Note 4º quarter: '))
                    if type(note_1) != float or type(note_2) != float or type(note_3) != float or type(note_4) != float:
                        print('Only numbers are allowed! 1')
                        return all_notes()
                except:
                    print('Only numbers are allowed!')
                    return all_notes()
                else:
                    cursor.execute(
                        "UPDATE student_notes SET first_quarter = %s, second_quarter = %s, third_quarter = %s, "
                        "fourth_quarter = %s WHERE ssn_student = %s", (note_1, note_2, note_3, note_4, ssn_student))
                    con.commit()
                    con.close()
                    print('Notes successfully inserted.')
            all_notes()
        elif quarter == '9':
            while True:
                print('See you soon!')
                break
    choosing_quarter()


def consult_notes_students():
    list_notes = []
    list_name = []
    try:
        ssn_student = int(input('Insert your SSN: '))
        if type(ssn_student) != int:
            print('Only numbers are allowed!')
    except:
        print('Only number are allowed!')
        return consult_notes_students()
    else:
        try:
            cursor.execute('SELECT * FROM student_notes WHERE ssn_student = %s', (ssn_student,))
        except:
            print('Only numbers are allowed!')
            return consult_notes_students()
        else:
            for i in cursor.fetchall():
                list_name.append(i[0])
                list_notes.append(i[1])
                list_notes.append(i[2])
                list_notes.append(i[3])
                list_notes.append(i[4])
            print(f'Notes:\n'
                  f'1º Quarter - {list_notes[0]}\n'
                  f'2º Quarter - {list_notes[1]}\n'
                  f'3º Quarter - {list_notes[2]}\n'
                  f'4º Quarter - {list_notes[3]}')

            def media_school():
                try:
                    media = sum(list_notes)/len(list_notes)
                except:
                    print('No notes were added!')
                else:
                    if media >= 7.0:
                        print(f"It's annual average was {media:.2f}")
                        print('Congratulations, you passed the year!')
                    elif media < 7.0:
                        print(f"It's annual average was {media:.2f}")
                        print("Unfortunately you didn't pass the year")
                    else:
                        pass
            media_school()


# consult_notes_students()
