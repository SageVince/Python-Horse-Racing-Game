import turtle
import random
import tkinter as tk
from tkinter import messagebox

class HorseRacingGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Horse Racing Game")
        self.window.geometry("400x300")
        self.race_count = 0
        self.racers = 0
        self.turtles = []
        self.create_widgets()

    def create_widgets(self):
        self.race_label = tk.Label(self.window, text="Races:")
        self.race_label.pack()
        self.race_entry = tk.Entry(self.window)
        self.race_entry.pack()
        self.race_button = tk.Button(self.window, text="Start Racing", command=self.start_racing)
        self.race_button.pack()
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

    def start_racing(self):
        try:
            self.race_count = int(self.race_entry.get())
            if self.race_count > 20:
                messagebox.showerror("Error", "Too many consecutive races. Maximum is 20.")
                return
            self.racers = int(input("Please enter a number of racers between 2 and 11 (inclusive): "))
            while self.racers < 2 or self.racers > 11:
                self.racers = int(input("Please enter a number between 2 and 11 (inclusive): "))
            self.turtles = []
            for p in range(self.racers):
                x = turtle.Turtle()
                if p == 0:
                    x.up()
                    x.setpos(-250, 0)
                    x.down()
                elif p % 2 == 0:
                    x.up()
                    x.setpos(-250, 25 * (p // 2))
                    x.down()
                elif p % 2 == 1:
                    x.up()
                    x.setpos(-250, -(25 * ((p + 1) // 2)))
                    x.down()
                pen = p
                fill = -(p + 1)
                if pen > 6:
                    pen = p - 5
                    fill = fill + 7
                x.color(["black", "red", "hotpink", "purple", "blue", "green", "cyan"][pen], ["black", "red", "hotpink", "purple", "blue", "green", "cyan"][fill])
                self.turtles.append(x)
            self.race()

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

    def race(self):
        for i in range(self.race_count):
            for turtle in self.turtles:
                turtle.forward(5)
            winner = random.randint(0, len(self.turtles) - 1)
            winner_turtle = self.turtles[winner]
            winner_color = str(winner_turtle.fillcolor())
            winner_horse = str(winner_turtle.pencolor())
            winner_turtle.right(1080)
            self.result_label.config(text=f"The {winner_horse} horse wins!")
            self.window.update()
            self.window.after(1000)
        self.window.destroy()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = HorseRacingGame()
    game.run()
