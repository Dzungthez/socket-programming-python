import tkinter as tk


class Root(tk.Tk):
    def __init__(self, tasks = None):
        super().__init__()
        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks
        self.label = tk.Label(self, text='Hello', padx=15, pady=5)

        self.title('My app v1.0')
        self.geometry('300x400')

        todo1 = tk.Label(self, text = '__Add items here__', bg = 'lightgrey',
                        fg = 'black', pady = 10)
        self.tasks.append(todo1)
        self.label.pack()


if __name__ == '__main__':
    root = Root()
    root.mainloop()
