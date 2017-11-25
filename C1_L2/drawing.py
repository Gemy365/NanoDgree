import turtle                   #Best Lib For Drawing

#def draw_Square(some_turtle):          #Function
#    for i in range(1,5):               #Loop From 1 To End-1 [4]
#        some_turtle.forward(100)       #Draw Line forward 100 & Stop There
#        some_turtle.right(90)          #New Angle Is   90  right
def draw_Triangle(some_info):
    for i in range(1,4):              #Loop From 1 To End-1 [3]
        some_info.backward(350)       #Draw Line backward 350 & Stop There
        if i is 2:                    #if i == 2
            some_info.goto(0,0)       #Goto Point (0,0)
            break                     #Stop This Loop
        else:
            some_info.left(135)       #New Angle Is   135  left

def draw_art():
#Create Window Screen
    window = turtle.Screen()    #For Window Screen
    window.bgcolor("black")     #Bage Color Is White
#Drow The square Shape
#    brad = turtle.Turtle()      #Turtle Class
#    brad.shape("turtle")        #Shape turtle for Drawing [Shapes: “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”]
#    brad.color("red")           #Color Of A Shape Is red
#    brad.speed(4)               #Speed Of A Shape Is 4
#    for i in range(1,37):       #Loop From 1 To End-1 [36] To make Circle By This Shape
#        draw_Square(brad)       #Call draw_Square Function
#        brad.right(10)          #New Angle Is   [Old Angel + 10]  right
#Drow The Circle Shape
#    circle = turtle.Turtle()    #New Class For New Shape
#    circle.shape("arrow")       #Shape arrow For Drawing
#    circle.color("blue")        #Color Of A New Shape
#    circle.circle(100)          #Diagonal Of The circle
#Drow The Triangle Shape
    triangle = turtle.Turtle()  #New Class For New Shape
    triangle.shape("circle")    #Shape circle For Drawing
    triangle.color("white")      #Color Of A New Shape
    triangle.speed(5)           #Speed Of A Shape Is 4
    for i in range(1,15):       #Loop From 1 To End-1 [36] To make Circle By This Shape
        draw_Triangle(triangle) #Call draw_Triangle Function
        triangle.left()       #New Angle Is   [Old Angel + 50]  left
    window.exitonclick()        #Exit The Screen When Click On It

draw_art()                   #Call The Function
