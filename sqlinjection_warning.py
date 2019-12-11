"""
Потенциально опасный код с sql иньекцией когда строка запроса создается форматированием строки
"""

name = 'Ivan'
query = f'SELECT * from persons where name = {name}'
print(query)