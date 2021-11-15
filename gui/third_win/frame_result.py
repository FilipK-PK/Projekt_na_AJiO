""" frame_result.py """
from gui.third_win import frame_info

import tkinter as tk
import tkinter.ttk as ttk


MAX_DISPLAY = 50
PAD = 10
ALL = 'all'
FONT_TITLE = ('Arial', 12)
FONT_TEXT = ('Arial', 9)
CONFIG = '<Configure>'
START = (0, 0)
BUTTON_TEXT = 'Info'
BUTTON_LEN = 10
FIRST_IND = 0
TITLE_FRAME = 'Otrzymane wyniki'
NEXT_IND = 1
TEST_NUM = 'Test nr: '
BUTTON = '<Button-1>'
END_IND = -1
SEP = '.'
PAD_LABEL_PROC = 30
PAD_FRAME = 5
IND_PROC = 0
IND_TEST = 1
ROUND = 2
ERROR_FIT = 'ERROR'
IS_ERROR = 404
IS_CHECK = 'Sprawdzono '
FOR = ' na '
NAME_OPTION_CHECK = [
    'Wyszykiwanie w sposob:', 'do przeuczenia', 'do okreslonej epoki', 'kaskadowe',
    'epokowe'
]


class FrameResult:
    """ Klasa wyswietlajace zbiorczo wyniki przeszukiwania modeli """

    def __init__(self, main):
        """ Definiowanie zmiennych klasy"""
        self.__main = main
        self.__win = None
        self.__list = []
        self.__frame_num = 0
        self.__index = FIRST_IND
        self.__how_lay = 0
        self.__name_opt = tk.StringVar()
        self.__len_check = tk.IntVar()
        self.__len_check.set(0)
        self.__max_check = None

    def set_name(self, ind) -> None:
        """ Ustawianie nazwy wyswietlającego sie wyniku uczenia """
        self.__name_opt.set(
            NAME_OPTION_CHECK[FIRST_IND] + NAME_OPTION_CHECK[ind[FIRST_IND]]
        )

    def set_max(self, size) -> None:
        """ Definiowanie liczby wszystkich testów """
        self.__max_check = size

    def create(self) -> None:
        """ Tworzenie okna wyswietlajacego wszystkie wyniki uczenia """
        self.__win = tk.Frame(self.__main)
        self.__win.pack(expand=tk.YES, fill=tk.BOTH)

        title = tk.Label(self.__win, textvariable=self.__name_opt, font=FONT_TITLE)
        title.pack()

        self.__set_proc_check()

        self.__frame_num = tk.LabelFrame(self.__win, text=TITLE_FRAME)
        self.__frame_num.pack(expand=tk.YES, fill=tk.Y, padx=PAD, pady=PAD)

        self.__set_frame_result()

    def __set_proc_check(self) -> None:
        """ Wyswietlanie liczby obliczonych modeli """
        frame = tk.Frame(self.__win)
        frame.pack()

        tk.Label(frame, text=IS_CHECK, font=FONT_TITLE).pack(side=tk.LEFT)

        tk.Label(
            frame, textvariable=self.__len_check, font=FONT_TITLE
        ).pack(side=tk.LEFT)

        tk.Label(frame, text=FOR+str(self.__max_check), font=FONT_TITLE).pack()

    def set_len_lay(self, lay) -> None:
        """ Ustawianie liczby poszczegulnych warstw sieci """
        self.__how_lay = lay

    def __set_frame_result(self) -> None:
        """ Tworzenie ramki wyswietlajacej uzyskane wyniki z scrollem """
        self.canvas = tk.Canvas(self.__frame_num)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH)

        scroll = ttk.Scrollbar(
            self.__frame_num, orient=tk.VERTICAL, command=self.canvas.yview
        )
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=scroll.set)
        self.canvas.bind(
            CONFIG,
            lambda s: self.canvas.configure(scrollregion=self.canvas.bbox(ALL))
        )

        self.__frame_scroll = tk.Frame(self.canvas)
        self.canvas.create_window(START, window=self.__frame_scroll, anchor=tk.NW)

    def add_result(self, err, data) -> None:
        """ Dodawanie otrzymanych daych na ekran, z sortowaniem """
        self.__list.append([err, self.__index, data])
        self.__index += NEXT_IND
        self.__list.sort()
        self.__len_check.set(len(self.__list))

        self.__clear_frame_result()

        self.__set_rows_result()

        self.__update_scroll()

    def __set_rows_result(self) -> None:
        """ Wyswietlanie uzyskanych wyników w ramce z wynikami """
        display_to = self.__display_to()

        for i, row in enumerate(self.__list[:display_to]):
            frame = tk.Frame(self.__frame_scroll, name=str(i))

            frame.grid(row=i, sticky=tk.NSEW, pady=PAD_FRAME)

            tk.Label(
                frame, text=TEST_NUM + str(row[IND_TEST] + NEXT_IND),
                font=FONT_TEXT, width=12
            ).pack(side=tk.LEFT, fill=tk.Y, expand=tk.YES)

            text_proc = (
                str(round(row[IND_PROC], ROUND))
                if not row[IND_PROC] == IS_ERROR else ERROR_FIT
            )

            tk.Label(
                frame, text=text_proc, font=FONT_TEXT, width=6
            ).pack(side=tk.LEFT, padx=PAD_LABEL_PROC)

            button = tk.Button(
                frame, text=BUTTON_TEXT, width=BUTTON_LEN, name=str(i)
            )

            button.pack()
            button.bind(BUTTON, self.__click_info)

    def __click_info(self, even) -> None:
        """ Tworzenie okna z informacjami szczegułowymi o danym modelu """
        result_ind = int(str(even.widget).split(SEP)[END_IND])
        data = self.__list[result_ind]

        frame_info.FrameInfo(data, self.__how_lay)

    def __display_to(self) -> int:
        """ Ustawianie liczby wyswietlonych wierszy na ekranie """
        return (
            MAX_DISPLAY if len(self.__list) > MAX_DISPLAY else len(self.__list)
        )

    def __update_scroll(self) -> None:
        """ Aktuolizowanie wysokosci ramki dla scrolla """
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.__frame_scroll.bbox())

    def __clear_frame_result(self) -> None:
        """ Usuwanie wyswietlonych wynikuw w ramce """
        self.__frame_scroll.destroy()
        self.__frame_scroll = tk.Frame(self.canvas)
        self.canvas.create_window(START, window=self.__frame_scroll, anchor=tk.NW)
