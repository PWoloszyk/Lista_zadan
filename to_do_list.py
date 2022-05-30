import os
import time

to_do_list = []


def create_to_do_list():
    toDolist = open("toDoList.txt", "r+")
    for line in toDolist:
        if line == "\n":
            continue
        else:
            line = line.strip("\n")
            to_do_list.append(line)
    toDolist.close()


def create_new_task(new_task):
    toDolist = open("toDoList.txt", "w+")
    to_do_list.append(new_task)
    for x in to_do_list:
        toDolist.write(x + "\n")
    print("zadanie dodane")
    toDolist.close()


def show_to_do_list():
    if len(to_do_list) > 0:
        y = 1
        for x in to_do_list:
            print(str(y) + "." + x)
            y += 1
    else:
        print("brak zadań do wykonania")


def delete_task(indeks):
    to_do_list.pop(indeks)


def clear_window():
    os.system('cls')


def sleep_window(x):
    time.sleep(x)


create_to_do_list()
x = 0.5
while True:
    print()
    print("1.wyświetl liste rzeczy do zrobienia")
    print("2.dodaj rzeczy do zrobienia")
    print("3. usuń z listy")
    user_choice = input("co chcesz zrobić?")
    clear_window()
    sleep_window(x)
    if (user_choice == "1"):
        sleep_window(x)
        show_to_do_list()
    elif(user_choice == "2"):
        sleep_window(x)
        print("wpisz zadanie")
        print()
        new_task = input()
        clear_window()
        create_new_task(new_task)
    elif(user_choice == "3"):
        sleep_window(x)
        show_to_do_list()
        print()
        indeks = input("podaj indeks zadania do usunięcia")
        sleep_window(x)
        clear_window()
        try:
            int(indeks)
        except ValueError:
            print("zła wartość")
            continue
        else:
            indeks = int(indeks) - 1
            delete_task(indeks)
