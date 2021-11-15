""" frame_skeleton.py """
from gui.second_win import second_win

import tkinter as tk


TEXT_BUTTON = ''
TITLE_LAY = 'Prycisk'
ADD = 1
PAD_UP = 10
FIRST_IND = 0
START = 1
ID = 'id_'


class FrameSkeleton:
    """ Klasa jest podstaw dla klas do pobierania zmiennych warstwy """

    def __init__(self, win):
        """ Definiowanie zmiennych klasy """
        self._win = win
        self._index_lay = FIRST_IND
        self._win_frame = None
        self._update_scroll = None
        self._button_text = TEXT_BUTTON
        self._lay_text = TITLE_LAY
        self._list_frame = []

    def create_frame(self) -> tk.Frame:
        """ Zwraca ramke z warstwa """
        self._win_frame = tk.Frame(self._win)

        tk.Frame(
            self._win_frame, width=second_win.WIDTH_FRAME_IN, height=PAD_UP
        ).grid(row=self._index_lay)

        self._index_lay += ADD

        return self._win_frame

    def create_button(self) -> tk.Button:
        """ Zwraca przycisk do szczegułowych opcji """
        return tk.Button(self._win, text=self._button_text, command=self.add_layer)

    def add_up_scroll(self, up_scroll) -> None:
        """ Ustawianie skrola """
        self._update_scroll = up_scroll

    def add_layer(self) -> None:
        """ Dodawanie nowej warstwy do wyswietlenia """
        frame = tk.LabelFrame(
            self._win_frame, name=ID + str(self._index_lay), text=self._lay_text,
            width=second_win.WIDTH_FRAME_IN
        )

        frame.grid(row=self._index_lay, sticky=tk.NSEW)

        self._list_frame.append([frame])

        self._fill_frame(frame)
        self._index_lay += ADD
        self._update_scroll()

    def get_list(self) -> []:
        """ Zwracac liste warstw """
        return [
            [
                [j.get() for j in i] if isinstance(i, list) else i.get() for i in row[START:]
            ] for row in self._list_frame
        ]

    def _fill_frame(self, frame) -> None:
        """ Funkcja wyswietla w oknie ramke pusta """
        tk.Frame(frame).pack()

    def _del_frame(self, frame) -> None:
        """ Usuwanie rwmki z danym id """
        for i, row in enumerate(self._list_frame):
            if row[0] == frame:
                del self._list_frame[i]

        frame.destroy()
        self._update_scroll()
