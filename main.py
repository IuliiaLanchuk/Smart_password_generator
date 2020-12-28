import random
from tkinter import *
import time

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.!#$%&*+-=?@^_.!#$%&*+-=?@^_.'
ambiguous_symbols = 'il1Lo0O'


def isdigit_(a):
    if a.isdecimal():
        return True
    else:
        return False


def yes_or_no(b):
    if 'yes' in b or 'no' in b or 'YES' in b or 'NO' in b or 'Yes' in b or 'No' in b:
        return True
    else:
        return False


def clicked():
    size = list.size()
    if size != 0:
        list.delete(0, size)
    password = []

    amount_of_psw_value = amount_of_psw_entry.get()
    if len(amount_of_psw_value) == 0:
        lbl_empty_entry = Label(text='Should not be empty', bg='khaki1', fg='red')
        lbl_empty_entry.grid(row=1, column=2, sticky="w")
    else:
        lbl_empty_entry = Label(text='Should not be empty', bg='khaki1', fg='khaki1')
        lbl_empty_entry.grid(row=1, column=2, sticky="w")
        if not isdigit_(amount_of_psw_value):
            lbl_incorrect_psw_entry = Label(text='Incorrect format', bg='khaki1', fg='red')
            lbl_incorrect_psw_entry.grid(row=1, column=2, sticky="w")
        else:  # костыль
            lbl_incorrect_psw_entry = Label(text='Incorrect format', bg='khaki1', fg='khaki1')
            lbl_incorrect_psw_entry.grid(row=1, column=2, sticky="w")

    psw_len_value = psw_len_entry.get()
    if len(psw_len_value) == 0:
        lbl_empty_entry = Label(text='Should not be empty', bg='khaki1', fg='red')
        lbl_empty_entry.grid(row=2, column=2, sticky="w")
    else:
        lbl_empty_entry = Label(text='Should not be empty', bg='khaki1', fg='khaki1')
        lbl_empty_entry.grid(row=2, column=2, sticky="w")
        if not isdigit_(psw_len_value):
            lbl_incorrect_psw_len = Label(text='Incorrect format', bg='khaki1', fg='red')
            lbl_incorrect_psw_len.grid(row=2, column=2, sticky="w")
        else:  # костыль
            lbl_incorrect_psw_len = Label(text='Incorrect format', bg='khaki1', fg='khaki1')
            lbl_incorrect_psw_len.grid(row=2, column=2, sticky="w")

    is_numbers_value = is_numbers_entry.get()
    if len(is_numbers_value) == 0:
        lbl_empty_entry = Label(text='Should not be empty', bg='khaki1', fg='red')
        lbl_empty_entry.grid(row=3, column=2, sticky="w")
    else:
        lbl_empty_entry = Label(text='Should not be empty', bg='khaki1', fg='khaki1')
        lbl_empty_entry.grid(row=3, column=2, sticky="w")
        if not yes_or_no(is_numbers_value):
            lbl_incorrect_numbers = Label(text='Incorrect format', bg='khaki1', fg='red')
            lbl_incorrect_numbers.grid(row=3, column=2, sticky="w")
        if "yes" in is_numbers_value or "Yes" in is_numbers_value or "YES" in is_numbers_value:
            password.extend(digits)

    is_lowercase_letters_value = is_lowercase_letters_entry.get()
    if len(is_lowercase_letters_value) == 0:
        lbl_empty_entry = Label(text='Should not be empty', bg='khaki1', fg='red')
        lbl_empty_entry.grid(row=4, column=2, sticky="w")
    else:
        lbl_empty_entry = Label(text='Should not be empty', bg='khaki1', fg='khaki1')
        lbl_empty_entry.grid(row=4, column=2, sticky="w")
        if not yes_or_no(is_lowercase_letters_value):
            lbl_incorrect_lower = Label(text='Incorrect format', bg='khaki1', fg='red')
            lbl_incorrect_lower.grid(row=4, column=2, sticky="w")
        if "yes" in is_lowercase_letters_value or "Yes" in is_lowercase_letters_value or "YES" in is_lowercase_letters_value:
            password.extend(lowercase_letters)

    is_uppercase_letters_value = is_uppercase_letters_entry.get()
    if len(is_uppercase_letters_value) == 0:
        lbl_empty_entry = Label(text='Should not be empty', bg='khaki1', fg='red')
        lbl_empty_entry.grid(row=5, column=2, sticky="w")
    else:
        lbl_empty_entry = Label(text='Should not be empty', bg='khaki1', fg='khaki1')
        lbl_empty_entry.grid(row=5, column=2, sticky="w")
        if not yes_or_no(is_uppercase_letters_value):
            lbl_incorrect_upper = Label(text='Incorrect format', bg='khaki1', fg='red')
            lbl_incorrect_upper.grid(row=5, column=2, sticky="w")
        if "yes" in is_uppercase_letters_value or "Yes" in is_uppercase_letters_value or "YES" in is_uppercase_letters_value:
            password.extend(uppercase_letters)

    is_symbols_value = is_symbols_entry.get()
    if len(is_symbols_value) == 0:
        lbl_empty_entry = Label(text='Should not be empty', bg='khaki1', fg='red')
        lbl_empty_entry.grid(row=6, column=2, sticky="w")
    else:
        lbl_empty_entry = Label(text='Should not be empty', bg='khaki1', fg='khaki1')
        lbl_empty_entry.grid(row=6, column=2, sticky="w")
        if not yes_or_no(is_symbols_value):
            lbl_incorrect_symbols = Label(text='Incorrect format', bg='khaki1', fg='red')
            lbl_incorrect_symbols.grid(row=6, column=2, sticky="w")
        if "yes" in is_symbols_value or "Yes" in is_symbols_value or "YES" in is_symbols_value:
            password.extend(punctuation)

    ignore_another_symbols_value = ignore_another_symbols_entry.get()
    if len(ignore_another_symbols_value) == 0:
        lbl_empty_entry = Label(text='Should not be empty', bg='khaki1', fg='red')
        lbl_empty_entry.grid(row=7, column=2, sticky="w")
    else:
        lbl_empty_entry = Label(text='Should not be empty', bg='khaki1', fg='khaki1')
        lbl_empty_entry.grid(row=7, column=2, sticky="w")
        if not yes_or_no(ignore_another_symbols_value):
            lbl_incorrect_ambiguous_symbols = Label(text='Incorrect format', bg='khaki1', fg='red')
            lbl_incorrect_ambiguous_symbols.grid(row=7, column=2, sticky="w")

    print(password)
    # генерация паролей происходит здесь
    if "yes" in [is_symbols_value, is_uppercase_letters_value, is_lowercase_letters_value,
                                   is_numbers_value]:
        for i in range(int(amount_of_psw_value)):
            final_psw = random.sample(password, int(psw_len_value))
            list.insert(END, ''.join(final_psw))
        list.grid(row=11, column=0)

    if "no" in is_symbols_value and "no" in is_uppercase_letters_value and "no" in is_lowercase_letters_value \
            and "no" in is_numbers_value:
        text = 'Password can`t be generated because you filled in '
        text2 = 'fields with "no".'
        list.insert(END, ''.join(text))
        list.insert(END, ''.join(text2))
        list.grid(row=11, column=0)


