from tkinter import *

def delete_entries():
  for field in fields:
    field.delete(0,END)

def UserInput(status,name):
  optionFrame = Frame(root)
  optionLabel = Label(optionFrame)
  optionLabel["text"] = name
  optionLabel.pack(side=LEFT)
  var = StringVar(root)
  var.set(status)
  w = Entry(optionFrame, textvariable= var)
  w.pack(side = LEFT)
  optionFrame.pack()
  return w
  #this return is crucial because if you don't return your widget's identity,
  #you can not use them in another function

if __name__ == '__main__':
  root = Tk()    
  Number = UserInput("1", "Number")
  Name = UserInput("output.txt", "Name")
  Quantity = UserInput("1000", "Quantity")
  
  #you are saying it does not work because of they are strings.
  #then don't assign strings to fields. assign variables.
  fields = Number, Name, Quantity
  #since fields is defined in global scope, you don't need to use it as parameter

  Delete_button = Button(root, text = 'Clear all', command = delete_entries)
  Delete_button.pack()

  root.mainloop()
