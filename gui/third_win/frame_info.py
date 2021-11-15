""" frame_info.py """
from gui.third_win import frame_result

import tkinter as tk

FIRST_IN = 2
NEXT_IND = 1
CON_LAY, NEU_LAY = 0, 1
NEU_SIZE = 4
CON_SIZE = 5
ROUND = 2
WIDTH_PAD = 20
ROW_PAD = 1
ROUNF_TO = 2
PAD_START, PAD_END, PAD_JUMP = 1, 14, 3
IND_LAY = 2
WIDTH_MIN_PAD = 10
ERROR_FIT = 404
NAME_FUN_ACT = ['relu', 'tanh', 'softmax']
NAME_OPTYMAIZEL = ['Adam', 'RMSprop', 'SGD']
IS_BATH = ['NO', 'YES']
RESULT = {
    'title': 'Uzyskano:', 'row': 0, 'col': 0, 'row_res': 0, 'col_res': 1,
    'ind_res': 0
}
LR = {
    'title': 'Skok uczenia:', 'row': 0, 'col': 2, 'row_res': 0, 'col_res': 3,
    'ind_res': 0
}
OPTYM = {
    'title': 'Optymalizator:', 'row': 0, 'col': 5, 'row_res': 0, 'col_res': 6,
    'ind_res': 1
}
TITLE_CON = {'title': 'W.Konwolucjna ',  'col': 0}
SIZE_CON = {'title': 'Rozmiar warstwy:', 'col': 2, 'col_res': 3}
REPET_CON = {'title': 'Powturzenia warstwy:', 'col': 5, 'col_res': 6, 'ind': 2}
MAX_CON = {'title': 'Maxpolling:', 'col': 8, 'col_res': 9, 'ind': 3}
FILTER_CON = {'title': 'Filtr:', 'col': 11, 'col_res': 12, 'ind': 4}
BATCH_CON = {'title': 'Batchnorm..', 'col': 14, 'col_res': 15, 'ind': 1}
TITLE_NEU = {'title': 'W.Neuronowa ', 'col': 0, 'col_res': 1, 'ind': 1}
ACT_NEU = {'title': 'F.aktywacji:', 'col': 2, 'col_res': 3}
SIZE_NEU = {'title': 'Rozmiar warstwy:', 'col': 5, 'col_res': 6, 'ind': 1}
DROP_NEU = {'title': 'Drop', 'col': 8, 'col_res': 9, 'ind': 2}
REPET_NEU = {'title': 'Powtuzenia.w:', 'col': 11, 'col_res': 12, 'ind': 3}


