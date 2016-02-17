"""Beemodoro
Pomodoro app that updates your Beeminder logs.

NOT: Not functional.

TODO
----

[X] Show Timer
[ ] Start Timer
[ ] Count-down timer
[ ] Stop timer / Forfeit Timer
[ ] Ding when complete
[ ] Set goal / intention
[ ] Post to Beeminder
[ ] Pull from Beeminder for category list
"""

import tkinter

SECONDS_PER_MINUTE = 60
DEFAULT_TIMER_LENGTH = 25 * SECONDS_PER_MINUTE

class Beemodoro:

    def __init__(self, master):
        self.master = master

        self.mainframe = tkinter.Frame(self.master, bg="white")
        self.mainframe.pack(fill=tkinter.BOTH, expand=True)

        self.timer_text = tkinter.StringVar()
        self.timer_text.set(self.seconds_to_time_string(DEFAULT_TIMER_LENGTH))

        self.build_grid()
        self.build_timer()

    def seconds_to_time_string(self, seconds):
        """Converts 60 to '01:00' """

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

if __name__ == '__main__':
    root = tkinter.Tk() #Primary Dialog
    beemodoro = Beemodoro(root)
    root.mainloop()