import turtle 
import time

wn = turtle.Screen()
wn.title("Unip Flappy Bird")
wn.bgcolor("blue")
wn.bgpic("background.gif")
wn.tracer(0)
#tamanho da tela
wn.setup(width=500, height=800)

#registrando personagem
wn.register_shape("bird.gif")

pen = turtle.Turtle()
pen.speed()
pen.hideturtle()
pen.penup()
pen.color("white")
pen.goto(0,250)
pen.write("0", move=False, align="left", font=("Arial", 32, "normal"))


#jogador
bird = turtle.Turtle()
bird.speed(0)
bird.penup()
bird.color("yellow")
bird.shape("bird.gif")
bird.goto(-200,0)
bird.dx = 0 
bird.dy = 1

#map_tuneis 
tunel_top = turtle.Turtle()
tunel_top.speed(0)
tunel_top.penup()
tunel_top.color("green")
tunel_top.shape("square")
tunel_top.shapesize(stretch_wid=18 , stretch_len=3, outline=None)
tunel_top.goto(300,250)
tunel_top.dx = -2 
tunel_top.dy = 0
tunel_top.value = 1

tunel_bottom = turtle.Turtle()
tunel_bottom.speed(0)
tunel_bottom.penup()
tunel_bottom.color("green")
tunel_bottom.shape("square")
tunel_bottom.shapesize(stretch_wid=18 , stretch_len=3, outline=None)
tunel_bottom.goto(300,-250)
tunel_bottom.dx = -2
tunel_bottom.dy = 0


tunel2_top = turtle.Turtle()
tunel2_top.speed(0)
tunel2_top.penup()
tunel2_top.color("green")
tunel2_top.shape("square")
tunel2_top.shapesize(stretch_wid=18 , stretch_len=3, outline=None)
tunel2_top.goto(600,300)
tunel2_top.dx = -2 
tunel2_top.dy = 0
tunel2_top.value = 1

tunel2_bottom = turtle.Turtle()
tunel2_bottom.speed(0)
tunel2_bottom.penup()
tunel2_bottom.color("green")
tunel2_bottom.shape("square")
tunel2_bottom.shapesize(stretch_wid=18 , stretch_len=3, outline=None)
tunel2_bottom.goto(600,-200)
tunel2_bottom.dx = -2
tunel2_bottom.dy = 0



gravidade = -0.3

#definição de metodo/função 
def go_cima():
    bird.dy += 8

    if bird.dy > 8:
        bird.dy = 8
                
#teclado obrigatorio 
wn.listen()
wn.onkeypress(go_cima,"space")

#inicializaão game variaveis 
bird.score = 0
print("Score: {}".format(bird.score))

#main game loop 
while True:
    
    #Pause
    time.sleep(0.02)
    
    #atualização de tela 
    wn.update()
    
    #adiciona gravidade 
    bird.dy += gravidade
    
    #mover bird
    y = bird.ycor()
    y+= bird.dy
    bird.sety(y)

    #borda de baixo 
    if bird.ycor() < -390:
        bird.dy = 0 
        bird.sety(-390)


    #move_tuneis_1
    x = tunel_top.xcor()
    x += tunel_top.dx
    tunel_top.setx(x)

    x = tunel_bottom.xcor()
    x += tunel_bottom.dx
    tunel_bottom.setx(x)

    #Return pipes to start
    if tunel_top.xcor () < -350:
        tunel_top.setx(350)
        tunel_bottom.setx(350)
        tunel_top.value = 1


       #move_tuneis_2
    x = tunel2_top.xcor()
    x += tunel2_top.dx
    tunel2_top.setx(x)

    x = tunel2_bottom.xcor()
    x += tunel2_bottom.dx
    tunel2_bottom.setx(x)

    #Return pipes to start_2
    if tunel2_top.xcor () < -350:
        tunel2_top.setx(350)
        tunel2_bottom.setx(350)  
        tunel2_top.value = 1


    #colisão dos tuneis
    #tunel_top_1
    if (bird.xcor() + 10 > tunel_top.xcor() -10) and (bird.xcor() - 10 < tunel_top.xcor() + 30):
        if (bird.ycor() + 10 > tunel_top.ycor() - 180) or (bird.ycor() - 30 < tunel_bottom.ycor() + 180):
            pen.clear()
            pen.write("Game Over!",move=False, align="center", font=("Arial", 32, "normal"))
            wn.update()
            time.sleep(3)
            #reset score
            bird.score = 0
            #Mover tuneis de volta
            tunel_top.setx(300)
            tunel_bottom.setx(300)
            tunel_top.setx(600)
            tunel_bottom.setx(600)
            #mover bird de bolta 
            bird.goto(-200,0)
            bird.dy = 0
            pen.clear()


    #checar o score
    if tunel_top.xcor() + 30 < bird.xcor() - 10:
        bird.score += tunel_top.value
        tunel_top.value = 0
        pen.clear()
        pen.write(bird.score, move=False, align="left", font=("Arial", 32, "normal"))
                      

    #colisão dos tuneis
    #tunel_top_2
    if (bird.xcor() + 10 > tunel2_top.xcor() -30) and (bird.xcor() - 10 < tunel2_top.xcor() + 30):
        if (bird.ycor() + 10 > tunel2_top.ycor() - 180) or (bird.ycor() - 30 < tunel2_bottom.ycor() + 180):
            pen.clear()
            pen.write("Game Over!",move=False, align="center", font=("Arial", 32, "normal"))      
            wn.update()
            time.sleep(3)
            #reset score
            bird.score = 0
            #Mover tuneis de volta
            tunel2_top.setx(300)
            tunel2_bottom.setx(300)
            tunel2_top.setx(600)
            tunel2_bottom.setx(600)
            #mover bird de bolta 
            bird.goto(-200,0)
            bird.dy = 0
            #clear placar
            pen.clear()


    #checar o score 2 
    if tunel2_top.xcor() + 30 < bird.xcor() - 10:
        bird.score += tunel2_top.value
        tunel2_top.value = 0
        pen.clear()
        pen.write(bird.score, move=False, align="left", font=("Arial", 32, "normal"))


wn.mainloop()