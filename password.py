def improve_password(improvements, password):
    
    password_let = []

    for letter in password:
        password_let.append(letter)


    new_password = ""

    for items in password_let:
        for key, vallue in improvements.items():
            if items == key:
                item_index = password_let.index(items)
                password_let.remove(items)
                password_let.insert(item_index, vallue)

    for new_item in password_let:
        new_password = new_password + new_item

    return new_password

improvements = {
        "s": "$",
        "S": "$",
        "A": "4",
        "a": "@",
        "e": "3",
        "B": "8",
        }


print(improve_password(improvements, "BeatlesFan11"))
    
