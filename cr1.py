
from tkinter import *
class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do-list')
        self.root.geometry('650x410+300+150')

       
        self.label = Label(self.root, text='To-do-list-App', font='ariel, 25 bold', width=10, bd=5, bg='orange', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add task', font='ariel, 20 bold', width=10, bd=5, bg='orange', fg='black')
        self.label2.place(x=20, y=54)

        self.label3 = Label(self.root, text='Tasks', font='ariel, 20 bold', width=10, bd=5, bg='orange', fg='black')
        self.label3.place(x=345, y=54)

        self.tasks_listbox = Listbox(self.root, height=9, bd=5, width=22, font='ariel, 20 italic bold')
        self.tasks_listbox.place(x=270, y=100)

        self.text_entry = Text(self.root, height=2, bd=4, width=18, font='ariel, 16 bold')
        self.text_entry.place(x=20, y=120)

        def add():
            content = self.text_entry.get(1.0, END)
            self.tasks_listbox.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content)
            self.text_entry.delete(1.0, END)

        def delete():
            delete_ = self.tasks_listbox.curselection()
            look = self.tasks_listbox.get(delete_)
            with open('data.txt', 'r+') as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.tasks_listbox.delete(delete_)

        with open('data.txt', 'r') as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.tasks_listbox.insert(END, ready)

        self.button = Button(self.root, text="add", bd=5, width=16, font='ariel, 16 bold', command=add)
        self.button.place(x=20, y=200)

        self.button2 = Button(self.root, text="delete", bd=5, width=16, font='ariel, 16 bold', command=delete)
        self.button2.place(x=20, y=270)

def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()


