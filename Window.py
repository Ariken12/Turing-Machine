from tkinter import *
from List import List
from Box import TuringMachine
from re import *


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.box = TuringMachine()
        self.line = Entry(self)
        self.program = Text(self)
        self.output = List(self)
        self.button_execute = Button(self, text='Выполнить', command=self.execute)
        self.button_clear_output = Button(self, text='Очистить вывод', command=self.clear)
        self.line.pack()
        self.button_execute.pack()
        self.button_clear_output.pack()
        self.program.pack()
        self.output.pack()

    # Добавить параметрические переменные
    def execute(self):
        text = self.program.get(0.0, END)
        input_string = self.line.get()
        program = text.split('\n')
        for i in range(len(program)):
            line = program[i]
            if not(fullmatch(
                    r'\s*(\w+)\s+(\w+)\s+(?:(\->)|(\->\.))\s+(\w+)\s+(\w+),?\s+(?:(r)|(l)|(s)|(R)|(L)|(S))\s*',
                    line
                            )):
                self.output.add_item(str(i+1) + ' line: syntax error.')
                return 0
            string = line.split()
            node1 = string[0]
            value1 = string[1]
            if string[2] == '->':
                end = False
            elif string[2] == '->.':
                end = True
            node2 = string[3]
            value2 = string[4]
            if string[5].lower() == 'r':
                shift = 1
            elif string[5].lower() == 'l':
                shift = -1
            elif string[5].lower() == 's':
                shift = 0
            self.box.rules[(node1, value1)] = (node2, value2, shift, end)
        self.box.execution(input_string)

    def clear(self):
        self.output.clear()
