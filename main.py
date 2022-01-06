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

with open("input.txt") as f:
    for line in f:
        currentline = line.split(',')
        name = currentline[0]
        car = currentline[1]
        service = currentline[2]
        tuple_insert = (name, car, service)
        lst.append(tuple_insert)

f.close()
# testing functions
x.search_name("Tyler Williams", lst)
x.add_new_user("Amal Sam", "Aston Martin DB11", "Headlight replacement", lst)
x.search_car("Porsche 911", lst)
lst1 = x.delete_user("Adi Ramana", "Ferrari 458", "Tire change", lst)
x.search_service("Tire change", lst)
x.customer_count(lst)
x.search("Porsche 911", lst)

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

i = 0

output = open("output.txt", "w")

for i in range(len(lst)):
    name = str(lst[i][0])
    car = str(lst[i][1])
    service = str(lst[i][2])
    output.write(name + "," + car + "," + service)

output.close()
