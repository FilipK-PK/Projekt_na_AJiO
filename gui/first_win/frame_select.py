""" frame_select.py """
from gui.first_win import first_win

import tkinter as tk


COLUMN_CONTEXT = 0
COLUMN_CONTEXT_SIZE = 0
COLUMN_ENTRY = 2
EPOCH_IND = 1
IS_EPOCH = 2
NULL = 0


class FrameSelect:
    """ Klasa wyswietlajaca opcej do przeszukiwania najlepszego modelu """

    def __init__(self, win):
        """ Definiowanie zmiennych klasy """
        self.__win = win
        self.__radio_select = tk.StringVar()
        self.__epoch_all = None
        self.__index_select = None

    def create(self) -> None:
        """ Tworzenie i wstawianie ramki selekcji na ekram """
        frame = tk.LabelFrame(
            self.__win, text=first_win.SELECT_WIN['title'],
            font=first_win.FONT_FRAME
        )

        frame.place(
            width=first_win.WIDTH_RADIO_BUTTON, x=first_win.CENTER_RADIO_BUTTON,
            y=first_win.SELECT_WIN['y']
        )

        for i, name in enumerate(first_win.SELECT_WIN['option']):
            tk.Radiobutton(
                frame, text=name, font=first_win.FONT_TEXT,
                value=i + first_win.RADIO_BUTTON_BIAS,
                variable=self.__radio_select,
                command=self.__click_select
            ).grid(row=i, column=COLUMN_CONTEXT, sticky=tk.W)

            if i == EPOCH_IND:
                tk.Label(
                    frame, text=first_win.SELECT_WIN['title_epoch'],
                    font=first_win.FONT_TEXT
                ).grid(row=i, column=COLUMN_CONTEXT_SIZE)

                self.__epoch_all = tk.Entry(
                    frame, width=first_win.SELECT_WIN['width_epoch']
                )

                self.__epoch_all.grid(row=i, column=COLUMN_ENTRY, sticky=tk.W)

    def get_epoch(self) -> str:
        """ Zwraca indeks zaznaczonej opcji z liczba epok """
        return (
            self.__epoch_all.get() if self.__index_select == IS_EPOCH else NULL
        )

    def get_check(self) -> int:
        """ Zwraca index zaznaczonej opcji """
        return self.__index_select

    def __click_select(self) -> None:
        """ Zapisuje zaznaczona opcje podczas klikniecia"""
        self.__index_select = int(self.__radio_select.get())
