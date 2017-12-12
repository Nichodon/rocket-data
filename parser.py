from Tkinter import *
from math import *

tk = Tk()
canvas = Canvas(tk, width=1000, height=900)
canvas.pack()

m = 0
a = [0, 0, 0]
d = ['33']
l = [0, 0, 0]
s = 30
t = 8500
i = 5

for datum in d:
    f = open('data/LOG' + datum + '.txt', 'r')
    for line in f:
        m += 1
        if m > t:
            n = m - t
            a[0] += float(line.split(',')[1]) * s
            a[1] += float(line.split(',')[2]) * s
            a[2] += float(line.split(',')[3]) * s
            if n % i == 0:
                z = abs(a[0]) + abs(a[1]) + abs(a[2])
                c = ['#fcc', '#cfc', '#ccf']
                for j in range(3):
                    canvas.create_line(n / i, -z / i + j * 300 + 150,
                                       n / i, z / i + j * 300 + 150,
                                       fill=c[j])
                
                canvas.create_line(n / i, 150, n / i,
                                   a[0] / i + 150, fill='#c99')
                canvas.create_line(n / i, 450, n / i,
                                   a[1] / i + 450, fill='#9c9')
                canvas.create_line(n / i, 750, n / i,
                                   a[2] / i + 750, fill='#99c')

                canvas.create_line(n / i - 1, l[0] / i + 150, n / i,
                                   a[0] / i + 150, fill='#966')
                canvas.create_line(n / i - 1, l[1] / i + 450, n / i,
                                   a[1] / i + 450, fill='#696')
                canvas.create_line(n / i - 1, l[2] / i + 750, n / i,
                                   a[2] / i + 750, fill='#669')
                
                l[0] = a[0]
                l[1] = a[1]
                l[2] = a[2]
                a = [0, 0, 0]

canvas.create_line(0, 150, 1000, 150, fill='#633')
canvas.create_line(0, 450, 1000, 450, fill='#363')
canvas.create_line(0, 750, 1000, 750, fill='#336')

mainloop()
