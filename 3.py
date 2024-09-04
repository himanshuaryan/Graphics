import turtle as tt
tt.getscreen()
        
tt.bgcolor("black")
tt.speed(0)
tt.pensize(3)

for i in range(1,1000):
        tt.right(10)
        tt.color("red","white")
        tt.circle(i)
        tt.color("yellow","white")
        tt.bk(100)
        tt.fd(i+i)
        tt.right(270)
     
tt.mainloop()
