from tkinter import *
from Functions import Car

class Table:

    def __init__(self, main):
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(main, width=20, fg='black', font=('Arial', 10))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

x = Car

lst = [("Pranav", "Porsche 911", "Oil change"),
       ("Nirav", "Lexus LFA", "Oil change"),
       ("Sasank", "Mercedes AMG GTR", "Tire change"),
       ("Rithwik", "Audi R8", "Brake pad change"),
       ("Adi", "Ferrari 458", "Transmission fluid change"),
       ("Shrihan", "BMW M8", "Alignment check"),
       ("Rohan", "Acura NSX", "Battery replacement"),
       ("Dheeraj", "Nissan GTR", "Interior cleaning"),
       ("Vinni", "Lamborghini Huracan", "Engine replacement"),
       ("Arya", "Mclaren 570S", "Front lift")]

x.search_name("Nirav", lst)
x.add_new_user("Amal", "Aston Martin DB11", "Headlight replacement", lst)
x.search_car("Aston Martin DB11", lst)
x.delete_user("Pranav", "Porsche 911", "Oil change", lst)
x.search_service("Oil change", lst)
x.customer_count(lst)

total_rows = len(lst)
total_columns = len(lst[0])

main = Tk()
button1 = Button(main, text="Table", bd=5)
button1.pack()
table = Tk()
table.geometry("500x500")
t = Table(table)
main.mainloop()
table.mainloop()
