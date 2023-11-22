import tkinter as tk


class App:
    def __init__(self):
        self.root= tk.Tk()
        self.window()
        self.interface()
    def window(self):
        self.root.title("Dicionário")
        self.root.geometry("560x640")

    def interface(self):
        self.root.configure(bg="#3f3f3f")
        titulo = tk.Label(self.root,
                            text="A frase do dia é:",
                            font=("Arial",23,"bold"))
        titulo.pack(pady=10)


if __name__ == "__main__":
    start = App()
    start.root.mainloop()