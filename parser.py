from Tkinter import *
from math import *

tk = Tk()

canvas = Canvas(tk, width=850, height=850)
canvas.grid(row=0, column=0)

settings = Tk()

l1 = Label(settings, text='File')
l1.grid(row=0, column=0, padx=10, pady=10)

s1 = Spinbox(settings, from_=0, to=100)
s1.grid(row=0, column=1, padx=10, pady=10)
s1.insert(END, 33)
s1.delete(0)

l2 = Label(settings, text='Start')
l2.grid(row=1, column=0, padx=10, pady=10)

s2 = Spinbox(settings, from_=0, to=20000)
s2.grid(row=1, column=1, padx=10, pady=10)
s2.insert(END, 8942)
s2.delete(0)

l3 = Label(settings, text='X Scale')
l3.grid(row=2, column=0, padx=10, pady=10)

s3 = Spinbox(settings, from_=1, to=100)
s3.grid(row=2, column=1, padx=10, pady=10)
s3.insert(END, 1)
s3.delete(0)

l4 = Label(settings, text='Y Scale')
l4.grid(row=3, column=0, padx=10, pady=10)

s4 = Spinbox(settings, from_=0, to=100)
s4.grid(row=3, column=1, padx=10, pady=10)
s4.insert(END, 4000)
s4.delete(0)

l5 = Label(settings, text='DOF')
l5.grid(row=4, column=0, padx=10, pady=10)

s5 = Spinbox(settings, from_=0, to=2)
s5.grid(row=4, column=1, padx=10, pady=10)

l6 = Label(settings, text='Jump To')
l6.grid(row=4, column=0, padx=10, pady=10)

s6 = Spinbox(settings, from_=0, to=749)
s6.grid(row=4, column=1, padx=10, pady=10)
s6.insert(END, 375)
s6.delete(0)

current = 0

def make():
    s = float(s4.get()) / 100
    canvas.delete('line')
    canvas.create_line(current, 0, current, 850, tag='line', fill='#999')
    b = float(int(data[0][current - 51] * 100)) / 100
    canvas.create_text(current, 175 - b * s / 100, tag='line', fill='#633', text=b)
    b = float(int(data[1][current - 51] * 100)) / 100
    canvas.create_text(current, 425 - b * s / 100, tag='line', fill='#363', text=b)
    b = float(int(data[2][current - 51] * 100)) / 100
    canvas.create_text(current, 675 - b * s / 100, tag='line', fill='#336', text=b)

def left(e):
    global current
    current -= 1
    if current < 50:
        current = 50
    make()

def right(e):
    global current
    current += 1
    if current > 799:
        current = 799
    make()

tk.bind('<Left>', left)
tk.bind('<Right>', right)

data = [[], [], [], []]
grated = [[], [], []]

thing = 0
stop = True

def integrate():
    global grated, stop, thing
    grated[0].append(
        (data[0][-2] ** 2 + data[1][-2] ** 2 + data[2][-2] ** 2) ** 0.5 *
        (data[3][-1] - data[3][-2]))
    last = grated[2][-1]
    grated[2].append(
        data[0][-2] * (data[3][-1] - data[3][-2]) + last)
    if stop:
        thing += data[0][-2] * (data[3][-1] - data[3][-2])
    if data[0][-2] < 0:
        stop = False
    
def update():
    global s1, canvas, data, current, thing, grated
    thing = 0
    stop = True
    data = [[], [], [], []]
    grated = [[], [], []]
    current = int(s6.get()) + 50
    canvas.delete('all')
    d = s1.get()
    t = int(s2.get())
    i = int(s3.get())
    s = float(s4.get()) / 100
    o = int(s5.get()) * 3
    m = 0
    a = [0, 0, 0]
    l = [0, 0, 0]
    f = open('data/LOG' + d + '.txt', 'r')
    #print current
    for line in f:
        m += 1
        if m > t:
            n = m - t + 50 * i
            a[0] += float(line.split(',')[o + 1]) * s
            a[1] += float(line.split(',')[o + 2]) * s
            a[2] += float(line.split(',')[o + 3]) * s
            if n % i == 0:
                z = (a[0] ** 2 + a[1] ** 2 + a[2] ** 2) ** 0.5
                for j in range(3):
                    if n / i < 799:
                        canvas.create_line(n / i, -z / i + j * 250 + 175,
                                           n / i, z / i + j * 250 + 175,
                                           fill='#ccc')
                    data[j].append(-(a[j] * 100) / (s * i))
                data[3].append(int(line.split(',')[0]))

                if len(data[0]) > 1:
                    integrate()
                else:
                    grated[0].append(0)
                    grated[2].append(0)

                if n / i < 799:
                    canvas.create_line(n / i, 175, n / i,
                                       a[0] / i + 175, fill='#fcc')
                    canvas.create_line(n / i, 425, n / i,
                                       a[1] / i + 425, fill='#cfc')
                    canvas.create_line(n / i, 675, n / i,
                                       a[2] / i + 675, fill='#ccf')

                    if n / i > 51:
                        canvas.create_line(n / i - 1, l[0] / i + 175, n / i,
                                           a[0] / i + 175, fill='#c99')
                        canvas.create_line(n / i - 1, l[1] / i + 425, n / i,
                                           a[1] / i + 425, fill='#9c9')
                        canvas.create_line(n / i - 1, l[2] / i + 675, n / i,
                                           a[2] / i + 675, fill='#99c')
                    
                    l[0] = a[0]
                    l[1] = a[1]
                    l[2] = a[2]
                    a = [0, 0, 0]

                if n / i > 800:
                    break

    canvas.create_line(50, 175, 800, 175, fill='#966')
    canvas.create_line(50, 425, 800, 425, fill='#696')
    canvas.create_line(50, 675, 800, 675, fill='#669')

    for j in range(16):
        canvas.create_text((j + 1) * 50, 825, text=
                           j * (data[3][-1] - data[3][0]) / 15000,
                           fill='#666')
        canvas.create_text((j + 1) * 50, 25, text=
                           j * (data[3][-1] - data[3][0]) / 15000,
                           fill='#666')
    for h in range(3):
        for j in range(9):
            k = int(2500 * float(4 - j) / s)
            canvas.create_text(825, (j + 3) * 25 + h * 250, text=k,
                               fill='#666')
            canvas.create_text(25, (j + 3) * 25+ h * 250, text=k,
                               fill='#666')

    make()
    print thing

update()
make()

b1 = Button(settings, text='Update', command=update)
b1.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

settings.wm_title('Settings')
tk.wm_title('Graph')

settings.mainloop()
tk.mainloop()
