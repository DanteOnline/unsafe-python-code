"""
Код содержит уязвимость когда в eval передаются данные из стороннего источника,
например из input или файла
"""

with open('some.txt', 'r') as f:
    test = f.read()

print(eval(test))