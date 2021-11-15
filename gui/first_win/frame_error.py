""" frame_error.py """
from gui.first_win import first_win

import tkinter as tk


EMPTY = ''


class FrameError:
    """ Klasa wyswietlajaca wykryte błedy """

    def __init__(self, win):
        """ Definiowanie zmiennych klasy """
        self.__win = win
        self.__text_error = tk.StringVar()
        self.__text_error.set(EMPTY)

    def create(self) -> None:
        """ Tworzeniae ramki wyswietlajacej bład """
        frame = tk.Label(
            self.__win, font=first_win.FONT_TEXT,
            fg=first_win.ERROR_WIN['color'],
            textvariable=self.__text_error
        )

        frame.place(
            width=first_win.WIDTH_RADIO_BUTTON,
            x=first_win.CENTER_RADIO_BUTTON,
            y=first_win.ERROR_WIN['y']
        )

    def set_text_error(self, text) -> None:
        """ Ustawianie tekstu ktury jest wyswietlany """
        self.__text_error.set(text)
