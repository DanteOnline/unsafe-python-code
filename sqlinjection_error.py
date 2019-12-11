"""
Содержит уязвимость с sql иньекцией когда строка запроса создается форматированием строки
мы получаем данные из вне и отправляем запрос в базу
"""
import sqlite3

name = input('Введтие имя человека')
query = f'SELECT * from persons where name = {name}'

connecton = sqlite3.connect('some.db')
cursor = connecton.cursor()
cursor.execute(query)
