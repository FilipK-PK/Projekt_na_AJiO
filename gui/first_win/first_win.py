""" first.win.py """
from gui.second_win import second_win
from gui.first_win import check_data, frame_type, frame_error
from gui.first_win import frame_select, frame_path
from gui import gui

import tkinter as tk


WIDTH_RADIO_BUTTON = int(800*0.8)
CENTER_RADIO_BUTTON = int(800*0.1)
FONT_TITLE = ('Arial', 14)
FONT_BUTTON = ('Arial', 12)
FONT_FRAME = ('Arial', 11)
FONT_TEXT = ('Arial', 9)
ERROR_FRONT = 'Nie zaznaczono: '
RADIO_BUTTON_BIAS = 1
END_IND = -1

TITLE = {
    'title': 'Wstepne parametry optymalizacji',
    'y': 20,
}

TYPE_MODEL = {
    'title': 'Wybor rodzaju sieci',
    'y': 80,
    'option': ['Neuronowa - pliki .csv',
               'Konwolucyjna - zdiecia']
}

SELECT_WIN = {
    'title': 'Wybor selekcji uczenia modelu',
    'y': 180,
    'option': ['Sprawdzenie wszystkich mozliwosci do wykrycia przeuczenia',
               'Sprawdzenie wszystkich mozliwosci do pewnej liczby epok'],
    'title_epoch': 'Liczba epok: ',
    'width_epoch': 6
}

DATA_WIN = {
    'title': 'Wybor zbioru uczacego',
    'y': 330,
    'button_text': 'Wybierz scierzke do pliku',
}

START_BUTTON = {
    'text': 'Przejdz dalej',
    'y': 430,
    'width': 16
}

ERROR_WIN = {
    'y': 400,
    'color': 'red'
}


class FirstWin:
    """ Klasa wyswietla okno poczatkowe """

    def __init__(self, main):
        """ Definiowanie zmiennych klasy """
        self.__main = main
        self.__win = None
        self.__next_win = None

        self.__frame_type = None
        self.__frame_select = None
        self.__frame_error = None
        self.__frame_path = None

        self.__set_win()

    def create(self) -> None:
        """ Funkcja nanosi moduły na okno programu """
        self.__set_title()
        self.__set_frame_type()
        self.__set_frame_select()
        self.__set_frame_path()
        self.__set_frame_error()
        self.__set_button_start()

    def __set_win(self) -> None:
        """ Fun ustawia i dodaje do okna głóuwnego programu famkę
        okna początkowego """
        self.__win = tk.Label(
            self.__main, width=gui.WIDTH_WIN, height=gui.HEIGHT_WIN
        )

        self.__win.pack()

    def __set_title(self) -> None:
        """ Funkcja dodaje tytuł do ramy okna pierwszego """
        frame = tk.Label(
            self.__win, text=TITLE['title'], font=FONT_TITLE
        )

        frame.place(
            width=WIDTH_RADIO_BUTTON, x=CENTER_RADIO_BUTTON, y=TITLE['y']
        )

    def __set_frame_type(self) -> None:
        """ Funkcja dodaje ramke z rodzajem sieci do ramki okna pierwszego,
        załadowując ja z klasy FrameType """
        self.__frame_type = frame_type.FrameType(self.__win)
        self.__frame_type.create()

    def __set_frame_select(self) -> None:
        """ Funkcja dodaje ramke z wyborem opcji przeszukującej możliwosci
         do ramki okna pierwszego, załadowując ja z klasy FrameSelect """
        self.__frame_select = frame_select.FrameSelect(self.__win)
        self.__frame_select.create()

    def __set_frame_path(self) -> None:
        """ Funkcja dodaje ramke z pobierająca sciezke z danymi uczącymi
         do ramki okna pierwszego, załadowując ja z klasy FramePath """
        self.__frame_path = frame_path.FramePath(self.__win)
        self.__frame_path.create()

    def __set_frame_error(self) -> None:
        """Funkcja dodaje ramke z wyswietlającej komunikat o dłędzie
         do ramki okna pierwszego, załadowując ja z klasy FrameError"""
        self.__frame_error = frame_error.FrameError(self.__win)
        self.__frame_error.create()

    def __set_button_start(self) -> None:
        """ Funkcja dodaje przyciskiem uruchamiającym test poprawnosci
        wpisanych danych i okno wyboru ustawiania warstwy uczącej do ramki
        okna pierwszego """
        frame = tk.Label(self.__win)

        tk.Button(
            frame, text=START_BUTTON['text'], font=FONT_BUTTON,
            width=START_BUTTON['width'], command=self.__click_start
        ).pack()

        frame.place(
            width=WIDTH_RADIO_BUTTON, x=CENTER_RADIO_BUTTON,
            y=START_BUTTON['y']
        )

    def __click_start(self) -> None:
        """ Funkcja uruchamiana jest po naciśnieciu przycisku, sprawdza ona
        poprawnosci danych, podacas błedy wypisuje błąd, jesli nie to
        uruchamia okno wyboru wratwy """
        test = check_data.CheckData()

        try:
            test.check_type(self.__frame_type.get_check())
            test.check_learn_opt(
                self.__frame_select.get_check(), self.__frame_select.get_epoch()
            )

            if self.__frame_type.get_check() - RADIO_BUTTON_BIAS:
                test.check_data_img(self.__frame_path.get_path())
            else:
                test.check_data_csv(self.__frame_path.get_path())

        except ValueError as err:
            self.__frame_error.set_text_error(err)

        else:
            next_win = second_win.SecondWin(
                self.__main, self.__frame_type.get_check(),
                (self.__frame_select.get_check(), int(self.__frame_select.get_epoch())),
                self.__frame_path.get_path()
            )

            self.__win.destroy()
            next_win.create()
