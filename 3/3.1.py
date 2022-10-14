from collections import Counter
foot_dict = {
'Россия': 'A',
'Португалия': 'B',
'Франция': 'C',
'Дания': 'C',
'Египет': 'A'
}
foot_dict[''] = 'B'
vvod = input()
itog = []
for i in foot_dict:
    if foot_dict[i] == vvod:
        itog.append(i)
col = list(foot_dict.values())
print(itog)
print(Counter(col))