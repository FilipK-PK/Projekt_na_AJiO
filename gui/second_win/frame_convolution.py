""" frame_convolution.py """
from gui.second_win import frame_skeleton
from gui.first_win import first_win

import tkinter as tk


BUTTON_TEXT = 'Dodaj warstwe konwolucjna'
LAY_TITLE = 'Warstwa konwolucjna'
CONTEXT_LAY = 'Podaj rozmiary warstwy:'
CONTEXT_REP_LAY = 'Podaj liczbę powturzen w.:'
CONTEXT_MAXPOLL = 'Podaj maxpoll:'
CONTEXT_BIAS = 'Batchnormalization:'
CONTEXT_FILTER = 'Podaj rozmiar filtra:'
BUTTON_TEXT_DEL = ' X '
PAD_MIDDLE = 20
ENTRY_WIDTH = 25
PAD_X, PAD_Y = 5, 4
PAD_DELETE = 55
END = -1
START = 1
ON, OFF = 1, 0
INDEX = {
    'lay_con_y': 0, 'lay_con_x': 0, 'lay_ans_y': 0, 'lay_ans_x': 1,
    'pad_y': 0, 'pad_x': 2,
    'bia_con_y': 0, 'bia_con_x': 3, 'bia_ans_y': 0, 'bia_ans_x': 4,
    'rep_con_y': 1, 'rep_con_x': 0, 'rep_ans_y': 1, 'rep_ans_x': 1,
    'pol_con_y': 1, 'pol_con_x': 3, 'pol_ans_y': 1, 'pol_ans_x': 4,
    'fil_con_y': 2, 'fil_con_x': 0, 'fil_ans_y': 2, 'fil_ans_x': 1,
    'pad_del_y': 0, 'pad_del_x': 5, 'but_del_y': 0, 'but_del_x': 6,
}


class FrameConvolution(frame_skeleton.FrameSkeleton):
    """"""

    def __init__(self, win):
        """ Definiowanie zmiennyc klasy """
        super().__init__(win)
        self._button_text = BUTTON_TEXT
        self._lay_text = LAY_TITLE

    def _fill_frame(self, frame) -> None:
        """ Wywołanie funkcji pobierających podane zmienne """
        self.__set_lay(frame)
        self.__set_pad_middle(frame)
        self.__set_bias(frame)
        self.__set_repeat_lay(frame)
        self.__set_maxpoll(frame)
        self.__set_filter(frame)
        self.__set_button_del(frame)

    def __set_lay(self, frame) -> None:
        """ Definiuje pole dla rozmiaru warstwy """
        tk.Label(frame, text=CONTEXT_LAY, font=first_win.FONT_TEXT).grid(
            row=INDEX['lay_con_y'], column=INDEX['lay_con_x'], sticky=tk.W,
            padx=PAD_X
        )

        entry = tk.Entry(frame, width=ENTRY_WIDTH, font=first_win.FONT_TEXT)
        entry.grid(
            row=INDEX['lay_ans_y'], column=INDEX['lay_ans_x'], sticky=tk.W,
            padx=PAD_X
        )

        self._list_frame[END].append(entry)

    def __set_repeat_lay(self, frame) -> None:
        """ Definiuje pole dla powturzenia warstwy """
        tk.Label(frame, text=CONTEXT_REP_LAY, font=first_win.FONT_TEXT).grid(
            row=INDEX['rep_con_y'], column=INDEX['rep_con_x'], sticky=tk.W,
            padx=PAD_X
        )

        entry = tk.Entry(frame, width=ENTRY_WIDTH, font=first_win.FONT_TEXT)
        entry.grid(
            row=INDEX['rep_ans_y'], column=INDEX['rep_ans_x'], sticky=tk.W,
            padx=PAD_X
        )

        self._list_frame[END].append(entry)

    @staticmethod
    def __set_pad_middle(frame) -> None:
        """ Definiuje odstep pomiedzy kolumnami """
        tk.Frame(frame, width=PAD_MIDDLE).grid(
            row=INDEX['pad_y'], column=INDEX['pad_x']
        )

    def __set_maxpoll(self, frame) -> None:
        """ Definiuje pole dla maxpool """
        tk.Label(frame, text=CONTEXT_MAXPOLL, font=first_win.FONT_TEXT).grid(
            row=INDEX['pol_con_y'], column=INDEX['pol_con_x'], sticky=tk.W,
            padx=PAD_X, pady=PAD_Y
        )

        entry = tk.Entry(frame, width=ENTRY_WIDTH, font=first_win.FONT_TEXT)
        entry.grid(
            row=INDEX['pol_ans_y'], column=INDEX['pol_ans_x'], sticky=tk.W,
            padx=PAD_X, pady=PAD_Y
        )

        self._list_frame[END].append(entry)

    def __set_bias(self, frame) -> None:
        """ Definiuje pole dla bias """
        tk.Label(frame, text=CONTEXT_BIAS, font=first_win.FONT_TEXT).grid(
            row=INDEX['bia_con_y'], column=INDEX['bia_con_x'], sticky=tk.W,
            padx=PAD_X, pady=PAD_Y
        )

        var = tk.IntVar()
        tk.Checkbutton(frame, variable=var, onvalue=ON, offvalue=OFF).grid(
            row=INDEX['bia_ans_y'], column=INDEX['bia_ans_x'], sticky=tk.W
        )

        self._list_frame[END].append(var)

    def __set_filter(self, frame) -> None:
        """ Definiuje pole dla filtr """
        tk.Label(frame, text=CONTEXT_FILTER, font=first_win.FONT_TEXT).grid(
            row=INDEX['fil_con_y'], column=INDEX['fil_con_x'], sticky=tk.W,
            padx=PAD_X, pady=PAD_Y
        )

        entry = tk.Entry(frame, width=ENTRY_WIDTH, font=first_win.FONT_TEXT)
        entry.grid(
            row=INDEX['fil_ans_y'], column=INDEX['fil_ans_x'], sticky=tk.W,
            padx=PAD_X, pady=PAD_Y
        )

        self._list_frame[END].append(entry)

    def __set_button_del(self, frame) -> None:
        """  Definiuje pole dla przycisku dodającego nowe warstwy """
        tk.Frame(frame, width=PAD_DELETE).grid(
            row=INDEX['pad_del_y'], column=INDEX['pad_del_x'], sticky=tk.NSEW
        )

        tk.Button(
            frame, text=BUTTON_TEXT_DEL, font=first_win.FONT_TEXT,
            command=lambda: self._del_frame(frame)
        ).grid(
            row=INDEX['but_del_y'], column=INDEX['but_del_x'], sticky=tk.E
        )
