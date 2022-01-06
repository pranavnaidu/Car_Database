class Car: # class functions with comments
    def search_name(search_key_name, list_names): # searches for a name within the list
        i = 0
        found = 0
        for i in range(len(list_names)):
            if search_key_name == list_names[i][0]:
                print(search_key_name + " is in the list. Owns a" + list_names[i][1] + " and needs a" + list_names[i][2])
                found = 1
                continue
        if found == 0:
            print("The name is not in the list.")

    def search_car(search_key_car, list_names): # searches for a car within the list
        i = 0
        found = 0
        for i in range(len(list_names)):
            if search_key_car == list_names[i][1]:
                print("The car " + search_key_car + " is in the list. The owner is " + list_names[i][0] + " and needs a " + list_names[i][2] + ".")
                found = 1
                continue
        if found == 0:
            print("The car is not in the list.")

    def search_service(search_key_service, list_names): # searches for a service in the list
        i = 0
        found = 0
        for i in range(len(list_names)):
            if search_key_service == list_names[i][2]:
                print("The service " + search_key_service + " is in the list. The customer is " + list_names[i][0] + " and owns a " + list_names[i][1] + ".")
                found = 1
                continue
        if found == 0:
            print("The service is not in the list.")

    def add_new_user(name, car, service, list_names): # adds a new customer to the list
        add_tuple = (name, car, service)
        list_names.append(add_tuple)
        print("The user " + name + " with the " + car + " has been added to the list.")

    def delete_user(name, car, service, list_names): # removes a customer from the list
        i = 0
        for i in range(len(list_names)):
            if name == list_names[i][0]:
                if car == list_names[i][1]:
                    if service == list_names[i][2]:
                        list_names.remove(list_names[i])
                        print("The user " + name + " has been removed.")
                        continue
        else:
            print("The user " + name + " is not in the list.")

        return list_names

    def customer_count(list_names): # counts the number of customers in the list
        x = len(list_names)
        if x == 0:
            print("There are no customers in the database.")
        else:
            print("Number of customers: " + str(x))


    def search(key1, list_names):
        i = 0
        j = 0
        fieldvar = ''
        for i in range(len(list_names)):
            for j in range(len(list_names[i])):
                var1 = list_names[i][j]
                if key1 == var1:
                    if j == 0:
                        fieldvar == "Name"
                    elif j == 1:
                        fieldvar == "Car"
                    elif j == 2:
                        fieldvar == "Service"
                    else:
                        print("Error : " + j)

                    print(key1 + " : " + fieldvar)
                    print(list_names[i])
                    continue
