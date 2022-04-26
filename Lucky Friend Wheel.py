 from tkinter import *
import random

root = Tk()
root.title("Lucky Friend Wheel")
root.geometry("500x500")

list_name_of_freinds = ["aryan", "nate", "manas", "xanelle", "shreya"]
print(list_name_of_freinds)

def random_number():
    random_number = random.randint(0,4)
    print(random_number)
    random_Lucky_friends = list_name_of_freinds[random_number]
    print("Your Lucky name is " + random_Lucky_friends)
    op["text"]=random_Lucky_friends
op = Label(root, bg="blue" ,fg="pink")
op.place(relx=0.5, rely=0.6, anchor=CENTER)  
btn = Button(root, text="Generate Your Lucky freind", command=random_number)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)





root.mainloop()
