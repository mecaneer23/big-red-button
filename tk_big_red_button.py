#!/usr/bin/env python3
# pylint: disable=missing-module-docstring, missing-function-docstring

from functools import partial
from tkinter import StringVar
from customtkinter import CTk, CTkButton


def increment(counter: StringVar) -> None:
    counter.set(int(counter.get()) + 1)


def main() -> None:
    root = CTk()
    root.title("Big Red Button")
    counter = StringVar(value="0")
    button = CTkButton(
        root,
        textvariable=counter,
        command=partial(increment, counter),
        fg_color="red",
        hover=False,
        width=750,
        height=750,
        corner_radius=375,
        font=("", -150),
    )
    button.pack()
    root.mainloop()


if __name__ == "__main__":
    main()

# TODO:
# animate press
# avoid stretching when additional digits are added (ie 10, 100, 1000)
