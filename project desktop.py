from tkinter import *

class DecisionModel(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create labels for the decision matrix
        Label(self, text="Decision Matrix").grid(row=0, column=0, columnspan=3)
        Label(self, text="Option 1").grid(row=1, column=0)
        Label(self, text="Option 2").grid(row=1, column=1)
        Label(self, text="Option 3").grid(row=1, column=2)
        Label(self, text="State 1").grid(row=2, column=0)
        Label(self, text="State 2").grid(row=3, column=0)
        Label(self, text="State 3").grid(row=4, column=0)

        # Create entry widgets for the decision matrix
        self.decision_matrix = []
        for i in range(3):
            row = []
            for j in range(3):
                entry = Entry(self)
                entry.grid(row=j+2, column=i)
                row.append(entry)
            self.decision_matrix.append(row)

        # Create buttons to calculate maximin, maximax, and minimax regret
        self.maximin_button = Button(self, text="Maximin", command=self.maximin)
        self.maximin_button.grid(row=2, column=3)
        self.maximax_button = Button(self, text="Maximax", command=self.maximax)
        self.maximax_button.grid(row=3, column=3)
        self.minimax_regret_button = Button(self, text="Minimax Regret", command=self.minimax_regret)
        self.minimax_regret_button.grid(row=4, column=3)

        # Create labels to display the results
        self.maximin_result = Label(self, text="")
        self.maximin_result.grid(row=2, column=4)
        self.maximax_result = Label(self, text="")
        self.maximax_result.grid(row=3, column=4)
        self.minimax_regret_result = Label(self, text="")
        self.minimax_regret_result.grid(row=4, column=4)

    def get_decision_matrix(self):
        matrix = []
        for row in self.decision_matrix:
            matrix.append([int(entry.get()) for entry in row])
        return matrix

    def maximin(self):
        matrix = self.get_decision_matrix()
        result = min([max(row) for row in matrix])
        self.maximin_result.config(text=str(result))

    def maximax(self):
        matrix = self.get_decision_matrix()
        result = max([max(row) for row in matrix])
        self.maximax_result.config(text=str(result))

    def minimax_regret(self):
        matrix = self.get_decision_matrix()
        max_row_values = [max(row) for row in matrix]
        regret_matrix = [[max_row_values[j] - matrix[i][j] for j in range(3)] for i in range(3)]
        result = max([max(row) for row in regret_matrix])
        self.minimax_regret_result.config(text=str(result))

root = Tk()
app = DecisionModel(master=root)
app.mainloop()