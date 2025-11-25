from operator import itemgetter
import math
import datetime as d
from collections import Counter
import statistics as s

print("Welcome to the student portal! Choose a login method to continue.\n")
print("Login Time:", d.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

l = []

def Portal():
    while True:
        print("\n<--------------------LOGIN PAGE-------------------->")
        print ('Press 1 to login as Management')
        print ('Press 2 to login as Teacher')
        print ('Press 3 to login as Student')
        print ('Press 4 to login as Parent')
        print ('Press 5 to exit the portal')
        n = input('Enter the choice: ')

        if n == "1":
            management()
        elif n == "2":
            teacher()
        elif n == "3":
            student()
        elif n == "4":
            parent()
        elif n == "5":
            print ('Exiting the portal . . . . .')
            break
        else:
            print('Invalid input, please try again!')


def management():
    print("\n<--------------------LOGGED IN AS MANAGEMENT-------------------->")
    while True:
        print ()
        print ('Press 1 to add student records')
        print ('Press 2 to delete student records')
        print ('Press 3 to view student records')
        print ('Press 4 to logout')
        n = input('Enter the choice: ')

        if n == '1':
            print('Adding student record: \n')
            manage_add()
        elif n == '2':
            print('Deleting student record: \n')
            manage_delete()
        elif n == '3':
            print('Viewing student records: \n')
            manage_view()
        elif n == '4':
            print('Logging out . . . . . . .\n\n')
            break
        else:
            print('Invalid input, please try again.')

def manage_add():
    while True:
        try:
            roll = int(input('Enter roll: '))
        except ValueError:
            print ('Invalid input')
            continue
        x = False
        for j in l:
            if j[0] == roll:
                x = True
                break
        if x:
            print('Roll number already exists, Please enter a unique one')
        else:
            break
    name = input('Enter name: ')
    while True:
        try:
            age = int(input('Enter age: '))
            break
        except ValueError:
                print ('Invalid input')
                continue

    while True:
        print('Select branch:')
        print('Press 1 for CSE')
        print('Press 2 for AIML')
        print('Press 3 for Mechanical Engineering')
        print('Press 4 for ECE')
        m = input('Enter choice: ')

        if m == '1':
            branch = 'CSE'
            break
        elif m == '2':
            branch = 'AIML'
            break
        elif m == '3':
            branch = 'Mechanical Engineering'
            break
        elif m == '4':
            branch = 'ECE'
            break
        else:
            print('Invalid choice')

    l.append([roll, name, age, branch, {}, "","","",""])
    print(f'Student {name} added successfully in {branch} branch')

def manage_delete():
    while True:
        try:
            roll = int(input('Enter roll number of student whose record to delete: '))
            break
        except ValueError:
                print ('Invalid input')
                continue
    for n in l:
        if n[0] == roll:
            l.remove(n)
            print(f'Student with roll number {roll} deleted successfully')
            break
    else:
        print('Student record not found')


def manage_view():
    while True:
        try:
            roll = int(input('Enter roll number of student whose record to view: '))
            break
        except ValueError:
                print ('Invalid input')
                continue
    for n in l:
        if n[0] == roll:
            print('Roll number of student:', n[0])
            print('Name of student:', n[1])
            print('Age of student:', n[2])
            print('Branch of student:', n[3])
            break
    else:
        print('Student record not found')

def teacher():
    print('\n<--------------------LOGGED IN AS TEACHER-------------------->')
    while True:
        print()
        print('Press 1 to add student marks')
        print('Press 2 to delete student marks')
        print('Press 3 to view student records and marks')
        print('Press 4 to add message for parents')
        print('Press 5 to add message for students')
        print('Press 6 to view message from parents')
        print('Press 7 to view message from students')
        print('Press 8 to view student rankings by marks')
        print('Press 9 to view class statistics')
        print('Press 10 to logout')

        n = input('Enter the choice: ')

        if n == '1':
            print('Adding student marks:\n')
            teacher_add()
        elif n == '2':
            print('Deleting student marks:\n')
            teacher_delete()
        elif n == '3':
            print('Viewing student records and marks:\n')
            teacher_view()
        elif n == '4':
            print('Adding message for parents:\n')
            teachermsg_parent()
        elif n == '5':
            print('Adding message for students:\n')
            teachermsg_student()
        elif n == '6':
            print('Viewing messages from parents:\n')
            viewmsg_parent()
        elif n == '7':
            print('Viewing messages from students:\n')
            viewmsg_student()
        elif n == '8':
            print('Viewing student rankings:\n')
            rankings()
        elif n == '9':
            print('Viewing class statistics:\n')
            statistics()
        elif n == '10':
            print('Logging out . . . . . . .\n\n')
            break
        else:
            print('Invalid input, please try again')


def teacher_add():
    while True:
        try:
            roll = int(input('Enter roll number to add marks: '))
            break
        except ValueError:
                print ('Invalid input')
                continue
    for n in l:
        if n[0]==roll:
            branch=n[3]
            mandatory=['Programming Basics', 'Electric Circuits And Systems', 'Communication Skills', 'Human Values', 'Calculus']
            if branch=='CSE':
                subject='Advanced Programming'
            elif branch=='ECE':
                subject='Advanced Electrical Circuits'
            elif branch=='Mechanical Engineering':
                subject='Engineering Mechanics'
            elif branch=='AIML':
                subject='Fundamentals of AIML'
            print('Enter marks:')
            for k in mandatory:
                while True:
                    try:
                        m1=int(input(f'{k}: '))
                        if 0<= m1<= 100:
                            n[4][k]=m1
                            break
                        else:
                            print('Marks should be between 0 and 100')
                    except ValueError:
                        print('Invalid input')
            while True:
                try:
                    m2 = int(input(f'{subject}: '))
                    if 0<=m2<=100:
                        n[4][subject]=m2
                        break
                    else:
                        print('Marks should be between 0 and 100')
                except ValueError:
                    print('Invalid input')
            print(f'Marks added for student roll {roll}')
            break
    else:
        print('Student record not found')

def teacher_delete():
    while True:
        try:
            roll = int(input('Enter roll number to delete marks: '))
            break
        except ValueError:
                print ('Invalid input')
                continue
    for n in l:
        if n[0] == roll:
            subject = input('Enter subject name to delete marks: ').title()
            if subject in n[4]:
                del n[4][subject]
                print(f'Marks deleted for {subject} in roll {roll}')
            else:
                print(f'No marks found for subject {subject}')
            break
    else:
        print('Student record not found')

def teacher_view():
    while True:
        try:
            roll = int(input('Enter roll number to view records and marks: '))
            break
        except ValueError:
            print('Invalid input')
            continue
    for n in l:
        if n[0] == roll:
            print('Roll:', n[0])
            print('Name:', n[1])
            print('Age:', n[2])
            print('Branch:', n[3])
            print('Marks:')
            if n[4]:
                x = list(n[4].values())
                for sub, marks in n[4].items():
                    print(f'{sub}: {marks}')
                t = math.fsum(x)
                avg = t / len(x)
                print('Total Marks: ',t)
                print(f'Average Marks: {avg:.2f}')
            else:
                print('No marks entered')
            break
    else:
        print('Student record not found')

def teachermsg_parent():
    while True:
        try:
            roll = int(input('Enter roll number to add message for parent: '))
            break
        except ValueError:
                print ('Invalid input')
                continue
    for n in l:
        if n[0] == roll:
            msg = input('Enter message for parent: ')
            n[5] = msg
            print('Message added for parent')
            break
    else:
        print('Student record not found')

def teachermsg_student():
    while True:
        try:
            roll = int(input('Enter roll number to add message for student: '))
            break
        except ValueError:
                print ('Invalid input')
                continue
    for n in l:
        if n[0] == roll:
            msg = input('Enter message for student: ')
            n[6] = msg
            print('Message added for student')
            break
    else:
        print('Student record not found')

def viewmsg_parent():
    while True:
        try:
            roll=int(input('Enter roll number to view messages from parents: '))
            break
        except ValueError:
                print ('Invalid input')
                continue
    for n in l:
        if n[0]==roll:
            if n[7]:
                print(f'Message from parent: {n[7]}')
                break
            else:
                print('No message from parent')
    else:
        print('Student record not found')

def viewmsg_student():
    while True:
        try:
            roll=int(input('Enter roll number to view messages from students: '))
            break
        except ValueError:
                print ('Invalid input')
                continue
    for n in l:
        if n[0]==roll:
            if n[8]:
                print(f'Message from student: {n[8]}')
                break
            else:
                print('No message from students')
    else:
        print('Student record not found')

def rankings():
    branchno = Counter(n[3] for n in l)
    print('Student count per branch:')
    for branch, c in branchno.items():
        print(branch,':',c)
    print()

    print('Student Rankings:\n')
    r = []
    for n in l:
        roll = n[0]
        name = n[1]
        marks = n[4]
        if marks and all(marks.values()):
            total = sum(marks.values())
            r.append((roll, name, total))
    r.sort(key=itemgetter(2), reverse=True)
    print("%-6s %-8s %-20s %-6s" % ("Rank", "Roll", "Name", "Total Marks"))
    print("-" * 50)
    rank = 1
    for roll, name, total in r:
        print('%-6s %-8s %-20s %-6s' % (rank, roll, name, total))
        rank += 1
    if not r:
        print('No students with complete marks')

def statistics():
    t = []
    for n in l:
        m = n[4]
        if m and all(m.values()):
            t.append(sum(m.values()))
    if not t:
        print('No students with complete marks')
        return
    mean = s.mean(t)
    median = s.median(t)
    try:
        mode = s.mode(t)
    except s.StatisticsError:
        mode = 'No unique mode'
    print('\nClass Statistics :')
    print(f'Mean (Average): {mean:.2f}')
    print('Median: ',median)
    print('Mode: ',mode)
    
def student():
    print('\n<--------------------LOGGED IN AS STUDENT-------------------->')
    while True:
        print()
        print('Press 1 to view your records')
        print('Press 2 to view your marks')
        print('Press 3 to send a message to your teachers')
        print('Press 4 to view a message from your teachers')
        print('Press 5 to logout')
        n = input('Enter the choice: ')

        if n == '1':
            print('Viewing your records:\n')
            view_record()
        elif n == '2':
            print('Viewing your marks:\n')
            view_marks()
        elif n == '3':
            print('Sending message to teachers:\n')
            messageteach()
        elif n == '4':
            print('Viewing message from teachers:\n')
            viewmessageteach()
        elif n == '5':
            print('Logging out . . . . . . .\n\n')
            break
        else:
            print('Invalid input, please try again')
            
def view_record():
    while True:
        try:
            roll = int(input('Enter your roll number: '))
            break
        except ValueError:
                print ('Invalid input')
                continue
    for n in l:
        if n[0] == roll:
            print(f'Roll: {n[0]}')
            print(f'Name: {n[1]}')
            print(f'Age: {n[2]}')
            print(f'Branch: {n[3]}')
            break
    else:
        print('Record not found')

def view_marks():
    while True:
        try:
            roll = int(input('Enter your roll number: '))
            break
        except ValueError:
            print('Invalid input')
            continue
    for n in l:
        if n[0] == roll:
            if n[4]:
                print('Marks:')
                x = list(n[4].values())
                for subject, marks in n[4].items():
                    print(f'{subject}: {marks}')
                t = math.fsum(x)
                avg = t / len(x)
                print(f'Total Marks: {t}')  
                print(f'Average Marks: {avg:.2f}')
            else:
                print('No marks found')
            break
    else:
        print('Record not found')


def viewmessageteach():
    while True:
        try:
            roll = int(input('Enter your roll number to view message from teachers: '))
            break
        except ValueError:
                print ('Invalid input')
                continue
    for n in l:
        if n[0] == roll:
            if n[6]:
                print(f'Message from teachers: {n[6]}')
            else:
                print('No messages from teachers')
            break
    else:
        print('Record not found')

def messageteach():
    while True:
        try:
            roll = int(input('Enter your roll number to send a message: '))
            break
        except ValueError:
                print ('Invalid input')
                continue
    for n in l:
        if n[0] == roll:
            msg = input('Enter your message: ')
            n[8] = msg
            print('Message sent to teachers')
            break
    else:
        print('Record not found')


def parent():
    print('\n<--------------------LOGGED IN AS PARENT-------------------->')
    while True:
        print()
        print('Press 1 to view records')
        print('Press 2 to view marks')
        print('Press 3 to send a message to teachers')
        print('Press 4 to view a message from teachers')
        print('Press 5 to logout')
        n = input('Enter the choice: ')

        if n == '1':
            print('Viewing records:\n')
            parentview_record()
        elif n == '2':
            print('Viewing marks:\n')
            parentview_marks()
        elif n == '3':
            print('Sending message to teachers:\n')
            parentmessageteach()
        elif n == '4':
            print('Viewing message from teachers:\n')
            parentviewmessageteach()
        elif n == '5':
            print('Logging out . . . . . . .\n\n')
            break
        else:
            print('Invalid input, please try again')

def parentview_record():
    roll = input('Enter your child\'s roll number to view records: ')
    for n in l:
        if str(n[0]) == roll:
            print(f'Roll: {n[0]}')
            print(f'Name: {n[1]}')
            print(f'Age: {n[2]}')
            print(f'Branch: {n[3]}')
            break
    else:
        print('Record not found')

def parentview_marks():
    roll = input("Enter your child's roll number to view marks: ")
    for n in l:
        if str(n[0]) == roll:
            if n[4]:
                print('Marks:')
                x = list(n[4].values())
                for sub, marks in n[4].items():
                    print(f'{sub}: {marks}')
                t = math.fsum(x)
                avg = t / len(x)
                print('Total Marks: ',t)
                print(f'Average Marks :[avg:.2f]')
            else:
                print('No marks found')
            break
    else:
        print('Record not found')

def parentmessageteach():
    roll = input('Enter your child\'s roll number to send message to teachers: ')
    for n in l:
        if str(n[0]) == roll:
            msg = input('Enter your message to teachers: ')
            n[7] = msg
            print('Message sent to teachers')
            break
    else:
        print('Record not found')

def parentviewmessageteach():
    roll = input('Enter your child\'s roll number to view messages from teachers: ')
    for n in l:
        if str(n[0]) == roll:
            if n[5]:
                print('Message from teachers:',n[5])
            else:
                print('No messages from teachers')
            break
    else:
        print('Record not found')

Portal()




