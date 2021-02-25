from tkinter import *
from tkinter import filedialog as fd


class List(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.list = Listbox(self, selectmode=EXTENDED)
        self.scroll = Scrollbar(command=self.list.yview)
        self.list.config(yscrollcommand=self.scroll.set)
        self.list.grid(row=0, column=0, rowspan=4, sticky=N+S+W+E)

    def add_item(self, text):
        self.list.insert(0, text)

    def delete_item(self):
        select = list(self.list.curselection())
        select.reverse()
        for i in select:
            self.list.delete(i)

    def clear(self):
        for i in range(len(self.list.get(0, END))):
            self.list.delete(i)


