""" second_win.py """
from gui.second_win import frame_neuron, frame_convolution
from gui.second_win import frame_options, frame_check
from gui.third_win import result_win

import tkinter as tk
import tkinter.ttk as ttk


PAD_FRAME = 5
PAD_SETTING_FRAME = 10
IF_IMG = 2
TEXT_NEU_BUT = 'Dodaj nową warstę neuronową'
TEXT_CON_BUT = 'Dodaj nową warstę konwolucjna'
LIST_FRAME = [
    ['skoku uczenia', 'optymailzatora'],
    ['rozmiaru warstw', 'batchnormalization', 'liczby powturzen', 'maxpoll'],
    ['optymalizacji', 'rozmiaru warstw', 'drop']
]
MAIN_LIST = [
    'opcjach początkowych', 'warstwach konwolucyjnych', 'warstw neuronowych'
]

WIDTH_FRAME_IN = 770
CONFIG = '<Configure>'
START = (0, 0)
TITLE_BUTTON_END = 'Zatwierdz'
COLOR_FRAME_ERR = 'red'
MAIN_INDEX = {'setting_frame': 0, 'main_option': 1,
              'frame_convolution': 2, 'button_convolution': 3,
              'frame_neuron': 4, 'button_neuron': 5,
              'frame_error': 6, 'button_compile': 7}


class SecondWin:
    """ Klasa wywołujaca klasy słurzace do podawania infoemacji o
    zmiennych warstwy """

    def __init__(self, main, typ, opt, path):
        """ Definiowanie zmiennych klasy """
        self.__main = main
        self.__typ = typ
        self.__opt = opt
        self.__path = path
        self.__win = None
        self.__main_win = None
        self.__frame_win = None
        self.__win_opt = None
        self.__win_con = None
        self.__win_neu = None
        self.__test_list = frame_check.FrameCheck()
        self.__text_error = tk.StringVar()
        self.__text_error.set('')

    def create(self) -> None:
        """ Funkcja wywołujaca funkcje wstawiajace komponenty na ekran """
        self.__set_open_start()
        self.__set_scroll()
        self.__set_main_option()

        if self.__typ == IF_IMG:
            self.__set_frame_convolution()

        self.__set_frame_neuron()
        self.__set_but_end()

    def __set_open_start(self) -> None:
        """ Definiowanie ramki głuwnej do wyswietlania komonentów """
        self.__main_win = tk.Frame(self.__main)
        self.__main_win.pack(fill=tk.BOTH, expand=tk.YES)

        self.__frame_win = tk.Canvas(self.__main_win)
        self.__frame_win.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)

    def __set_scroll(self) -> None:
        """ Definiowanie funkcji skrol """
        scroll = ttk.Scrollbar(
            self.__main_win, orient=tk.VERTICAL, command=self.__frame_win.yview
        )
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.__frame_win.configure(yscrollcommand=scroll.set)
        self.__frame_win.bind(
            CONFIG, lambda e: self.__frame_win.configure(
                scrollregion=self.__frame_win.bbox(tk.ALL))
        )

        self.__win = tk.Frame(self.__frame_win)
        self.__frame_win.create_window(START, window=self.__win, anchor=tk.NW)

    def __up_scroll(self) -> None:
        """ Aktualizacja skrola """
        self.__frame_win.update_idletasks()
        self.__frame_win.config(scrollregion=self.__win.bbox())

    def __set_main_option(self) -> None:
        """ Ustawianie ramki do definoowania opcji kompilacji """
        tk.Frame(
            self.__win, width=WIDTH_FRAME_IN + PAD_SETTING_FRAME, height=IF_IMG
        ).grid(row=MAIN_INDEX['setting_frame'])

        self.__win_opt = frame_options.FrameOption(self.__win)
        frame = self.__win_opt.create_option()
        frame.grid(
            row=MAIN_INDEX['main_option'], padx=PAD_FRAME, sticky=tk.NSEW
        )

    def __set_frame_convolution(self) -> None:
        """ Definiowanie i uruchamianie klasy do definiowania warstw
        konwolucjnych """
        self.__win_con = frame_convolution.FrameConvolution(self.__win)
        self.__win_con.add_up_scroll(self.__up_scroll)

        frame = self.__win_con.create_frame()
        button = self.__win_con.create_button()

        frame.grid(row=MAIN_INDEX['frame_convolution'])

        button.grid(
            row=MAIN_INDEX['button_convolution'], sticky=tk.W,
            padx=PAD_FRAME, pady=PAD_FRAME
        )

        self.__win_con.add_layer()

    def __set_frame_neuron(self) -> None:
        """ Definiowanie i uruchamianie klasy do definiowania warstw
        neuronowych """
        self.__win_neu = frame_neuron.FrameNeuron(self.__win)
        self.__win_neu.add_up_scroll(self.__up_scroll)

        frame = self.__win_neu.create_frame()
        button = self.__win_neu.create_button()

        frame.grid(row=MAIN_INDEX['frame_neuron'])

        button.grid(
            row=MAIN_INDEX['button_neuron'], sticky=tk.W,
            padx=PAD_FRAME, pady=PAD_FRAME
        )

        self.__win_neu.add_layer()

    def __set_but_end(self) -> None:
        """ Definiowanie przycisku do uruchominia testow """
        tk.Label(
            self.__win, textvariable=self.__text_error, fg=COLOR_FRAME_ERR
                 ).grid(
            row=MAIN_INDEX['frame_error'], sticky=tk.N, padx=PAD_FRAME,
            pady=PAD_FRAME
        )

        tk.Button(
            self.__win, text=TITLE_BUTTON_END, command=self.__check_option
        ).grid(
            row=MAIN_INDEX['button_compile'], sticky=tk.N, padx=PAD_FRAME,
            pady=PAD_FRAME
        )

    def __check_option(self) -> None:
        """ Funkcja uruchamia klase sprawdzajaca poprawnosc wprowadzonych
        danych """
        test = frame_check.FrameCheck()

        try:
            test.check_options(self.__win_opt.get_list())

            if self.__typ == IF_IMG:
                test.check_convolution(self.__win_con.get_list())

            test.check_neuron(self.__win_neu.get_list())
        except ValueError as err:
            self.__text_error.set(err)
        else:
            self.__create_next_win()

    def __create_next_win(self) -> None:
        """ Funkcja oczyszcza ekran i wywołuje klase wyswietlająca okno
        z wynikami """
        win = result_win.ResultWin(self.__main)

        win.set_main_opt(self.__typ, self.__opt, self.__path)
        win.set_option(self.__win_opt.get_list())

        if self.__typ == IF_IMG:
            win.set_convolution(self.__win_con.get_list())

        win.set_neuron(self.__win_neu.get_list())

        win.create()

        self.__main_win.destroy()
