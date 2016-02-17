"""Beemodoro
Pomodoro app that updates your Beeminder logs.

NOT: Not functional.

TODO
----

[X] Show Timer
[ ] Start Timer
[X] Count-down timer
[ ] Stop timer / Forfeit Timer
[ ] Ding when complete
[ ] Set goal / intention
[ ] Post to Beeminder
[ ] Pull from Beeminder for category list
"""

import tkinter

SECONDS_PER_MINUTE = 60
DEFAULT_TIMER_LENGTH = 25 * SECONDS_PER_MINUTE
DEFAULT_BREAK_LENGTH = 5 * SECONDS_PER_MINUTE

#Temporarily Update
DEFAULT_TIMER_LENGTH = 5
DEFAULT_BREAK_LENGTH = 3

class Beemodoro:

    def __init__(self, master):
        self.master = master

        self.mainframe = tkinter.Frame(self.master, bg="white")
        self.mainframe.pack(fill=tkinter.BOTH, expand=True)

        self.time_left = DEFAULT_TIMER_LENGTH

        self.timer_text = tkinter.StringVar()
        self.timer_text.set(self.MM_SS(self.time_left))

        self.build_grid()
        self.build_timer()

        self.update()

    def MM_SS(self, seconds):
        """Converts 60 seconds to '01:00' """

        min = seconds // SECONDS_PER_MINUTE  # Integer division
        sec = seconds % SECONDS_PER_MINUTE  # Remainder

        return '{:0>2}:{:0>2}'.format(min, sec)


    def build_grid(self):
        """Controls the building of the grid.

        weight 0: don't resize
        weight 1: resize proportionally
        """

        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=0)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=0)

    def build_timer(self):
        timer = tkinter.Label(
            self.mainframe,
            text=self.timer_text.get(),
            font=('Helvetica', 36)
        )
        timer.grid(row=1, column=0, sticky='nsew')

    def update(self):
        """Updates the timer every second."""

        print("Update.")

        #Countdown the time
        self.time_left -= 1
        if self.time_left < 0:
            self.time_left = 0

        #Update the timer text
        self.timer_text.set(self.MM_SS(self.time_left))
        self.build_timer()

        #Repeat every second
        self.master.after(1000, self.update)

if __name__ == '__main__':
    root = tkinter.Tk() #Primary Dialog
    beemodoro = Beemodoro(root)
    root.mainloop()