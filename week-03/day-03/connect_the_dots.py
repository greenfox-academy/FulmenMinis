from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]

box = [[10, 10], [290,  10], [290, 290], [10, 290]]
shape = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]]

def draw(lists):
    for i in range(len(lists)):
        try:
            line = canvas.create_line(lists[i], lists[i+1], fill = 'green')
        except:
            line = canvas.create_line(lists[i], lists[0], fill = 'green')

draw(box)
draw(shape)
root.mainloop()
