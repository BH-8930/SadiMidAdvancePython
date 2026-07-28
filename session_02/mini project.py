from tkinter import *

#window settings
win = Tk()
win.geometry('900x900')
win.title('contacts')
win.config(bg='#869d88')

#add frame
adding_frame = Frame(win, padx=20, pady=20, bg='#40656c')
adding_frame.pack()

#fname
fname_lb = Label(adding_frame, text='نام')
fname_en = Entry(adding_frame)

#lname
lname_lb = Label(adding_frame, text='نام خانوادگی')
lname_en = Entry(adding_frame)

#phone
phone_lb = Label(adding_frame, text='شماره تلفن')
phone_en = Entry(adding_frame)


#packing the add frame
fname_lb.pack(pady=10)
fname_en.pack(pady=10)
lname_lb.pack(pady=10)
lname_en.pack(pady=10)
phone_lb.pack(pady=10)
phone_en.pack(pady=10)


#add processes:
def save_contact():

    fname = fname_en.get()
    lname = lname_en.get()
    phone = phone_en.get()

    fname_en.delete(0, END)
    lname_en.delete(0, END)
    phone_en.delete(0, END)

    #add into file
    with open("contacts.txt", 'a', encoding='utf-8') as file:
        file.write(f"{fname},{lname},{phone}" + "\n")

#submit button
submit_btn = Button(adding_frame, text='ثبت مخاطب', command=save_contact)
submit_btn.pack()

#show contacts frame
show_frame = Frame(win, padx=20, pady=20, bg='#af9a81')
contact_list = Listbox(show_frame)

#packing show contacts
show_frame.pack()
contact_list.pack(padx=20, pady=10)

#show processes
def show_contact():

    contact_list.delete(0, END)

    with open("contacts.txt", "r", encoding='utf-8') as file:

        for line in file:
            lst = line.strip().split(',')

            contact = f"{lst[0]} {lst[1]} - {lst[2]}"

            contact_list.insert(END, contact)


#show button
show_btn = Button(show_frame, text="نمایش مخاطبان", command=show_contact)
show_btn.pack()


#search frame
search_frame = Frame(win, padx=20, pady=20, bg='#ffeccc')
search = Entry(search_frame)

#packing search frame
search_frame.pack()
search.pack(padx=20, pady=10)

#searching processes
def search_contact():

    searching = search.get()

    search.delete(0, END)

    contact_list.delete(0, END)

    with open("contacts.txt", encoding='utf-8') as file:

        for line in file:
            if searching != '' and searching in line:

                lst = line.split(",")

                contact = f"{lst[0]} {lst[1]} - {lst[2]}"

                contact_list.insert(END, contact)

#search button
search_btn = Button(search_frame, text="جستجو", command=search_contact)
search_btn.pack()

#delete processes
def delete_contact():

    selected = contact_list.curselection()

    if not selected:
        return

    selected_contact = contact_list.get(selected)

    with open("contacts.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open("contacts.txt", "w", encoding="utf-8") as file:
        for line in lines:
            lst = line.strip().split(",")

            contact = f"{lst[0]} {lst[1]} - {lst[2]}"

            if contact != selected_contact:
                file.write(line)

    contact_list.delete(selected)

#delete buttom
delete_btn = Button(show_frame, text='حذف مخاطب', command=delete_contact)
delete_btn.pack()

#show
win.mainloop()