class FrameInfo:
    """ Klasa wyswietla szczegułowe informacje o urzytej sieci """

    def __init__(self, data, len_lay):
        """ Dekralacja zmiennych klasy i ustawianie kolejnosci
        wyswietlania sie warstw sieci """
        self.__main = None
        self.__data = data
        self.__len_lay = len_lay
        self.__ind_lay = FIRST_IN

        self.__set_win()
        self.__set_opt()
        self.__set_con()
        self.__set_neu()
        self.__set_padding()

    def __set_win(self) -> None:
        """ Tworzenie osobnego okna do wyswitlania ustawen warstwy """
        self.__main = tk.Toplevel(self.__main)
        self.__main.resizable(width=tk.NO, height=tk.NO)
        self.__main.title(
            frame_result.TEST_NUM + str(
                self.__data[frame_result.IND_TEST] + frame_result.NEXT_IND
            )
        )

    def __set_opt(self) -> None:
        """ wywołuje funkcje wstawiające na ekram informacje o
        optymalizatorze  """
        self.__set_result()
        self.__set_lr()
        self.__set_opt_f()

    def __set_con(self) -> None:
        """ Wywuje funkcje wstawiajace na ekran informacje o sieci
        konwolucjej """
        start = FIRST_IN
        stop = FIRST_IN + self.__len_lay[CON_LAY] * CON_SIZE
        self.__ind_lay = NEXT_IND

        for i, j in zip(
                range(start, stop, CON_SIZE), range(self.__len_lay[CON_LAY])
        ):
            self.__set_title_con(self.__ind_lay, j)
            self.__set_size_con(self.__ind_lay, i)
            self.__set_repet(self.__ind_lay, i)
            self.__set_maxpoll(self.__ind_lay, i)
            self.__set_filter(self.__ind_lay, i)
            self.__set_bath(self.__ind_lay, i)

            self.__ind_lay += NEXT_IND

    def __set_neu(self) -> None:
        """ Wywuje funkcje wstawiajace na ekran informacje o sieci
        neuronowej """
        start = FIRST_IN + self.__len_lay[CON_LAY] * CON_SIZE
        stop = start + self.__len_lay[NEU_LAY] * NEU_SIZE

        for i, j in zip(
                range(start, stop, NEU_SIZE), range(self.__len_lay[NEU_LAY])
        ):
            self.__set_title_neu(self.__ind_lay, j)
            self.__set_act(self.__ind_lay, i)
            self.__set_size_neu(self.__ind_lay, i)
            self.__set_drop(self.__ind_lay, i)
            self.__set_repet_neu(self.__ind_lay, i)

            self.__ind_lay += NEXT_IND

    def __set_padding(self) -> None:
        """ Funkcja wstawia odstepy pomiedzy wyswietlającyni sie kolumnami """
        for i in range(PAD_START, PAD_END, PAD_JUMP):
            tk.Frame(self.__main, width=WIDTH_PAD).grid(row=ROW_PAD, column=i)

    def __set_result(self) -> None:
        """ Funkcja wyswietla uzyskany bład """
        tk.Label(
            self.__main, text=RESULT['title']
        ).grid(row=RESULT['row'], column=RESULT['col'], sticky=tk.W)

        if self.__data[RESULT['ind_res']] == ERROR_FIT:
            var = 'X'
        else:
            var = str(round(self.__data[RESULT['ind_res']], ROUNF_TO))

        tk.Label(
            self.__main, text=var
        ).grid(row=RESULT['row_res'], column=RESULT['col_res'], sticky=tk.E)

    def __set_lr(self) -> None:
        """ Funkcja wyswietla skok uczenia """
        tk.Label(
            self.__main, text=LR['title']
        ).grid(row=LR['row'], column=LR['col'], sticky=tk.W)

        tk.Label(
            self.__main, text=str(self.__data[IND_LAY][LR['ind_res']])
        ).grid(row=LR['row_res'], column=LR['col_res'], sticky=tk.E)

    def __set_opt_f(self) -> None:
        """ Funkcja wyswietla uzyta funkcje aktywacji """
        tk.Label(
            self.__main, text=OPTYM['title']
        ).grid(row=OPTYM['row'], column=OPTYM['col'], sticky=tk.W)

        tk.Label(
            self.__main,
            text=NAME_OPTYMAIZEL[self.__data[IND_LAY][OPTYM['ind_res']]]
        ).grid(row=OPTYM['row_res'], column=OPTYM['col_res'], sticky=tk.E)

    def __set_title_con(self, ind_lay, row) -> None:
        """ Funkcja wyswietla nazwe i index warstwy konwolucjnej """
        tk.Label(
            self.__main, text=TITLE_CON['title'] + str(row + NEXT_IND)
        ).grid(row=ind_lay, column=TITLE_CON['col'], sticky=tk.W)

    def __set_size_con(self, ind_lay, ind_opt) -> None:
        """ Funkcja wyswietla rozniar danej warstwy konwolucjnej """
        tk.Label(
            self.__main, text=SIZE_CON['title']
        ).grid(row=ind_lay, column=SIZE_CON['col'], sticky=tk.W)

        tk.Label(
            self.__main, text=str(self.__data[IND_LAY][ind_opt])
        ).grid(row=ind_lay, column=SIZE_CON['col_res'], sticky=tk.E)

    def __set_repet(self, ind_lay, ind_opt) -> None:
        """ Funkcja wyswietla liczbe powturzen danej warstwy konwolucjnej """
        tk.Label(
            self.__main, text=REPET_CON['title']
        ).grid(row=ind_lay, column=REPET_CON['col'], sticky=tk.W)

        tk.Label(
            self.__main,
            text=str(self.__data[IND_LAY][ind_opt + REPET_CON['ind']])
        ).grid(row=ind_lay, column=REPET_CON['col_res'], sticky=tk.E)

    def __set_maxpoll(self, ind_lay, ind_opt) -> None:
        """ Funkcja wyswietla maxpool dla danej warstwy konwolucjnej """
        tk.Label(
            self.__main, text=MAX_CON['title']
        ).grid(row=ind_lay, column=MAX_CON['col'], sticky=tk.W)

        tk.Label(
            self.__main,
            text=str(self.__data[IND_LAY][ind_opt + MAX_CON['ind']])
        ).grid(row=ind_lay, column=MAX_CON['col_res'], sticky=tk.E)

    def __set_filter(self, ind_lay, ind_opt) -> None:
        """ Funkcja wyswietla rozniar filtra dla danej warstwy
        konwolucjnej """
        tk.Label(
            self.__main, text=FILTER_CON['title']
        ).grid(row=ind_lay, column=FILTER_CON['col'], sticky=tk.W)

        tk.Label(
            self.__main,
            text=str(self.__data[IND_LAY][ind_opt + FILTER_CON['ind']])
        ).grid(row=ind_lay, column=FILTER_CON['col_res'], sticky=tk.E)

    def __set_bath(self, ind_lay, ind_opt) -> None:
        """ Funkcja wyswietla bath dla danej warstwy konwolucjnej """
        tk.Label(
            self.__main, text=BATCH_CON['title']
        ).grid(row=ind_lay, column=BATCH_CON['col'], sticky=tk.W)

        tk.Label(
            self.__main,
            text=IS_BATH[self.__data[IND_LAY][ind_opt + BATCH_CON['ind']]]
        ).grid(row=self.__ind_lay, column=BATCH_CON['col_res'], sticky=tk.E)

    def __set_title_neu(self, ind_lay, ind_opt) -> None:
        """ Funkcja wyswietla tytuł i index dla danej warstwy neuronowej """
        tk.Label(
            self.__main, text=TITLE_NEU['title'] + str(ind_opt + NEXT_IND)
        ).grid(row=ind_lay, column=TITLE_NEU['col'], sticky=tk.W)

        tk.Frame(
            self.__main, width=WIDTH_MIN_PAD
        ).grid(row=ind_lay, column=TITLE_NEU['col_res'])

    def __set_act(self, ind_lay, ind_opt) -> None:
        """ Funkcja wyswietla funkcje aktywacji dla danej warstwy neuronowej """
        tk.Label(
            self.__main, text=ACT_NEU['title']
        ).grid(row=ind_lay, column=ACT_NEU['col'], sticky=tk.W)

        tk.Label(
            self.__main,
            text=NAME_FUN_ACT[self.__data[IND_LAY][ind_opt]]
        ).grid(row=ind_lay, column=ACT_NEU['col_res'], sticky=tk.E)

    def __set_size_neu(self, ind_lay, ind_opt) -> None:
        """ Funkcja wyswietla rozmiar warstwy dla danej warstwy neuronowej """
        tk.Label(
            self.__main, text=SIZE_NEU['title']
        ).grid(row=ind_lay, column=SIZE_NEU['col'], sticky=tk.W)

        tk.Label(
            self.__main, text=str(self.__data[IND_LAY][ind_opt + SIZE_NEU['ind']])
        ).grid(row=ind_lay, column=SIZE_NEU['col_res'], sticky=tk.E)

    def __set_drop(self, ind_lay, ind_opt) -> None:
        """ Funkcja wyswietla drop dla danej warstwy neuronowej """
        tk.Label(
            self.__main, text=DROP_NEU['title']
        ).grid(row=ind_lay, column=DROP_NEU['col'], sticky=tk.W)

        tk.Label(
            self.__main,
            text=str(self.__data[IND_LAY][ind_opt + DROP_NEU['ind']])
        ).grid(row=ind_lay, column=DROP_NEU['col_res'], sticky=tk.E)

    def __set_repet_neu(self, ind_lay, ind_opt) -> None:
        """ Funkcja wyswietla powturzenia warstwy dla danej warstwy
        neuronowej """
        tk.Label(
            self.__main, text=REPET_NEU['title']
        ).grid(row=ind_lay, column=REPET_NEU['col'], sticky=tk.W)

        tk.Label(
            self.__main,
            text=str(self.__data[IND_LAY][ind_opt + REPET_NEU['ind']])
        ).grid(row=ind_lay, column=REPET_NEU['col_res'], sticky=tk.E)
