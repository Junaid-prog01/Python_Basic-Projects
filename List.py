



list = []

while True :
    print('=' * 40)
    print("this is TO-DO list choose what tou want to do")
    print("1 - Add task in your list")
    print("2 - Remove task from your list")
    print("3 - Exit")
    task_opration = int(input("Enter opration number; "))
    if task_opration == 1 :
        tasks = str(input("Enter Task name; "))
        list.append(tasks)
    elif task_opration == 2 :
        tasks = str(input("Enter Task name; "))
        list.remove(tasks)
    elif task_opration == 3 :
        break
    else :
        print("Enter valid opration")

print(list)










# while True :
#     list = []
#     tasks_number = int(input("Enter opration; "))
#     task_name = input("Enter task name; ")
#     if tasks_number == 1 :
#         print(update_tasks())
#         print(list)
#     if tasks_number == 3 :
#         print("over")
#         break


# def main():
#     print("Hello or something ")

# def add_task(task, list):
#     print(list.append(task))

# def remove_task(task, list):
#     print(list.remove(task))

# for task in tasks :
#     if tasks == 1:
#         print(add_task())
# print(list)

