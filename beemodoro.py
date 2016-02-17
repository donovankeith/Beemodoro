"""beemodoro v0.01
A pomodoro app that auto-posts data to Beeminder.

Author: Donovan Keith
"""

import tkinter

class Pymodoro:
    def __init__(self, master):
        """
        :param master: Master window / process
        :return:
        """

        self.master = master
        self.mainframe = tkinter.Frame(self.master, bg="white")
        self.mainframe.pack(fill=tkinter.BOTH, expand=True)

        self.build_grid()
        self.build_banner()
        self.build_buttons()
        self.build_timer()

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
        """Adds a logo banner."""

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
        """Adds buttons."""

        buttons_frame = tkinter.Frame(self.mainframe)
        buttons_frame.grid(row=2, column=0, sticky='nsew', pady=10)
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)

        self.start_button = tkinter.Button(
            buttons_frame,
            text='Start'
        )

        self.stop_button = tkinter.Button(
            buttons_frame,
            text='Stop'
        )

        self.start_button.grid(row=0, column=0, sticky='ew')
        self.stop_button.grid(row=0, column=1, sticky='ew')

    def build_timer(self):
        """Creates a timer."""

        timer = tkinter.Label(
            self.mainframe,
            text='TIMER',
            font=(
                'Helvetica',
                36
            )
        )
        timer.grid(row=1, column=0, sticky='nsew')


#Only create dialog if it's being run as it's own script
if __name__ == '__main__':
    root = tkinter.Tk()

    Pymodoro(root)

    root.mainloop()