

# # text box
# text = tkinter.Text(height=5,width=10)
# # puts the cursor in textbox
# text.focus()
# # add some text to begin with 
# text.insert(tkinter.END,"Example of multi line text entry")
# text.pack()

# # spinbox
# def spinbox_used():
#     # gets the current value in spinbox
#     print(spinbox.get())

# spinbox = tkinter.Spinbox(from_=0,to=10,width=5,command=spinbox_used)
# spinbox.pack()

# # scale
# def scale_used(value):
#     print(value)

# scale = tkinter.Scale(from_=0,to=100,command=scale_used)
# scale.pack()


# # checkbox
# def checkbutton_used():
#     # prints 1 if on button otherwise 0
#     print(checked_state.get())
    
# # variable to hold the state
# checked_state = tkinter.IntVar()
# checkbutton = tkinter.Checkbutton(text="is on ?",variable=checked_state,command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()


# # radiobuttons
# def radio_used():
#     print(radio_state.get())
    
# radio_state = tkinter.IntVar()
# radiobutton1 = tkinter.Radiobutton(text="option1",value=1,variable=radio_state,command=radio_used)
# radiobutton2 = tkinter.Radiobutton(text="option2",value=2,variable=radio_state,command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()


# # listbox
# def listbox_used(event):
#     print(listbox.get(listbox.curselection()))
    
# listbox = tkinter.Listbox(height=4)
# fruits = ["apple","pear","orange","banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item),item)
    
# listbox.bind("<<ListboxSelect>>",listbox_used)
# listbox.pack()


# # keep the window open
# window.mainloop()


# # # tkinter
# # import tkinter
# # # object
# # window = tkinter.Tk()
# # window.title("My First GUI Program")
# # window.minsize(width= 500,height=300)

# # # label
# # my_label = tkinter.Label(text="I am a label",font=("Arial",24,"bold")) 
# # my_label.pack()

# # # ways to change the arg or update the properties of the component 
# # # my_label["text"] = "New Text"
# # # my_label.config(text="new text")

# # # button
# # def button_clicked():
# #     # get() -> return the input string
# #     new_text = input.get()
# #     my_label.config(text=new_text)



# # my_button = tkinter.Button(text="Click me",command=button_clicked)
# # my_button.pack()


# # # entry

# # input = tkinter.Entry(width=10)
# # input.pack()


# # # keep the window open
# # window.mainloop()