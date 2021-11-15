""" check_data.py """
import os


IF_SECOND_OPT = 2
NEG = 0
IS_BIG = 500
DOT = '.'
FIRST_IND = 0
SECOND_IND = 1
SIZE_MAIN_FOL = 2
PNG = '.png'
SET_MAIN_FOL = ['train', 'val']
SET_MAIN_FOL_CSV = ['train_x.csv', 'train_y.csv', 'val_x.csv', 'val_y.csv',]
TEXT_ERROR_TYPE = 'Nie zaznaczono rodzaju sieci'
TEXT_ERROR_OPT = {
    'not_check': 'Nie zaznaczono selekcji uczenia',
    'empty': 'Nie wpisano liczby epok dla sekcji uczenia',
    'not_num': 'Liczba epok nie jest liczbą w sekcji uczenia',
    'is_neg': 'Liczby epok niemoze byc ujemna lub zerowa w sekcji uczenia',
    'is_big': 'Duza liczba epok, w sekcji uczenai, proponuje zamienic na opcje nr 1'
}
TEXT_ERROR_PATH = {
    'equ_fol': 'Folder z danymi ma niepoprawna liczbę folderów głwnych',
    'not_find_set_name': 'Folder z danymi posiada niepoprawne nazwy folderów',
    'not_fol': 'Folder głowny zawiera  plik nie będący folderem',
    'p_is_emp': 'Pod folder jest pusty',
    'p_not_eq': 'Liczba pod folderów jest różna',
    'p_name': 'Nazwa podfolderów jest różna',
    'p_not_fol': 'Pod folder niejest folderem',
    'p_name_csv': 'Pod foldery ma złe nazewnictwo',
    'i_not_img': 'Folder z zdieciami niejest zdiecie',
    'i_emp': 'Folder z zdieciami jest pusty'
}


class CheckData:
    """ Klasa sprawdzająca poprawnosc podanych danych w klasie first_win """

    def __init__(self):
        """ Definiowanie zmiennych klasy """
        self.__path = None

    @staticmethod
    def check_type(data) -> None:
        """ Sprawdzanie poprawniosci ramki z typem sieci """
        if not data:
            raise ValueError(TEXT_ERROR_TYPE)

    @staticmethod
    def check_learn_opt(data, epoch) -> None:
        """ Sprawdzanie poprawniosci ramki z opcją przeszukiwania """
        if not data:
            raise ValueError(TEXT_ERROR_OPT['not_check'])

        if data == IF_SECOND_OPT:
            if not epoch:
                raise ValueError(TEXT_ERROR_OPT['empty'])

            try:
                int(epoch)
            except ValueError:
                raise ValueError(TEXT_ERROR_OPT['not_num'])

            if int(epoch) <= NEG:
                raise ValueError(TEXT_ERROR_OPT['is_neg'])

            if int(epoch) > IS_BIG:
                raise ValueError(TEXT_ERROR_OPT['is_big'])

    def check_data_img(self, data) -> None:
        """ Sprawdzanie poprawniosci ramki z scieżka do danych dla
        kolwolucji """
        self.__path = data

        self.__is_path(data)
        self.__check_main_fol_img()
        self.__check_emot_fol_img()
        self.__check_fol_img()

    def check_data_csv(self, data) -> None:
        """ Sprawdzanie poprawniosci ramki z scieżki do damymi dla neuronów """
        self.__path = data
        self.__is_path(data)

        self.__check_main_fol_csv()

    @staticmethod
    def __is_path(data) -> None:
        """ Funkcja sprawdza czy scierzka do folderu istnieje """
        if not data:
            raise ValueError('Nie podano scierzki do bazy danych')

    def __check_main_fol_img(self) -> None:
        """ Sprawdzenie czy główny folder dla konwolucji ma poprawną
        strtukture """
        main_fol = os.listdir(self.__path)

        if not len(main_fol) == SIZE_MAIN_FOL:
            raise ValueError(TEXT_ERROR_PATH['equ_fol'])

        for fol in main_fol:
            if fol.count(DOT):
                raise ValueError(TEXT_ERROR_PATH['not_fol'])

        if not SET_MAIN_FOL == main_fol:
            raise ValueError(TEXT_ERROR_PATH['not_find_set_name'])

    def __check_emot_fol_img(self) -> None:
        """ Sprawdzenie czy pod foldery dla konwolucji mają poprawna budowe """
        path_test = os.path.join(self.__path, SET_MAIN_FOL[FIRST_IND])
        path_val = os.path.join(self.__path, SET_MAIN_FOL[SECOND_IND])

        test_fol = os.listdir(path_test)
        val_fol = os.listdir(path_val)

        if not len(test_fol):
            raise ValueError(TEXT_ERROR_PATH['p_is_emp'])

        if not len(val_fol):
            raise ValueError(TEXT_ERROR_PATH['p_is_emp'])

        if not len(test_fol) == len(val_fol):
            raise ValueError(TEXT_ERROR_PATH['p_not_eq'])

        if not test_fol == val_fol:
            raise ValueError(TEXT_ERROR_PATH['p_name'])

        for row in test_fol:
            if row.count(DOT):
                raise ValueError(TEXT_ERROR_PATH['p_not_fol'])

        for row in val_fol:
            if row.count(DOT):
                raise ValueError(TEXT_ERROR_PATH['p_not_fol'])

    def __check_fol_img(self) -> None:
        """ Sprawdzanie czy folder posiada tylko zdiecia """
        for set_name in SET_MAIN_FOL:
            path = os.path.join(self.__path, set_name)
            path_test = [os.path.join(path, i) for i in os.listdir(path)]

            for row in path_test:
                data = os.listdir(row)

                if not data:
                    raise ValueError(TEXT_ERROR_PATH['i_emp'])

                for mame in data:
                    if PNG in mame:
                        raise ValueError(TEXT_ERROR_PATH['i_not_img'])

    def __check_main_fol_csv(self) -> None:
        """ Sprawdzenie czy folder posiada odpowiednia strukture dla sieci
        neuronowej """
        list_fol = os.listdir(self.__path)

        if not len(list_fol):
            raise ValueError(TEXT_ERROR_PATH['p_is_emp'])

        if not len(list_fol) == len(SET_MAIN_FOL_CSV):
            raise ValueError(TEXT_ERROR_PATH['p_not_eq'])

        if not SET_MAIN_FOL_CSV == list_fol:
            raise ValueError(TEXT_ERROR_PATH['p_name_csv'])
