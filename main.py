#1
'''A = {'Саша', 'Аня', 'Нико', 'Миша', 'Карина'} # должники за Сентябрь
B = {'Николоз', 'Пеня', 'Катя', 'Маша', 'Дима'} # должники за Октябрь

print(f'Должники за Сентябрь и Октябрь: {A, B}')
print(f'Должники за Октябрь : {B - A}')'''

#2
access_files = {}
n = int(input('Number of files : '))
for i in range(n):
    files_input = input(f'Enter names of files #{i + 1} and command: ').split()
    access_files[files_input[0]] = set(files_input[1:])
for k in range(int(input('Enter number of file requests, m: '))):
    ar, request = input(f'Enter the command and name the file, request #{k + 1}: ').split()
    if ar == 'write':
        ar = 'W'
    if ar == 'read':
        ar = 'R'
    if ar == 'execute':
        ar = 'X'
    if ar in access_files[request]:
        print('OK')
    else:
        print('Access denied')