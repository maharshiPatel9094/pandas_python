import tkinter

# event listners
def button_click():
    print("I got clicked")


def new_button_clicked():
    print("I am a new button")

# creating a new window and configurations
window = tkinter.Tk()
window.title("Widget Window")
window.minsize(width=500,height=500)

# labels
my_label = tkinter.Label(text="I am a old label")
my_label.config(text="I am a new label")
# my_label["text"] = "I am a new label"
# my_label.pack()
my_label.grid(column=1,row=1)

# buttons
# handel some events by button click
my_button = tkinter.Button(text="click me",command=button_click)
# my_button.pack()
my_button.grid(column=2,row=2)


new_button = tkinter.Button(text="new_button",command=new_button_clicked)
new_button.grid(column=3,row=1)



# entries
entry = tkinter.Entry(width=30)
# entry box will display with inb uilt text written for u
entry.insert(tkinter.END,string="some text to begin with")
# return the input string
print(entry.get())
# entry.pack()
entry.grid(column=4,row=3)



# class Car:
#     def __init__ (self,**kwargs):
#         self.make = kwargs["make"]
#         self.model = kwargs["model"]


# my_car = Car(make="Nissan",model="gtr")
# # print(my_car.model)
# # print(my_car.make)
# print(my_car["model"])
# print(my_car["make"])


# def calculate(n,**kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)

# calculate(2,add=3,multiply=5)



# # total = 0
# # def add(*args):
# #     global total
# #     for n in args:
# #         total+=n


# # add(2,3,4,1)
# # print(total)