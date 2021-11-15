""" resulr_win.py """
from gui.third_win import frame_result, neuron_network

import threading


SEP = ','
FIRST_IND = 0
SECOND_IND = 1
IND_LAY_CON = 0
IND_BATH = 1
IND_REP = 2
IND_POLL = 3
IND_FIL = 4
NULL = 0
IND_LAY_NEU = 1
INF_F_ACT = 0
IND_DROP = 2
IND_REP_NEU = 3
USE_DEMON = True
EMPTY = []
EMPTY_2 = [[]]


class ResultWin:
    """ Klasa zazadzajaca wyswietlaniem i przeszykiwanie pochanych modeli """

    def __init__(self, main):
        """ Definiowanie zmiennych klasy """
        self.__main = main
        self.__typ = None
        self.__opt = None
        self.__path = None
        self.__frame_result = None
        self.__list = []
        self.__all_var = []
        self.__len_con = NULL
        self.__len_neu = NULL
        self.__is_con = False
        self.__how_lay = None

    def set_main_opt(self, typ, opt, path) -> None:
        """ Zapisanie pdanych zmiennych """
        self.__typ = typ
        self.__opt = opt
        self.__path = path

    def set_option(self, data) -> None:
        """ Funkcja wstawia do tablizy przekształcone zmienne kompilacji """
        self.__list.append([float(i) for i in data[FIRST_IND].split(SEP)])
        self.__list.append([i for i, var in enumerate(data[SECOND_IND]) if var])

    def set_convolution(self, data) -> None:
        """ Funkcja wstawia do tablizy przekształcone zmienne o warstwie
        konwolucjnej """
        if data:
            self.__is_con = True
            self.__len_con = len(data)

            for row in data:
                self.__list.append([int(i) for i in row[IND_LAY_CON].split(SEP)])
                self.__list.append([row[IND_BATH]])
                self.__list.append([int(i) for i in row[IND_REP].split(SEP)])
                self.__list.append([int(i) for i in row[IND_POLL].split(SEP)])
                self.__list.append([int(i) for i in row[IND_FIL].split(SEP)])
        else:
            self.__len_con = NULL

    def set_neuron(self, data) -> None:
        """ Funkcja wstawia do tablizy przekształcone zmienne o warstwie
        neuronowej """
        self.__len_neu = len(data)

        for row in data:
            self.__list.append([i for i, var in enumerate(row[INF_F_ACT]) if var])
            self.__list.append([int(i) for i in row[IND_LAY_NEU].split(SEP)])
            self.__list.append([float(i) for i in row[IND_DROP].split(SEP)])
            self.__list.append([int(i) for i in row[IND_REP_NEU].split(SEP)])

    def create(self) -> None:
        """ Funkcja uruchamia funkcje oblicające wsystkie mozliwosci, obliczajace bład i
        wyswietlające je na ekranie """
        self.__all_possibi()
        self.__set_frame_result()

        model = neuron_network.NeuronNetwork(
            self.__typ, self.__opt, self.__path, self.__how_lay
        )

        threading.Thread(
            target=self.__test_model,
            args=(model, self.__frame_result),
            daemon=USE_DEMON
        ).start()

    def __set_frame_result(self) -> None:
        """ Funkcja wywołuje klase wyswietlajaca wyniki w oknie """
        self.__how_lay = [self.__len_con, self.__len_neu]

        self.__frame_result = frame_result.FrameResult(self.__main)
        self.__frame_result.set_name(self.__opt)
        self.__frame_result.set_max(len(self.__all_var))
        self.__frame_result.set_len_lay(self.__how_lay)
        self.__frame_result.create()

    def __all_possibi(self) -> None:
        """ Funkcja tworzy wszystkie mozliwosci podanych wartosci i zapisuje
        je do tablicy """
        data_a, data_b = EMPTY, EMPTY_2

        for var in self.__list:
            for v in data_b:
                for i in var:
                    data_a.append(v + [i])

            data_b, data_a = data_a, []

        self.__all_var = data_b

    def __test_model(self, model, frame) -> None:
        """ Funkcja wywołuje funkcje zwracająca bład uczenia danego modelu
        i wyswietla go na ekranie"""
        for vec in self.__all_var:
            err = model.test_model(vec)
            frame.add_result(err, vec)
