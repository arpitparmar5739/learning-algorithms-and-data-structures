from .queue import test_queue
from .queue_using_2_stacks import test_queue_using_2_stacks

print("Select one option")
print("1. Queue")
print("2. Queue using two stacks")
selected_option = input("Your choice: ")

if selected_option == "1":
    test_queue()
elif selected_option == "2":
    test_queue_using_2_stacks()
