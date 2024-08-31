import turtle as tt
import random as rnd

num = rnd.randint(0,11)
color = ["red","green","blue","lightslategrey","lightblue","pink","brown","orange","purple","gold","white","teal","yellow"]
choice= color[num]
tt.getscreen()

def random_color(list, count): # count is the no. of color in list.
    for c in list:
        num = rnd.randint(0,count)
        return list[num]
        
tt.bgcolor("black")
tt.speed(0)
tt.pensize(3)

for i in range(1,1000):
        rc = random_color(color,11)
        tt.right(10)
        tt.circle(i+8)
        tt.pencolor(rc)
        tt.bk(100)
        tt.right(270)
     
tt.mainloop()
