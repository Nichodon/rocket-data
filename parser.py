from Tkinter import *
from math import *

tk = Tk()
canvas = Canvas(tk, width=900, height=900)
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
s4.insert(END, 30)
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
            n = m - t
            try: 
                a[0] += float(line.split(',')[1]) * s
                a[1] += float(line.split(',')[2]) * s
                a[2] += float(line.split(',')[3]) * s
                if n % i == 0:
                    z = abs(a[0]) + abs(a[1]) + abs(a[2])
                    for j in range(3):
                        canvas.create_line(n / i, -z / i + j * 300 + 150,
                                           n / i, z / i + j * 300 + 150,
                                           fill='#ccc')
                    
                    canvas.create_line(n / i, 150, n / i,
                                       a[0] / i + 150, fill='#fcc')
                    canvas.create_line(n / i, 450, n / i,
                                       a[1] / i + 450, fill='#cfc')
                    canvas.create_line(n / i, 750, n / i,
                                       a[2] / i + 750, fill='#ccf')

                    canvas.create_line(n / i - 1, l[0] / i + 150, n / i,
                                       a[0] / i + 150, fill='#c99')
                    canvas.create_line(n / i - 1, l[1] / i + 450, n / i,
                                       a[1] / i + 450, fill='#9c9')
                    canvas.create_line(n / i - 1, l[2] / i + 750, n / i,
                                       a[2] / i + 750, fill='#99c')
                    
                    l[0] = a[0]
                    l[1] = a[1]
                    l[2] = a[2]
                    a = [0, 0, 0]

                    if n / i > 900:
                        break
            except IndexError:
                pass

    canvas.create_line(0, 150, 1000, 150, fill='#966')
    canvas.create_line(0, 450, 1000, 450, fill='#696')
    canvas.create_line(0, 750, 1000, 750, fill='#669')
    
    canvas.create_line(0, 300, 1000, 300, fill='#ccc')
    canvas.create_line(0, 600, 1000, 600, fill='#ccc')

update()

b1 = Button(settings, text='Update', command=update)
b1.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

settings.mainloop()
tk.mainloop()
