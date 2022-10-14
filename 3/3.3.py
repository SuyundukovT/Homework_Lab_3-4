print('Нормативы забегов следующие:')
print('              Оценка      5    4     3')
a = ['6 Класс', 'Мальчики:', 9.9, 10.4, 11.1]
b = ['6 Класс', 'Девочки:', 10.3, 10.6, 11.2]
c = ['7 Класс', 'Мальчики:', 9.4, 10.2, 11.0]
d = ['7 Класс', 'Девочки: ', 9.8, 10.6, 11.4]
print(a)
print(b)
print(c)
print(d)
rez = []
klass = []
pol = []
ok = []
with open("run_of_60_m.txt", mode = 'r+', encoding = 'utf-8') as file:
    ludi = [row.strip() for row in file]
    for i in range(len(ludi)):
        ind1 = ludi[i].find('Время')
        ind2 = ludi[i].find('Класс')
        rez.append(ludi[i][ind1+6:ind2-5])

    for i in range(len(ludi)):
        ind = ludi[i].rfind('Класс')
        ind3 = ludi[i].rfind('Класс')
        pol.append(ludi[i][ind-4:ind-1])
        klass.append(ludi[i][ind3+6:ind3+9])
    file.close()

with open("run_of_60_mark.txt", mode = 'w+', encoding = 'utf-8') as otvet:
    for i in range(len(ludi)):
        if klass[i] == '6':
            if pol[i] == 'Муж':
                if float(rez[i]) < a[2]:
                    otvet.write(ludi[i] + ' Оценка - 5' + '\n')
                    continue

        if klass[i] == '6':
            if pol[i] == 'Муж':
                if float(rez[i]) > a[2] and float(rez[i]) <= a[3]:
                    otvet.write(ludi[i] + ' Оценка - 4' + '\n')
                    otvet.flush()

        if klass[i] == '6':
            if pol[i] == 'Муж':
                if float(rez[i]) > a[3] and float(rez[i]) <= a[4] :
                    otvet.write(ludi[i] + ' Оценка - 3' + '\n')
                    otvet.flush()

        if klass[i] == '6':
            if pol[i] == 'Муж':
                if float(rez[i]) > a[4]:
                    otvet.write(ludi[i] + ' Оценка - 2' + '\n')
                    continue

        if klass[i] == '6':
            if pol[i] == 'Жен':
                if float(rez[i]) < b[2]:
                    otvet.write(ludi[i] + ' Оценка - 5' + '\n')
                    continue

        if klass[i] == '6':
            if pol[i] == 'Жен':
                if float(rez[i]) > b[2] and float(rez[i]) <= b[3]:
                    otvet.write(ludi[i] + ' Оценка - 4' + '\n')
                    continue

        if klass[i] == '6':
            if pol[i] == 'Жен':
                if float(rez[i]) > b[3] and float(rez[i]) <= b[4] :
                    otvet.write(ludi[i] + ' Оценка - 3' + '\n')
                    continue

        if klass[i] == '6':
            if pol[i] == 'Жен':
                if float(rez[i]) > b[4]:
                    otvet.write(ludi[i] + ' Оценка - 2' + '\n')
                    continue

        if klass[i] == '7':
            if pol[i] == 'Муж':
                if float(rez[i]) < c[2]:
                    otvet.write(ludi[i] + ' Оценка - 5' + '\n')
                    continue

        if klass[i] == '7':
            if pol[i] == 'Муж':
                if float(rez[i]) > c[2] and float(rez[i]) <= c[3]:
                    otvet.write(ludi[i] + ' Оценка - 4' + '\n')
                    continue

        if klass[i] == '7':
            if pol[i] == 'Муж':
                if float(rez[i]) > c[3] and float(rez[i]) <= c[4] :
                    otvet.write(ludi[i] + ' Оценка - 3' + '\n')
                    continue

        if klass[i] == '7':
            if pol[i] == 'Муж':
                if float(rez[i]) > c[4]:
                    otvet.write(ludi[i] + ' Оценка - 2' + '\n')
                    continue

        if klass[i] == '7':
            if pol[i] == 'Жен':
                if float(rez[i]) < d[2]:
                    otvet.write(ludi[i] + ' Оценка - 5' + '\n')
                    continue

        if klass[i] == '7':
            if pol[i] == 'Жен':
                if float(rez[i]) > d[2] and float(rez[i]) <= d[3]:
                    otvet.write(ludi[i] + ' Оценка - 4' + '\n')
                    continue

        if klass[i] == '7':
            if pol[i] == 'Жен':
                if float(rez[i]) > d[3] and float(rez[i]) <= d[4] :
                    otvet.write(ludi[i] + ' Оценка - 3' + '\n')
                    continue
        if klass[i] == '7':
            if pol[i] == 'Жен':
                if float(rez[i]) > d[4]:
                    otvet.write(ludi[i] + ' Оценка - 2' + '\n')
                    continue

rezi = [float(x) for x in rez]

top = 0
minimum = 10000
for i in range(len(pol)):
    if pol[i] == 'Жен':
        minimum = min(rezi[i], minimum)
        if minimum < rezi[i]:
            top = i-2
o = ludi[top].find('Время')
h = ludi[top].find('Класс')

print('')

print('Самой быстрой школьницей оказалась' + ludi[top][3:o-1] + ', ученица ' + ludi[top][h+6:h+8] + ' класса с результатом ' + rez[top] )

print('')
top = 0
minimum = 10000
for i in range(len(pol)):
    if pol[i] == 'Муж':
        minimum = min(rezi[i], minimum)
        if minimum < rezi[i]:
            top = i-1
o = ludi[top].find('Время')
h = ludi[top].find('Класс')
print('Самым быстрым школьником оказался' + ludi[top][3:o-1] + ', ученик ' + ludi[top][h+6:h+8] + ' класса с результатом ' + rez[top] )