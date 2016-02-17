"""Beemodoro
Pomodoro app that updates your Beeminder logs.

NOT: Not functional.

TODO
----

[X] Show Timer
[ ] Start Timer
[X] Count-down timer
[ ] Single start/stop button
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

#States
STATE_RUNNING = 1
STATE_STOPPED = 2

#Modes
MODE_TIMER = 1
MODE_BREAK = 2

class Beemodoro:

    def __init__(self, master):
        self.master = master

        self.mainframe = tkinter.Frame(self.master, bg="white")
        self.mainframe.pack(fill=tkinter.BOTH, expand=True)

        self.state = STATE_STOPPED
        self.mode = MODE_TIMER

        self.time_left = tkinter.IntVar()
        self.time_left.set(DEFAULT_TIMER_LENGTH)

        self.timer_text = tkinter.StringVar()
        self.timer_text.set(self.MM_SS(self.time_left.get()))

        self.build_grid()
        self.build_timer()
        self.build_buttons()

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

    def build_buttons(self):
        """Adds [Start] [Stop] buttons to bottom row of mainframe."""

        # Create the Start/Stop buttons
        self.start_stop_button = tkinter.Button(
            self.mainframe,
            text='Start',
            command=self.start_stop
        )

        # Insert the buttons
        self.start_stop_button.grid(row=2, column=0, sticky='s')

    def start_stop(self):
        """
        States:
        Just opened, nothing started.
        Timer running
        Timer Paused
        Timer stopped (restart)
        Break running
        Break paused
        Break stopped
        Set next task
        """

        if self.state == STATE_STOPPED:
            print("Start!")
            self.state = STATE_RUNNING
            self.start_stop_button.config(text="Stop")
        elif self.state == STATE_RUNNING:
            print("Stop!")
            self.state = STATE_STOPPED
            self.start_stop_button.config(text="Start")

    def update(self):
        """Updates the timer every second."""

        print("Update.")

        #Countdown the time
        self.time_left.set(self.time_left.get() - 1)
        if self.time_left.get() < 0:
            self.time_left.set(0)

        #Update the timer text
        self.timer_text.set(self.MM_SS(self.time_left.get()))
        self.build_timer()

        #Repeat every second
        self.master.after(1000, self.update)

if __name__ == '__main__':
    root = tkinter.Tk() #Primary Dialog
    beemodoro = Beemodoro(root)
    root.mainloop()