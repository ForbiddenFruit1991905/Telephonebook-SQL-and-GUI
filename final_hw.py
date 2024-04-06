import sqlite3 as sl
from easygui import *
import easygui

easygui.ynbox('Запустить телефонный справочник?', 'Справочник', ('ДА', 'НЕТ'))

msgbox("Справочник подгружен.")

conn = sl.connect('telephonebook.db')

cur = conn.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS contacts
            (
            id INTEGER PRIMARY KEY,
            lastname TEXT,
            firstname TEXT,
            middlename TEXT,
            phonenumber INTEGER,
            birthday TEXT,            
            email TEXT
            )
            ''')

def add_values():
    with sl.connect('telephonebook.db') as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO contacts VALUES (1, 'Lastname_1', 'Firstname_1', 'Middlename_1', 555, '01.01.1900', 'id_1@yandex.ru');")
        cur.execute("INSERT INTO contacts VALUES (2, 'Lastname_2', 'Firstname_2', 'Middlename_3', 333333333, '01.01.2000', null);")
        cur.execute("INSERT INTO contacts VALUES (3, null, 'Firstname_3', null, 444444444, null, 'id_3@yandex.ru');")
        conn.commit()
# add_values()

def select_all():
    with sl.connect('telephonebook.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM contacts')
        list_of_contacts = ''
        for row in cur.fetchall():
            list_of_contacts += str(row) + "\n"
        msgbox(list_of_contacts, 'Список контактов')
        conn.commit()

def add_contacts():
    with sl.connect('telephonebook.db') as conn:
        cur = conn.cursor()
        id = enterbox("Введите id контакта: ")                             
        lastname = enterbox("Введите фамилию контакта: ")
        firstname = enterbox("Введите имя контакта: ")
        middlename = enterbox("Введите отчество контакта: ")
        phonenumber = enterbox("Введите телефонный номер:")
        birthday = enterbox("Введите день рождения:")
        email = enterbox("Введите электронную почту:")
        cur.execute("INSERT INTO contacts (id, lastname, firstname, middlename, phonenumber, birthday, email) VALUES (?, ?, ?, ?, ?, ?, ?)", (id, lastname, firstname, middlename, phonenumber, birthday, email))
        msgbox('Новый контакт добавлен')
        conn.commit()           
    
def search_contact():
    with sl.connect('telephonebook.db') as conn:
        cur = conn.cursor()
        keyword = enterbox("Введите ключевое слово для поиска:")
        cur.execute('SELECT * FROM contacts WHERE id LIKE? OR lastname LIKE ? OR firstname LIKE ? OR middlename LIKE? OR phonenumber LIKE ? OR birthday LIKE ? OR email LIKE ?' , (keyword, '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%',  '%' + keyword + '%',  '%' + keyword + '%'))
        list_of_contacts = ''
        for row in cur.fetchall():
            list_of_contacts += str(row)        
            msgbox(list_of_contacts, 'Результат поиска контакта по ключу')
            conn.commit()

def edit_contact():
    with sl.connect('telephonebook.db') as conn:
        cur = conn.cursor()
        edit_id = enterbox("Введите уникальный id контакта: ")
        choice = choicebox("Выберите изменение", "Форма для редактирования", ['lastname', 'firstname', 'middlename', 'phonenumber', 'birthday', 'email'])
        if choice == 'lastname':
            new_lastname = enterbox("Введите new_lastname: ")
            cur.execute('UPDATE contacts SET lastname = '+ new_lastname +' WHERE id LIKE?' , (edit_id))                      
            msgbox("Запись о контакте изменена")
            conn.commit()
        if choice == 'firstname':
            new_firstname = enterbox("Введите new_firstname: ")
            cur.execute('UPDATE contacts SET firstname = '+ new_firstname +' WHERE id LIKE?' , (edit_id))                      
            msgbox("Запись о контакте изменена")
            conn.commit()
        if choice == 'middlename':
            new_middlename = enterbox("Введите new_middlename: ")
            cur.execute('UPDATE contacts SET middlename = '+ new_middlename +' WHERE id LIKE?' , (edit_id))                      
            msgbox("Запись о контакте изменена")
            conn.commit()
        if choice == 'phonenumber':
            new_phonenumber = enterbox("Введите new_phonenumber: ")
            cur.execute('UPDATE contacts SET phonenumber = '+ new_phonenumber +' WHERE id LIKE?' , (edit_id))                      
            msgbox("Запись о контакте изменена")
            conn.commit()
        if choice == 'birthday':
            new_birthday = enterbox("Введите new_birthday: ")
            cur.execute('UPDATE contacts SET birthday = '+ new_birthday +' WHERE id LIKE?' , (edit_id))                      
            msgbox("Запись о контакте изменена")
            conn.commit()
        if choice == 'email':
            new_email = enterbox("Введите new_email: ")
            cur.execute('UPDATE contacts SET email = '+ new_email +' WHERE id LIKE?' , (edit_id))                      
            msgbox("Запись о контакте изменена")
            conn.commit()

def delete_contact():
    with sl.connect('telephonebook.db') as conn:
        cur = conn.cursor()
        id = enterbox("Введите id контакта для удаления:")
        cur.execute('DELETE FROM contacts WHERE id LIKE?', (id))
        print(cur.fetchall())
        msgbox("Контакт удален")
        conn.commit()      
    
def main():
    while True:
        choice = choicebox("Выберите действие", "Главная форма", ['Просмотр контактов', 'Добавить контакт', 'Поиск', 'Редактирование записи контакта', 'Удалить контакт', 'Выйти из приложения'])
        if choice == "Просмотр контактов":
            select_all()
        if choice == "Добавить контакт":
            add_contacts()
        if choice == "Поиск":
            search_contact()              
        if choice == "Редактирование записи контакта":
            edit_contact()
        if choice == "Удалить контакт":
            delete_contact()
        if choice == "Выйти из приложения":
            break
    conn.close()

if __name__ == '__main__':
    main()
