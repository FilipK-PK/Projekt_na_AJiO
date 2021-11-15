""" gui.py """
from gui.first_win import first_win

import tkinter as tk


TITLE = 'Aplikacja optymalizująca modelpod względem dłędu uczenia'
HEIGHT_WIN = 500
WIDTH_WIN = 800
IF_CHANGE = False


class Gui:
    """ Klasa główna, uruchamia pierwsze okno """

    def __init__(self):
        """ Tworzenie okna graficznego i załadowanie modułu okna pierwsego """
        self.__main = tk.Tk()
        self.__set_main()
        self.__first_win = first_win.FirstWin(self.__main)
        self.__first_win.create()

    def run(self) -> None:
        """ Uruchomie aplikacji """
        self.__main.mainloop()

    def __set_main(self) -> None:
        """ Ustawianie opcji dla okna głównego """
        self.__main.title(TITLE)
        self.__main.geometry(f'{WIDTH_WIN}x{HEIGHT_WIN}')
        self.__main.resizable(width=IF_CHANGE, height=IF_CHANGE)
