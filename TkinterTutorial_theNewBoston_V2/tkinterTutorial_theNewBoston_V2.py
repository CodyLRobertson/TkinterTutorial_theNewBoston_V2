from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame,text="Button 1 (Click ME)", fg= "red")
button2 = Button(topFrame,text="Button 2 (Click ME)", fg= "blue")
button3 = Button(topFrame,text="Button 3 (Click ME)", fg= "green")
button4 = Button(bottomFrame,text="Button 4 (Click ME)", fg= "purple")

button1.pack()
button2.pack()
button3.pack()
button4.pack()

root.mainloop()
  