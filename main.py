import math
import datetime
import formatValues as FV


ToDo = ["Take out the garbage", "Buy Maurice a tea", "Study Essentials and Python", "Write python program"]
# ToDo = []
TaskNum = 1

# for Task in ToDo:
#     print(f"  {TaskNum}. {Task}")
#     TaskNum += 1


#
# for Task in ToDo:
#     print(f"  {TaskNum}. {Task}")
#     TaskNum += 1
#
# NewTask = input("Enter a new task: ")
# ToDo.append(NewTask)
# DelItem = int(input("What item do you want to delete: "))
# ToDo.__delitem__(DelItem - 1)
# if len(ToDo) != 0:
#     TaskNum = 1
#     for Task in ToDo:
#         print(f"  {TaskNum}. {Task}")
#         TaskNum += 1

# else:
#     print("ToDo list is currently empty")
#
while True:
    NewTask = input("Enter a new task (END to quit): ")
    if NewTask.upper() == "END":
        break
    else:
        ToDo.append(NewTask)
if len(ToDo) != 0:
    TaskNum = 1
    for Task in ToDo:
        print(f"  {TaskNum}. {Task}")
        TaskNum += 1
else:
    print("ToDo list is currently empty")


