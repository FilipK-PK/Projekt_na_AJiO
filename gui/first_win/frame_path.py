""" frame_path.py """
from gui.first_win import first_win

import tkinter.filedialog as fd
import tkinter as tk


SEP_START = '../'
SEP = '/'
NONE = 'none'


class FramePath:
    """ Klasa wyswietlająca ramkę do pobierania scierki do folderu """

    def __init__(self, win):
        """ Definiowanie zmiennych klasy """
        self.__win = win
        self.__data_path = None
        self.__name_path_win = tk.StringVar()
        self.__name_path_win.set(NONE)

    def create(self) -> None:
        """ Tworzenie ramki do pobierania scierzki do folderu,
        z wyswietlaniem wprowadzonej scierzki """
        frame = tk.LabelFrame(
            self.__win, text=first_win.DATA_WIN['title'],
            font=first_win.FONT_FRAME
        )

        button = tk.Button(
            frame, text=first_win.DATA_WIN['button_text'],
            command=self.__check_data, font=first_win.FONT_TEXT
        )

        button.pack(
            anchor=tk.W, side=tk.LEFT, padx=5, pady=5
        )

        tk.Label(
            frame, textvariable=self.__name_path_win, font=first_win.FONT_TEXT
        ).pack(anchor=tk.W, side=tk.LEFT)

        frame.place(
            width=first_win.WIDTH_RADIO_BUTTON, x=first_win.CENTER_RADIO_BUTTON,
            y=first_win.DATA_WIN['y']
        )

    def get_path(self) -> str:
        """ Zwraca scierzke do pliku """
        return self.__data_path

    def get_path_visit(self) -> tk.StringVar:
        """ Zwraca sformatowaną scierzke wyswietlana w ramce """
        return self.__name_path_win

    def __check_data(self) -> None:
        """ Funkcja tworzy osobne okno w kturym mozna graficznie wybrac
         folder z damyni """
        self.__data_path = fd.askdirectory()

        self.__name_path_win.set(
            SEP_START + self.__data_path.split(SEP)[first_win.END_IND]
        )
