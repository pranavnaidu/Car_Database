from tkinter import *
from Functions1 import Car

class Table:

    def __init__(self, main):
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(main, width=20, fg='black', font=('Arial', 10))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

#empty list for customers
lst = []
x = Car  # instantiation of class

with open("text.txt") as f:
    for line in f:
        currentline = line.split(',')
        name = str(currentline[0])
        car = str(currentline[1])
        service = str(currentline[2])
        tuple_insert = (name, car, service)
        lst.append(tuple_insert)

f.close()
# testing functions
x.search_name("Tyler", lst)
x.add_new_user("Amal", "Aston Martin DB11", "Headlight replacement", lst)
x.search_car("Ferrari 488", lst)
x.delete_user("Aaron", "Ferrari 458", "Transmission fluid change", lst)
x.search_service("Tire change", lst)
x.customer_count(lst)

# size of the table
total_rows = len(lst)
total_columns = len(lst[0])

# window creation with the table and button.
main = Tk()
button1 = Button(main, text="Table", bd=5)
button1.pack()
table = Tk()
table.geometry("500x500")
t = Table(table)
main.mainloop()
table.mainloop()
