""" frame_type.py """
from gui.first_win import first_win

import tkinter as tk


class FrameType:
    """ Klasa wyswietla ramke z wyborem sieci """

    def __init__(self, win):
        """ Definiowanie zmiennych klasy """
        self.__win = win
        self.__radio_type = tk.StringVar()
        self.__index_typ = None

    def create(self) -> None:
        """ Tworzenie i wstawianie na ekran ramki z typani """
        frame = tk.LabelFrame(
            self.__win, text=first_win.TYPE_MODEL['title'],
            font=first_win.FONT_FRAME,
        )

        frame.place(
            width=first_win.WIDTH_RADIO_BUTTON, x=first_win.CENTER_RADIO_BUTTON,
            y=first_win.TYPE_MODEL['y']
        )

        for i, name in enumerate(first_win.TYPE_MODEL['option']):
            tk.Radiobutton(
                frame, text=name, font=first_win.FONT_TEXT,
                value=i + first_win.RADIO_BUTTON_BIAS, variable=self.__radio_type,
                command=self.__click
            ).pack(anchor=tk.W)

    def get_check(self) -> int:
        """ Zwraca index wybranej opcji """
        return self.__index_typ

    def __click(self) -> None:
        """ Zapisuje index wybranej opcji """
        self.__index_typ = int(self.__radio_type.get())
