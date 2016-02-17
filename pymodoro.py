"""beemodoro v0.01
A pomodoro app that auto-posts data to Beeminder.

Author: Donovan Keith
"""

import tkinter
from tkinter import messagebox

DEFAULT_TIMER_LENGTH = 60 * 25  # 25 minutes
DEFAULT_TIMER_LENGTH = 5


class Pymodoro:
    def __init__(self, master):
        """
        :param master: Master window / process
        :return:
        """

        # Dialog Variables
        self.master = master
        self.mainframe = tkinter.Frame(self.master, bg="white")
        self.mainframe.pack(fill=tkinter.BOTH, expand=True)

        # Timer Variables
        self.timer_text = tkinter.StringVar()
        self.timer_text.trace('w', self.build_timer) #Whenever this is written to, call build_timer

        self.time_left = tkinter.IntVar()  # Number of seconds left.
        self.time_left.set(DEFAULT_TIMER_LENGTH)
        self.time_left.trace('w', self.alert)

        self.timer_running = False

        # Create the Layout
        self.build_grid()
        self.build_banner()
        self.build_buttons()
        self.build_timer()

        self.update()

    def build_grid(self):
        """Controls the building of the grid.

        weight 0: don't resize
        weight 1: resize proportionally
        """

        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=0)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=0)


    def build_banner(self):
        """Adds a red 'Beemodoro' banner at the top of the window."""

        banner = tkinter.Label(
            self.mainframe,
            background='red',
            text='Beemodoro',
            fg='white',
            font=('Helvetica', 24)
        )

        banner.grid(
            row=0,
            column=0,
            sticky='ew',  # East / West
            padx=10,
            pady=10
        )

    def build_buttons(self):
        """Adds [Start] [Stop] buttons to bottom row of mainframe."""

        # Create a frame w/ two equally-sized columns for the buttons [  |  ]
        buttons_frame = tkinter.Frame(self.mainframe)
        buttons_frame.grid(row=2, column=0, sticky='nsew', pady=10)
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)

        # Create the Start/Stop buttons
        self.start_button = tkinter.Button(
            buttons_frame,
            text='Start',
            command=self.start_timer
        )

        self.stop_button = tkinter.Button(
            buttons_frame,
            text='Stop',
            command=self.stop_timer
        )

        # Insert the buttons
        self.start_button.grid(row=0, column=0, sticky='ew')
        self.stop_button.grid(row=0, column=1, sticky='ew')

        # Ensure Stop Button is disabled at the start.
        self.stop_button.config(state=tkinter.DISABLED)

    def build_timer(self, *args):
        """Draw timer on Screen
        """
        timer = tkinter.Label(
            self.mainframe,
            text=self.timer_text.get(),
            font=('Helvetica', 36)
        )
        timer.grid(row=1, column=0, sticky='nsew')

    def start_timer(self):
        """Starts the timer."""

        self.time_left.set(DEFAULT_TIMER_LENGTH)
        self.timer_running = True

        self.stop_button.config(state=tkinter.NORMAL)
        self.start_button.config(state=tkinter.DISABLED)

    def stop_timer(self):
        """Stops the timer."""

        self.timer_running = False

        self.stop_button.config(state=tkinter.DISABLED)
        self.start_button.config(state=tkinter.NORMAL)

    def minutes_seconds(self, seconds):
        """Converts seconds to a minutes/seconds string."""

        min, sec = int(seconds / 60), int(seconds % 60)

        return '{:0>2}:{:0>2}'.format(min, sec)

    def alert(self, *args):
        if not self.time_left.get():
            messagebox.showinfo('Beemodoro', 'Your timer is done!')

    def update(self):
        time_left = self.time_left.get()

        if self.timer_running and time_left:
            self.time_left.set(time_left-1)
            self.timer_text.set(
                self.minutes_seconds(time_left)
            )
        else:
            self.stop_timer()
            self.timer_text.set(
                self.minutes_seconds(DEFAULT_TIMER_LENGTH)
            )

        self.master.after(1000, self.update)

# Only create dialog if it's being run as it's own script
if __name__ == '__main__':
    root = tkinter.Tk()
    Pymodoro(root)
    root.mainloop()