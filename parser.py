from Tkinter import *

tk = Tk()
canvas = Canvas(tk, width=1000, height=400)
canvas.pack()

m = 0
a = 0
d = ['15']
l = 0

for datum in d:
    f = open('data/LOG' + datum + '.txt', 'r')
    for line in f:
        m += 1
        if m > 64000:
            n = m - 64000
            a += float(line.split(',')[4]) / 10
            if n % 10 == 0:
                canvas.create_line(n / 10, 200, n / 10, a / 10 + 200,
                                   fill='lightblue')
                canvas.create_line(n / 10 - 1, l / 10 + 200, n / 10,
                                   a / 10 + 200,
                                   fill='darkblue')
                l = a
                a = 0

canvas.create_line(0, 200, 1000, 200,
                                   fill='blue')

mainloop()
