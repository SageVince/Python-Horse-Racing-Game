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
            self.text_mode = False
            self.create_widgets()

        def create_widgets(self):
            self.menu = tk.Menu(self.window)
            self.window.config(menu=self.menu)
            self.file_menu = tk.Menu(self.menu)
            self.menu.add_cascade(label="File", menu=self.file_menu)
            self.file_menu.add_command(label="New Game", command=self.new_game)
            self.file_menu.add_command(label="Exit", command=self.window.destroy)
            self.file_menu.add_command(label="Switch to Text Mode", command=self.switch_to_text_mode)
            self.file_menu.add_command(label="Switch to Viewable Mode", command=self.switch_to_viewable_mode)

            self.race_label = tk.Label(self.window, text="Races:")
            self.race_label.pack()
            self.race_entry = tk.Entry(self.window)
            self.race_entry.pack()
            self.race_button = tk.Button(self.window, text="Start Racing", command=self.start_racing)
            self.race_button.pack()
            self.result_label = tk.Label(self.window, text="")
            self.result_label.pack()

        def new_game(self):
            self.race_count = 0
            self.racers = 0
            self.turtles = []
            self.create_widgets()

        def switch_to_text_mode(self):
            self.text_mode = True
            self.window.destroy()
            self.text_game()

        def switch_to_viewable_mode(self):
            self.text_mode = False
            self.window.destroy()
            self.viewable_game()

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
                if self.text_mode:
                    self.text_game()
                else:
                    self.viewable_game()

            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

        def text_game(self):
            print("Welcome to the Horse Racing Game!")
            print("You will be prompted to enter the number of races and the number of racers.")
            print("The game will then simulate the races and print the results.")
            print("Let's start!")
            self.race_count = int(input("Please enter the number of races: "))
            self.racers = int(input("Please enter the number of racers: "))
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
            for i in range(self.race_count):
                for turtle in self.turtles:
                    turtle.forward(5)
                winner = random.randint(0, len(self.turtles) - 1)
                winner_turtle = self.turtles[winner]
                winner_color = str(winner_turtle.fillcolor())
                winner_horse = str(winner_turtle.pencolor())
                winner_turtle.right(1080)
                print(f"The {winner_horse} horse wins!")

        def viewable_game(self):
            self.window = tk.Tk()
            self.window.title("Horse Racing Game")
            self.window.geometry("400x300")
            self.race_count = 0
            self.racers = 0
            self.turtles = []
            self.create_widgets()
            self.window.mainloop()

        def run(self):
            self.window.mainloop()

    if __name__ == "__main__":
        game = HorseRacingGame()
        game.run()
