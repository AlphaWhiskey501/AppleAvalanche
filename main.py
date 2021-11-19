#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "pear.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()

a = trtl.Turtle()


#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def drop():
  apple.penup()
  apple.goto(0,-200)
  apple.pendown()

def draw_an_A():
  a.color("blue")
  a.write("A", font=("Arial", 55, "bold"))
  drop()

#-----function calls-----

a.hideturtle() 
draw_apple(apple)
wn.bgpic("background.gif")
a.color("white")
a.penup()
a.goto(-22,-45)
a.pendown()
a.write("A", font=("Arial", 55, "bold"))



wn.onkeypress(draw_an_A, "a")

wn.listen()

wn.mainloop()