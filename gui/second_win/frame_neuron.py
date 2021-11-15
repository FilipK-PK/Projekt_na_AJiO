""" frame_neuron.py """
from gui.second_win import frame_skeleton
from gui.first_win import first_win

import tkinter as tk


BUTTON_TEXT_ADD = 'Dodaj warstwe neuronową'
LAY_TITLE = 'Warstwa neuronowa'
CONTEXT_OPTIONS = 'Wybierz rodzaj optymalizacji:'
CONTEXT_LAY = 'Podaj rozmiary warstw:'
CONTEXT_DROP = 'Podaj wartosci dla drop:'
CONTEXT_REPET = 'Podaj liczbę powturzen w:'
BUTTON_TEXT_DEL = ' X '
OPRYMAIZEL_NAME = ['Relu', 'tanH', 'softmax']
END_ID = -1
ON, OFF = 1, 0
PAD_X, PAD_Y = 5, 4
SIZE_ENTRY = 25
PAD_DELETE = 32
PAD_IN = 20
START = 1
INDEX = {
    'opt_con_y': 0, 'opt_con_x': 0, 'opt_ans_y': 0, 'opt_ans_x': 1,
    'rep_con_y': 0, 'rep_con_x': 3, 'rep_ans_y': 0, 'rep_ans_x': 4,

    'lay_con_y': 1, 'lay_con_x': 0, 'lay_ans_y': 1, 'lay_ans_x': 1,
    'pad_y': 1, 'pad_x': 2,
    'dro_con_y': 1, 'dro_con_x': 3, 'dro_ans_y': 1, 'dro_ans_x': 4,
    'pad_del_y': 0, 'pad_del_x': 5, 'but_del_y': 0, 'but_del_x': 6
}


class FrameNeuron(frame_skeleton.FrameSkeleton):
    """ Klasa wyswietla i pobiera informacje o sieci neuronowej """

    def __init__(self, win):
        """ Definiowanie zmiennych klasy """
        super().__init__(win)
        self._button_text = BUTTON_TEXT_ADD
        self._lay_text = LAY_TITLE

    def _fill_frame(self, frame) -> None:
        """ Wywołanie funkcji pobierających informacje o sieci """
        self.__set_optmaizel(frame)
        self.__set_size_lay(frame)
        self.__set_pad_middle(frame)
        self.__set_use_drop(frame)
        self.__set_repet_lay(frame)
        self.__set_button_del(frame)

    def __set_optmaizel(self, frame) -> None:
        """ Definiowanie pola dla f aktywacji"""
        tk.Label(
            frame, text=CONTEXT_OPTIONS, font=first_win.FONT_TEXT
        ).grid(
            row=INDEX['opt_con_y'], column=INDEX['opt_con_x'], sticky=tk.W,
            padx=PAD_X
        )

        frame_check = tk.Frame(frame)
        frame_check.grid(
            row=INDEX['opt_ans_y'], column=INDEX['opt_ans_x'],  sticky=tk.W,
            padx=PAD_X
        )

        len_opt = len(OPRYMAIZEL_NAME)
        check_val = [tk.IntVar() for _ in range(len_opt)]
        self._list_frame[END_ID].append(check_val)

        for check_id, row in zip(check_val, OPRYMAIZEL_NAME):
            tk.Checkbutton(
                frame_check, text=row, variable=check_id, onvalue=ON,
                offvalue=OFF, font=first_win.FONT_TEXT
            ).pack(side=tk.LEFT)

    def __set_size_lay(self, frame) -> None:
        """ Definiowanie pola dla rozmiaru sieci """
        tk.Label(
            frame, text=CONTEXT_LAY, font=first_win.FONT_TEXT
        ).grid(
            row=INDEX['lay_con_y'], column=INDEX['lay_con_x'], sticky=tk.W,
            padx=PAD_X, pady=PAD_Y
        )

        text = tk.Entry(frame, width=SIZE_ENTRY, font=first_win.FONT_TEXT)
        text.grid(
            row=INDEX['lay_ans_y'], column=INDEX['lay_ans_x'], pady=PAD_Y
        )

        self._list_frame[END_ID].append(text)

    def __set_repet_lay(self, frame) -> None:
        """ Definiowanie pola dla rowturzenia sieci """
        tk.Label(
            frame, text=CONTEXT_REPET, font=first_win.FONT_TEXT
        ).grid(
            row=INDEX['rep_con_y'], column=INDEX['rep_con_x'], sticky=tk.W,
            padx=PAD_X, pady=PAD_Y
        )

        text = tk.Entry(frame, width=SIZE_ENTRY, font=first_win.FONT_TEXT)
        text.grid(
            row=INDEX['rep_ans_y'], column=INDEX['rep_ans_x'], pady=PAD_Y
        )

        self._list_frame[END_ID].append(text)

    @staticmethod
    def __set_pad_middle(frame) -> None:
        """ Ustawia odstep mpniedzy opcjami """
        tk.Frame(frame, width=PAD_IN).grid(
            row=INDEX['pad_y'], column=INDEX['pad_x']
        )

    def __set_use_drop(self, frame) -> None:
        """ Definiowanie pola dla drop """
        tk.Label(
            frame, text=CONTEXT_DROP, font=first_win.FONT_TEXT
        ).grid(
            row=INDEX['dro_con_y'], column=INDEX['dro_con_x'], sticky=tk.W,
            padx=PAD_X, pady=PAD_Y
        )

        text = tk.Entry(frame, width=SIZE_ENTRY, font=first_win.FONT_TEXT)
        text.grid(
            row=INDEX['dro_ans_y'], column=INDEX['dro_ans_x'], pady=PAD_Y,
            sticky=tk.W
        )

        self._list_frame[END_ID].append(text)

    def __set_button_del(self, frame) -> None:
        """ Definiowanie przycisku do dodawania nowych warstw """
        tk.Frame(frame,  width=PAD_DELETE).grid(
            row=INDEX['pad_del_y'], column=INDEX['pad_del_x'], sticky=tk.NSEW
        )

        tk.Button(
            frame, text=BUTTON_TEXT_DEL,
            command=lambda: self._del_frame(frame)
        ).grid(
            row=INDEX['but_del_y'], column=INDEX['but_del_x'], sticky=tk.E
        )
