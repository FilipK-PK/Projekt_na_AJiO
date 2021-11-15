""" frame_options.py """
from gui.first_win import first_win

import tkinter as tk


TITLE = 'Początkowe opcje uczące'
TEXT_POINT_LEARNING_RATE = 'Podaj skoki uczenia, liczby podaj odzielone ","'
TEXT_POINT_OPTYMAIZEL = 'Zaznacz optymalizatory'
OPTION_OPTYMAIZEL = ['Adam', 'RMSprop', 'SGD']
LEN_CHECK_BOX = 3
ENTRY_LEN = 25
ON, OFF = 1, 0
PAD_X, PAD_Y = 3, 2
MARGIN_X = 10
INDEX = {'lr_cont_y': 0, 'lr_cont_x': 0,
         'lr_answ_y': 0, 'lr_answ_x': 1,
         'opt_cont_y': 1, 'opt_cont_x': 0,
         'opt_answ_y': 1, 'opt_answ_x': 1}


class FrameOption:
    """ Klasa wyswietla i pobiera informacje o optymalizacji modelu """

    def __init__(self, win):
        """ Definiowanie zmiennych klasy """
        self.__win = win
        self.__frame = None
        self.__learning_rates = None
        self.__opt = [tk.IntVar() for _ in range(LEN_CHECK_BOX)]

    def create_option(self) -> tk.LabelFrame:
        """ Zwraca stworzana ramke do pobierania danych """
        self.__frame = tk.LabelFrame(self.__win, text=TITLE)

        self.__create_point_learning_rate()
        self.__create_point_optymaizel()

        return self.__frame

    def get_list(self) -> []:
        """ Zwraca tablice z wpisanymi danymi """
        return [
            self.__learning_rates.get(), [val.get() for val in self.__opt]
        ]

    def __create_point_learning_rate(self) -> None:
        """ Tworzy w ramce pole do pobierania kroku uczenia """
        tk.Label(
            self.__frame, text=TEXT_POINT_LEARNING_RATE,
            font=first_win.FONT_TEXT
        ).grid(
            row=INDEX['lr_cont_y'], column=INDEX['lr_cont_x'],
            sticky=tk.E, padx=PAD_X, pady=PAD_Y
        )

        self.__learning_rates = tk.Entry(
            self.__frame, font=first_win.FONT_TEXT, width=ENTRY_LEN
        )

        self.__learning_rates.grid(
            row=INDEX['lr_answ_y'], column=INDEX['lr_answ_x'],
            sticky=tk.W, padx=4
        )

    def __create_point_optymaizel(self) -> None:
        """ Wyswietla na ekramie pole do wyboru optymalizatora """
        tk.Label(
            self.__frame, text=TEXT_POINT_OPTYMAIZEL,
            font=first_win.FONT_TEXT
        ).grid(
            row=INDEX['opt_cont_y'], column=INDEX['opt_cont_x'],
            sticky=tk.W, padx=PAD_X, pady=PAD_Y
        )

        frame = tk.Frame(self.__frame)
        frame.grid(
            row=INDEX['opt_answ_y'], column=INDEX['opt_answ_x'], sticky=tk.W
        )

        for i, row in enumerate(OPTION_OPTYMAIZEL):
            tk.Checkbutton(
                frame, text=row, variable=self.__opt[i],
                onvalue=ON, offvalue=OFF, font=first_win.FONT_TEXT
            ).pack(side=tk.LEFT)
