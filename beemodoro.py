"""Beemodoro
Pomodoro app that updates your Beeminder logs.

NOT: Not functional.

TODO
----

[ ] Show Timer
[ ] Start Timer
[ ] Count-down timer
[ ] Stop timer / Forfeit Timer
[ ] Ding when complete
[ ] Set goal / intention
[ ] Post to Beeminder
[ ] Pull from Beeminder for category list
"""

import tkinter

class Beemodoro:

    def __init__(self, master):
        self.master = master

        self.frame = tkinter.Frame(master)
        self.frame.pack()

        self.button = tkinter.Button(
            self.frame, text="QUIT", fg="red", command=self.frame.quit
            )
        self.button.pack(side=tkinter.LEFT)

        self.hi_there = tkinter.Button(self.frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=tkinter.LEFT)

    def say_hi(self):
        print("hi there, everyone!")

if __name__ == '__main__':
    root = tkinter.Tk() #Primary Dialog

    beemodoro = Beemodoro(root)

    root.mainloop()
    root.destroy()