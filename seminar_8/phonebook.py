from os import path

file_base = "base.txt"

all_data = []
id = 0

if not path.exists(file_base):
    with open (file_base, "w", encoding= "utf-8") as _:
        pass


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a new record\n"
                       "3. Search a record\n"
                       "4. Delite a record\n"
                       "5. Edit post\n"
                       "6. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_rec()
            case "3":
                search_rec()
            case "4":
                delite_post()
            case "5":
                edit_post()
            case "6":
                play = False
            case _:
                print("Try again!\n")
        print()


def read_records():
    global all_data, id

    with open(file_base, "r") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            id = int(all_data[-1][0])
        else: return all_data


def show_all():
    if not all_data:
        print("no entries")
    print(*all_data, sep='\n')


def add_new_rec():
    global id, all_data

    id = str(id + 1)
    x = ['surname', 'name', 'patronymic', 'phonenumber']
    b = id +' '
    for i in x:
        b += input(f'enter {i}: ') + ' '
    search = b.split()
    for rec in all_data:
        if search[-1] in rec:
            print(f'exists num. in {rec}')
            return rec
        
    with open(file_base, "a", encoding= "utf-8") as f:
        f.write(f'{b} \n')
        

def search_rec():
    global all_data

    search = input('search : ').lower()
    for rec in all_data:
        if search in rec.lower():
            print(rec)
            return rec[0]
        
def delite_post():
    global all_data, id
    result = int(search_rec()) - 1
    all_data.pop(result)
    id = 0
    with open (file_base, "w", encoding= "utf-8") as f:
        for row in all_data:
            id += 1
            f.write(f"{id}{row[1:]}\n")

def edit_post():
    global all_data, id
    row = int(search_rec()) - 1
    # all_data.insert(result, new_rec)
    start = True
    while start:
        answer = input('edit:\n'
                    '1. surname\n'
                    '2. name\n'
                    '3. patronymic\n'
                    '4. phonenumber\n'
                    '5. cancel\n')
        match answer:
            case "1":
                all_data[row][1] = input('new: ')
            case "2":
                all_data[row][2] = input('new: ')
            case "3":
                all_data[row][3] = input('new: ')
            case "4":
                all_data[row][4] = input('new: ')
            case "5":
                start = False
        with open (file_base, "w", encoding= "utf-8") as f:
            for c in all_data:
                f.write(f"{c}\n")
    print()








            



        



# show_all()
# add_new_rec()



main_menu()








