

from modules.task_list import *
from modules.output import *
from data.task_list import *
from modules.input import * 


# print("Do you want to load some existing tasks?")
# input(y, n)



print("Do you want to load existing tasks?")
answer = input()


if(answer.lower() == "yes"):
    answer == False
    while (answer):
        print_menu()
        answer= option_selector()
    