window = Tk()
window.title("Password Generator App")
window.config(bg='khaki1')
window.geometry('545x510')
lbl = Label(window, text="Please, fill in all the fields", font=("Helvetica", "12", "bold"), bg='khaki1', padx="50",
            pady="10")
lbl.grid(column=0, row=0)

amount_of_psw = StringVar()
psw_len = StringVar()
is_numbers = StringVar()
is_lowercase_letters = StringVar()
is_uppercase_letters = StringVar()
is_symbols = StringVar()
ignore_another_symbols = StringVar()

amount_of_psw_label = Label(text="Amount of passwords you need:", bg='khaki1')
psw_len_label = Label(text="Password length in symbols amount:", bg='khaki1')
is_numbers_label = Label(text="Numbers should be in password? **", bg='khaki1')
is_lowercase_letters_label = Label(text="Lowercase letters (a,b,c..) should be in password? **", bg='khaki1')
is_uppercase_letters_label = Label(text="Uppercase letters (A,B,C..) should be in password? **", bg='khaki1')
is_symbols_label = Label(text="Symbols (!,#,$...) should be in password? **", bg='khaki1')
ignore_another_symbols_label = Label(text="Exclude ambiguous characters (il1Lo0O)? **", bg='khaki1')

amount_of_psw_label.grid(row=1, column=0, sticky="w")
psw_len_label.grid(row=2, column=0, sticky="w")
is_numbers_label.grid(row=3, column=0, sticky="w")
is_lowercase_letters_label.grid(row=4, column=0, sticky="w")
is_uppercase_letters_label.grid(row=5, column=0, sticky="w")
is_symbols_label.grid(row=6, column=0, sticky="w")
ignore_another_symbols_label.grid(row=7, column=0, sticky="w")

amount_of_psw_entry = Entry(textvariable=amount_of_psw)
psw_len_entry = Entry(textvariable=psw_len)
is_numbers_entry = Entry(textvariable=is_numbers)
is_lowercase_letters_entry = Entry(textvariable=is_lowercase_letters)
is_uppercase_letters_entry = Entry(textvariable=is_uppercase_letters)
is_symbols_entry = Entry(textvariable=is_symbols)
ignore_another_symbols_entry = Entry(textvariable=ignore_another_symbols)

amount_of_psw_entry.grid(row=1, column=1, padx=5, pady=5)
psw_len_entry.grid(row=2, column=1, padx=5, pady=5)
is_numbers_entry.grid(row=3, column=1, padx=5, pady=5)
is_lowercase_letters_entry.grid(row=4, column=1, padx=5, pady=5)
is_uppercase_letters_entry.grid(row=5, column=1, padx=5, pady=5)
is_symbols_entry.grid(row=6, column=1, padx=5, pady=5)
ignore_another_symbols_entry.grid(row=7, column=1, padx=5, pady=5)

btn_generate_psw = Button(window, text="Generate password(s)", bg="light blue", fg="grey26", command=clicked)
btn_generate_psw.grid(column=1, row=8, padx="5", pady="5")
lbl2 = Label(window, text='** answer "yes" or "no"', font=("Arial", 8), bg='pale goldenrod')
lbl2.grid(column=0, row=8)

lbl_result = Label(window, text='Result', font=("Helvetica", "12", "bold"), bg='khaki1', padx="65", pady="15")
lbl_result.grid(column=0, row=10)
list = Listbox(bg='pale goldenrod', width='45', height='10')
list.grid(row=11, column=0)
window.mainloop()
