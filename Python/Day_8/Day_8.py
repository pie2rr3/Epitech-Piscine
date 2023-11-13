#Task_01
import numpy as np
import matplotlib.pyplot as plt
import math

# x_values = np.linspace (0,10, 1000)
# print(x_values)

#Task_02


# x = [0, 1, 2, 3]
# y = [12, 32, 42, 52]
# plt.scatter(x, y)

#ou

# plt.plot([0,1,2,3],[12,32,42,52],"ro")
# plt.show()

#Task_03

# def pointeur_TK78(x,y):
#     plt.plot(x,y,"ro")
#     plt.show()

# pointeur_TK78(0,12)

#Task_04

# import matplotlib.pyplot as plt
# import numpy as np
# import math
# import tkinter as tk

# def f(x):
#     return x**2+x*3+2

# def plot_fct(fct,min,max):
#     x=np.linspace(min,max,1000)
#     y=[]
#     for i in range(len(x)):
#         y.append(fct(x[i]))
#     plt.plot(x,y)
#     plt.grid(True)
#     plt.show()

#Task_01

# import tkinter as tk
# from tkinter import ttk

# Tk_78 = tk.Tk()
# all_entries = []

# def addBox():
#     print ("ADD")

#     ent = tk.Entry(Tk_78)
#     ent.pack()

#     all_entries.append(ent)

# entry = tk.Entry()
# entry.pack()
# all_entries.append(entry)

# def showEntries():

#     for number, ent in enumerate(all_entries):
#         print (number, ent.get().upper())

# showButton = tk.Button(Tk_78, text='Clique moi sal cliqueur', command=showEntries)
# showButton.pack()

# Tk_78.mainloop()

#Task_02

# from tkinter import *

# Tk_78 = Tk()
# all_entries = []

# def addBox():
#     print ("ADD")

#     ent = Entry(Tk_78)
#     ent.pack()

#     all_entries.append(ent)
    
# def showEntries():

#     for number, ent in enumerate(all_entries):
#         print (number, ent.get().upper())

# entry = Entry()
# entry.pack()
# all_entries.append(entry)

# showButton = Button(Tk_78, text='Clique moi sal cliqueur', command=showEntries)
# showButton.pack()

# bg = PhotoImage(file = "rire.png")
# Label(Tk_78, image = bg).pack()

# Tk_78.mainloop()

#Task_03

# from tkinter import *

# window = Tk()
# window.geometry('600x400')
# window.title("Canvas")

# canvas = Canvas(window, bg = 'white')
# canvas.pack()

# canvas.create_oval((125, 50, 175, 100), fill ="lightgreen")

# canvas.create_line((150, 110, 200, 160), fill ="blue")
# canvas.create_line((150, 110, 100, 160), fill ="red")
# canvas.create_line((150, 100, 150, 200), fill ="orange")
# canvas.create_line((150, 200, 200, 250), fill ="yellow")
# canvas.create_line((150, 200, 100, 250), fill ="green")

# window.mainloop()

#Task_04

# import tkinter as tk

# def animate_arms():
#     # Met à jour les coordonnées du bras gauche
#     canvas.coords(left_arm, 150, 150, 200, 75)
#     # Met à jour les coordonnées du bras droit
#     canvas.coords(right_arm, 150, 150, 100, 75)
#     # Appelle la fonction animate_arms après 100 millisecondes
#     root.after(1000, reset_arms)

# def reset_arms():
#     # Rétablit les coordonnées du bras gauche à la position initiale
#     canvas.coords(left_arm, 150, 150, 200, 225)
#     # Rétablit les coordonnées du bras droit à la position initiale
#     canvas.coords(right_arm, 150, 150, 100, 225)
#     # Appelle la fonction animate_arms après 100 millisecondes
#     root.after(1000, animate_arms)

# root = tk.Tk()
# root.title("Stickman Figure")

# canvas = tk.Canvas(root, width=300, height=300)
# canvas.pack()

# head = canvas.create_oval(125, 75, 175, 125, outline="black", fill="chartreuse1")

# body = canvas.create_line(150, 125, 150, 225, fill="green", width=3)

# left_arm = canvas.create_line(150, 150, 200, 225, fill="blue", width=3)

# right_arm = canvas.create_line(150, 150, 100, 225, fill="red", width=3)

