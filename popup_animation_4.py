import tkinter
from PIL import Image,ImageTk,ImageSequence

class App4:
    def __init__(self,parent):
        self.parent=parent
        self.canvas=tkinter.Canvas(parent,width=500,height=280,highlightbackground='black',highlightthickness=2,bg='white',borderwidth=0)
        self.canvas.pack()
        self.sequence=[ImageTk.PhotoImage(img)
                           for img in ImageSequence.Iterator(
                               Image.open(r"loading5.gif"))]
        self.image=self.canvas.create_image(250,80,image=self.sequence[0])
        self.x=7
        self.animate(1)


    def animate(self,counter):
        
        if(self.x<160):
            self.canvas.itemconfig(self.image,image=self.sequence[counter])
            self.parent.after(12,lambda:self.animate((counter+1) %len(self.sequence)))
        
        self.x+=1

    def __del__(self):
        print("destructor called")
        self.parent.destroy()

   
        

##root=tkinter.Tk()
##app=App4(root)
##del app
##root.mainloop()


        
