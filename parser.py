from Tkinter import *
from math import *

tk = Tk()
canvas = Canvas(tk, width=850, height=850)
canvas.pack()

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
s2.insert(END, 8750)
s2.delete(0)

l3 = Label(settings, text='X Scale')
l3.grid(row=2, column=0, padx=10, pady=10)

s3 = Spinbox(settings, from_=1, to=100)
s3.grid(row=2, column=1, padx=10, pady=10)
s3.insert(END, 6)
s3.delete(0)

l4 = Label(settings, text='Y Scale')
l4.grid(row=3, column=0, padx=10, pady=10)

s4 = Spinbox(settings, from_=0, to=100)
s4.grid(row=3, column=1, padx=10, pady=10)
s4.insert(END, 25)
s4.delete(0)

def update():
    global s1, canvas
    canvas.delete('all')
    d = s1.get()
    t = int(s2.get())
    i = int(s3.get())
    s = int(s4.get())
    m = 0
    a = [0, 0, 0]
    l = [0, 0, 0]
    f = open('data/LOG' + d + '.txt', 'r')
    for line in f:
        m += 1
        if m > t:
            n = m - t + 50 * i
            try: 
                a[0] += float(line.split(',')[1]) * s
                a[1] += float(line.split(',')[2]) * s
                a[2] += float(line.split(',')[3]) * s
                if n % i == 0:
                    z = abs(a[0]) + abs(a[1]) + abs(a[2])
                    for j in range(3):
                        canvas.create_line(n / i, -z / i + j * 250 + 175,
                                           n / i, z / i + j * 250 + 175,
                                           fill='#ccc')
                    
                    canvas.create_line(n / i, 175, n / i,
                                       a[0] / i + 175, fill='#fcc')
                    canvas.create_line(n / i, 425, n / i,
                                       a[1] / i + 425, fill='#cfc')
                    canvas.create_line(n / i, 675, n / i,
                                       a[2] / i + 675, fill='#ccf')

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

                    if n / i >= 799:
                        break
            except IndexError:
                pass

    canvas.create_line(50, 175, 800, 175, fill='#966')
    canvas.create_line(50, 425, 800, 425, fill='#696')
    canvas.create_line(50, 675, 800, 675, fill='#669')

    for j in range(16):
        canvas.create_text((j + 1) * 50, 825, text=t + 50 * (j + 1) * i,
                           fill='#666')
        canvas.create_text((j + 1) * 50, 25, text=t + 50 * (j + 1) * i,
                           fill='#666')
    for h in range(3):
        for j in range(9):
            k = int(2500 * float(4 - j) / s)
            canvas.create_text(825, (j + 3) * 25 + h * 250, text=k,
                               fill='#666')
            canvas.create_text(25, (j + 3) * 25+ h * 250, text=k,
                               fill='#666')

update()

b1 = Button(settings, text='Update', command=update)
b1.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

settings.mainloop()
tk.mainloop()