# left_leg = canvas.create_line(150, 225, 100, 300, fill="purple", width=3)

# right_leg = canvas.create_line(150, 225, 200, 300, fill="yellow", width=3)

# text = canvas.create_text(100, 50, text="Hello World!", font=("Arial", 12), fill="black")


# animate_arms()

# root.mainloop()

#Challenge

#Task_00

# import tkinter as tk
# import random
# import time

# # Constants
# WIDTH, HEIGHT = 400, 400
# SNAKE_SIZE = 20
# SPEED = 0.1

# # Initialize the window
# root = tk.Tk()
# root.title("Snake Game")

# # Canvas for drawing
# canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
# canvas.pack()

# # Initialize game variables
# snake = [(100, 100), (80, 100), (60, 100)]
# food = (200, 200)
# score = 0
# lives = 3

# # Create initial direction
# direction = "Right"

# # Functions
# def draw_snake():
#     for segment in snake:
#         canvas.create_rectangle(segment[0], segment[1], segment[0] + SNAKE_SIZE, segment[1] + SNAKE_SIZE, fill="green")

# def move_snake():
#     global direction, food, score, lives

#     head_x, head_y = snake[0]
#     if direction == "Up":
#         new_head = (head_x, head_y - SNAKE_SIZE)
#     elif direction == "Down":
#         new_head = (head_x, head_y + SNAKE_SIZE)
#     elif direction == "Left":
#         new_head = (head_x - SNAKE_SIZE, head_y)
#     else:
#         new_head = (head_x + SNAKE_SIZE, head_y)

#     snake.insert(0, new_head)

#     # Check for collisions
#     if snake[0] == food:
#         score += 10
#         food = (random.randint(0, (WIDTH-SNAKE_SIZE)//SNAKE_SIZE) * SNAKE_SIZE, random.randint(0, (HEIGHT-SNAKE_SIZE)//SNAKE_SIZE) * SNAKE_SIZE)
#     else:
#         snake.pop()

#     # Check if the snake hits the wall
#     if (snake[0][0] < 0 or snake[0][0] >= WIDTH or
#             snake[0][1] < 0 or snake[0][1] >= HEIGHT):
#         lives -= 1
#         reset_game()

#     # Check if the snake collides with itself
#     if len(snake) > 1 and snake[0] in snake[1:]:
#         lives -= 1
#         reset_game()

#     canvas.delete("all")
#     draw_snake()
#     canvas.create_rectangle(food[0], food[1], food[0] + SNAKE_SIZE, food[1] + SNAKE_SIZE, fill="red")
#     canvas.create_text(50, 10, text=f"Score: {score}", anchor="nw")
#     canvas.create_text(150, 10, text=f"Lives: {lives}", anchor="nw")
#     canvas.create_text(250, 10, text=f"Time: {int(time.time() - start_time)}", anchor="nw")

#     if lives > 0:
#         canvas.after(int(SPEED * 1000), move_snake)
#     else:
#         canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", font=("Helvetica", 24))
#         canvas.create_text(WIDTH // 2, HEIGHT // 2 + 30, text=f"Your Score: {score}", font=("Helvetica", 18))

# def reset_game():
#     global snake, food, direction, score
#     snake = [(100, 100), (80, 100), (60, 100)]
#     food = (200, 200)
#     direction = "Right"
#     score = 0  # Clear the canvas
#     draw_snake()

# def change_direction(new_direction):
#     global direction
#     if new_direction == "Left" and direction != "Right":
#         direction = new_direction
#     elif new_direction == "Right" and direction != "Left":
#         direction = new_direction
#     elif new_direction == "Up" and direction != "Down":
#         direction = new_direction
#     elif new_direction == "Down" and direction != "Up":
#         direction = new_direction

# # Create a menu button
# menu_button = tk.Button(root, text="Reset", command=reset_game)
# menu_button.pack()

# # Bind arrow keys to change direction
# root.bind("<Left>", lambda e: change_direction("Left"))
# root.bind("<Right>", lambda e: change_direction("Right"))
# root.bind("<Up>", lambda e: change_direction("Up"))
# root.bind("<Down>", lambda e: change_direction("Down"))

# # Start the game
# start_time = time.time()
# move_snake()

# root.mainloop()

#Task_01




    




    
    
    
    
    
    
