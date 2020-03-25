'''
Для этого кода есть несколько улучшений:
	1) Диаметр шара привязать к размеру доски и ширине экрана
	2) Соеденить 4 функции для проверки победы в одну
	3) Провека победы не по всем клеткам игры, а только на основании той, в которой игрок поставил шар -> уменьшении сложности алогитма 
'''

from tkinter import *
import tkinter as tk

WINDOWS_WIDTH = 800		#px
WINDOWS_HEIGHT = 600	#px	

GAME_HEIGHT = 6		#blocks
GAME_WIDHT = 7		#blocks
PLAYERS_AMOUNT = 2	#less then 4, or add a new colour to the colour list
players_colours = ["red", "yellow", "green", "blue"]

class Circle(object):
	def __init__(self, x, y, empty=True, colour="white"):
		self.x = x
		self.y = y
		self.colour = colour
		field.create_oval(self.x+10, self.y+10, self.x+61, self.y+61, fill=colour)


	def change_colour(self, colour):
		self.colour = colour
		field.create_oval(self.x+10, self.y+10, self.x+61, self.y+61, fill=colour)



class Field(Canvas):
	def __init__(self):
		self.player_colour = players_colours[0]
		self.player = 0
		self.circles_list = []
		self.game = True
		for i in range(0, WINDOWS_HEIGHT, int(WINDOWS_HEIGHT/GAME_HEIGHT)):
			circles = []
			for j in range(0, WINDOWS_WIDTH, int(WINDOWS_WIDTH/GAME_WIDHT)):
				circles.append(Circle(j, i ,self))

			self.circles_list.append(circles)

		field.bind("<Button-1>", self.set_circle)
		print("Player - ", self.player+1, " move")

	def set_circle(self, event):
		if self.game:
			column = int(event.x/WINDOWS_WIDTH*GAME_WIDHT)
			circle_num = 0

			while circle_num < len(self.circles_list):
				if self.circles_list[0][column].colour in players_colours:
					break

				if self.circles_list[circle_num][column].colour in players_colours:
					self.circles_list[circle_num-1][column].change_colour(self.player_colour)
					break

				elif circle_num == len(self.circles_list)-1:
					self.circles_list[circle_num][column].change_colour(self.player_colour)
					break
				circle_num+=1

			self.player += 1
			if self.player == PLAYERS_AMOUNT:
				self.player = 0
				self.player_colour = players_colours[0]
			self.player_colour = players_colours[self.player]
			print("Player - ", self.player+1, " move")


			self.row_win()
			self.col_win()
			self.diagonal_left_win()
			self.diagonal_right_win()

	def row_win(self):
		i = 0
		while(i < len(self.circles_list)):
			j = 0
			while(j < 3):
				if(self.circles_list[i][j].colour == self.circles_list[i][j+1].colour == self.circles_list[i][j+2].colour == self.circles_list[i][j+3].colour):
					if self.circles_list[i][j].colour != "white":
						print("Player - ", players_colours.index(self.circles_list[i][j].colour)+1, " wins!")
						self.game = False
						break
				j +=1
			i += 1

	def col_win(self):
		i = 0
		while(i < 3):
			j = 0
			while(j < len(self.circles_list[i])):
				if(self.circles_list[i][j].colour == self.circles_list[i+1][j].colour == self.circles_list[i+2][j].colour == self.circles_list[i+3][j].colour):
					if self.circles_list[i][j].colour != "white":
						print("Player - ", players_colours.index(self.circles_list[i][j].colour)+1, " wins")
						self.game = False
						break
				j+=1
			i+=1

	def diagonal_left_win(self):
		i = 0
		while(i < 3):
			j = 0
			while(j < 3):
				if(self.circles_list[i][j].colour == self.circles_list[i+1][j+1].colour == self.circles_list[i+2][j+2].colour == self.circles_list[i+3][j+3].colour):
					if self.circles_list[i][j].colour != "white":
						print("Player - ", players_colours.index(self.circles_list[i][j].colour)+1, " wins")
					
						self.game = False
						break
     
				j += 1
			i += 1


	def diagonal_right_win(self):
		i = 0
		while(i < 3):
			j = len(self.circles_list[i])-1
			while(j > len(self.circles_list)-4):
				if(self.circles_list[i][j].colour == self.circles_list[i+1][j-1].colour == self.circles_list[i+2][j-2].colour == self.circles_list[i+3][j-3].colour):
					if self.circles_list[i][j].colour != "white":
						print("Player - ", players_colours.index(self.circles_list[i][j].colour)+1, " wins")
					
						self.game = False
						break
              
				j -= 1
			i += 1






        



root = Tk()
field = Canvas(root, width=WINDOWS_WIDTH, height=WINDOWS_HEIGHT+50, bg="#ffffff")
field.grid()

game = Field()



root.mainloop()
