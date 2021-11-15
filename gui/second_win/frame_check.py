""" frame_check.py """


ON = 1
INDEX = 1
FOR = ' dla '
FOR_ROW = ' dla wiersza nr '
IN = ' w '
CHAR_SEP = ','
GOOD_CHAR = '0123456789., -'
CHAR_FOLOAT = '.'
ZERO, ONE, TWO = 0.0, 1.0, 2
NON_NEU_LAY = 'Wymagan jest przynajmniej jedna warstwa sieci neuronowej'
NON_CON_LAY = 'Wymagan jest przynajmniej jedna warstwa sieci konwolucjnej'

MAIN_OPTION = {
    'opt': 'opcji początkowych', 'con': 'warstwie konwolucjnej',
    'neu': 'warstwie neuronowej'
}

OPT_OPTION = {'lr': 0, 'check': 1}
OPT_CONT = {'lr': 'skoku uczenia', 'check': 'optymalizatora'}

CON_ITEM = ['size_lay', 'repet_lay', 'poll', 'filter']
CON_ABB = ['size', 'rep', 'poll', 'fil']
CON_OPTION = {'size_lay': 0, 'bath': 1, 'repet_lay': 2, 'poll': 3, 'filter': 4}
CON_CONT = {'size_lay': 'rozmiaru warstwy', 'repet_lay': 'liczby powturzen',
            'bath': '', 'poll': 'maxpollingu', 'filter': 'rozmiaru filtru'}

NEU_ITEM, NEU_ABB = ['size_lay', 'drop', 'repet'], ['size', 'drop', 'repet']
NEU_OPTION = {'check': 0, 'size_lay': 1, 'drop': 2, 'repet': 3}
NEU_CONT = {
    'check': 'funkcji optymalizacji', 'size_lay': 'rozmiaru warstwy',
    'drop': 'drop', 'repet': 'liczby powturzen warstwy'
}

ERROR = {
    'empty': 'Nie podano zadnej wartosci',
    'unrec_char': 'Wykryto nieprawidłowy znak',
    'wrong_order': 'Nieprawidłowa składnia',
    'num_out_01': 'Rozpoznano liczbę nie nalezącą do zbioru (0, 1)',
    'not_check': 'Nie zaznaczono zadnej opcji',
    'not_int': 'Wykryto nie liczbę całkowitą',
    'not_neg': 'Liczba niemoze byc ujemna',
    'not_div': 'Liczba musi byc parzysta',
    'not_ndiv': 'Liczba musi byc nieparzysta'
}

TEXT_ERROR = {
    'empty_lr_option': (
            ERROR['empty'] + FOR + OPT_CONT['lr'] + IN + MAIN_OPTION['opt']),
    'unrec_c_option': (
            ERROR['unrec_char'] + FOR + OPT_CONT['lr'] + IN + MAIN_OPTION['opt']),
    'wrong_oder_option': (
            ERROR['wrong_order'] + FOR + OPT_CONT['lr'] + IN + MAIN_OPTION['opt']),
    'num_not_01_option': (
            ERROR['num_out_01'] + FOR + OPT_CONT['lr'] + IN + MAIN_OPTION['opt']),
    'not_check_option': (
            ERROR['not_check'] + FOR + OPT_CONT['check'] + IN + MAIN_OPTION['opt']),
    'not_neg_check_option': (
            ERROR['not_neg'] + FOR + OPT_CONT['check'] + IN + MAIN_OPTION['opt']),

    'empty_size_con': (
            ERROR['empty'] + FOR + CON_CONT['size_lay'] + IN + MAIN_OPTION['con']),
    'unrec_c_size_con': (
            ERROR['unrec_char'] + FOR + CON_CONT['size_lay'] + IN + MAIN_OPTION['con']),
    'wrong_size_con': (
            ERROR['wrong_order'] + FOR + CON_CONT['size_lay'] + IN + MAIN_OPTION['con']),
    'not_int_size_con': (
            ERROR['not_int'] + FOR + CON_CONT['size_lay'] + IN + MAIN_OPTION['con']),
    'not_neg_size_con': (
            ERROR['not_neg'] + FOR + CON_CONT['size_lay'] + IN + MAIN_OPTION['con']),

    'empty_rep_con': (
            ERROR['empty'] + FOR + CON_CONT['repet_lay'] + IN + MAIN_OPTION['con']),
    'unrec_c_rep_con': (
            ERROR['unrec_char'] + FOR + CON_CONT['repet_lay'] + IN + MAIN_OPTION['con']),
    'wrong_rep_con': (
            ERROR['wrong_order'] + FOR + CON_CONT['repet_lay'] + IN + MAIN_OPTION['con']),
    'not_int_rep_con': (
            ERROR['not_int'] + FOR + CON_CONT['repet_lay'] + IN + MAIN_OPTION['con']),
    'not_neg_rep_con': (
            ERROR['not_neg'] + FOR + CON_CONT['repet_lay'] + IN + MAIN_OPTION['con']),

    'empty_poll_con': (
            ERROR['empty'] + FOR + CON_CONT['poll'] + IN + MAIN_OPTION['con']),
    'unrec_c_poll_con': (
            ERROR['unrec_char'] + FOR + CON_CONT['poll'] + IN + MAIN_OPTION['con']),
    'wrong_poll_con': (
            ERROR['wrong_order'] + FOR + CON_CONT['poll'] + IN + MAIN_OPTION['con']),
    'not_int_poll_con': (
            ERROR['not_int'] + FOR + CON_CONT['poll'] + IN + MAIN_OPTION['con']),
    'not_neg_poll_con': (
            ERROR['not_neg'] + FOR + CON_CONT['poll'] + IN + MAIN_OPTION['con']),
    'not_div_poll_con': (
            ERROR['not_div'] + FOR + CON_CONT['poll'] + IN + MAIN_OPTION['con']),

    'empty_fil_con': (
            ERROR['empty'] + FOR + CON_CONT['filter'] + IN + MAIN_OPTION['con']),
    'unrec_c_fil_con': (
            ERROR['unrec_char'] + FOR + CON_CONT['filter'] + IN + MAIN_OPTION['con']),
    'wrong_fil_con': (
            ERROR['wrong_order'] + FOR + CON_CONT['filter'] + IN + MAIN_OPTION['con']),
    'not_int_fil_con': (
            ERROR['not_int'] + FOR + CON_CONT['filter'] + IN + MAIN_OPTION['con']),
    'not_neg_fil_con': (
            ERROR['not_neg'] + FOR + CON_CONT['filter'] + IN + MAIN_OPTION['con']),
    'not_ndiv_fil_con': (
            ERROR['not_ndiv'] + FOR + CON_CONT['filter'] + IN + MAIN_OPTION['con']),

    'not_check_neu': (
            ERROR['not_check'] + FOR + NEU_CONT['check'] + IN + MAIN_OPTION['neu']),
    'empty_lr_neu': (
            ERROR['empty'] + FOR + NEU_CONT['drop'] + IN + MAIN_OPTION['neu']),
    'unrec_c_neu': (
            ERROR['unrec_char'] + FOR + NEU_CONT['drop'] + IN + MAIN_OPTION['neu']),
    'wrong_oder_neu': (
            ERROR['wrong_order'] + FOR + NEU_CONT['drop'] + IN + MAIN_OPTION['neu']),
    'num_not_01_neu': (
            ERROR['num_out_01'] + FOR + NEU_CONT['drop'] + IN + MAIN_OPTION['neu']),
    'not_neg_check_neu': (
            ERROR['not_neg'] + FOR + NEU_CONT['drop'] + IN + MAIN_OPTION['neu']),

    'empty_size_neu': (
            ERROR['empty'] + FOR + NEU_CONT['size_lay'] + IN + MAIN_OPTION['neu']),
    'unrec_c_size_neu': (
            ERROR['unrec_char'] + FOR + NEU_CONT['size_lay'] + IN + MAIN_OPTION['neu']),
    'wrong_size_neu': (
            ERROR['wrong_order'] + FOR + NEU_CONT['size_lay'] + IN + MAIN_OPTION['neu']),
    'not_int_size_neu': (
            ERROR['not_int'] + FOR + NEU_CONT['size_lay'] + IN + MAIN_OPTION['neu']),
    'not_neg_size_neu': (
            ERROR['not_neg'] + FOR + NEU_CONT['size_lay'] + IN + MAIN_OPTION['neu']),

    'empty_drop_neu': (
            ERROR['empty'] + FOR + NEU_CONT['drop'] + IN + MAIN_OPTION['neu']),
    'unrec_c_drop_neu': (
            ERROR['unrec_char'] + FOR + NEU_CONT['drop'] + IN + MAIN_OPTION['neu']),
    'wrong_drop_neu': (
            ERROR['wrong_order'] + FOR + NEU_CONT['drop'] + IN + MAIN_OPTION['neu']),
    'not_01_drop_neu': (
            ERROR['num_out_01'] + FOR + NEU_CONT['drop'] + IN + MAIN_OPTION['neu']),
    'not_neg_drop_neu': (
            ERROR['not_neg'] + FOR + NEU_CONT['drop'] + IN + MAIN_OPTION['neu']),

    'empty_repet_neu': (
            ERROR['empty'] + FOR + NEU_CONT['repet'] + IN + MAIN_OPTION['neu']),
    'unrec_c_repet_neu': (
            ERROR['unrec_char'] + FOR + NEU_CONT['repet'] + IN + MAIN_OPTION['neu']),
    'wrong_repet_neu': (
            ERROR['wrong_order'] + FOR + NEU_CONT['repet'] + IN + MAIN_OPTION['neu']),
    'not_int_repet_neu': (
            ERROR['not_int'] + FOR + NEU_CONT['repet'] + IN + MAIN_OPTION['neu']),
    'not_neg_repet_neu': (
            ERROR['not_neg'] + FOR + NEU_CONT['repet'] + IN + MAIN_OPTION['neu']),
}


class FrameCheck:
    """ Klasa sprawdzająca czy poddane dane warstwy sa poprawnie
    zdefiniowane """

    def check_options(self, data):
        """ Sprawdzanie tablicy z wprowadzonymi danymi dla optymalizatora """
        self.__empty_entry(
            data[OPT_OPTION['lr']], TEXT_ERROR['empty_lr_option'])
        self.__is_good_char(
            data[OPT_OPTION['lr']], TEXT_ERROR['unrec_c_option'])
        self.__is_split(
            data[OPT_OPTION['lr']], TEXT_ERROR['wrong_oder_option'])
        self.__is_01(
            data[OPT_OPTION['lr']], TEXT_ERROR['num_not_01_option'])
        self.__is_neg(
            data[OPT_OPTION['lr']], TEXT_ERROR['not_neg_check_option'])

        self.__is_check_opt(
            data[OPT_OPTION['check']], TEXT_ERROR['not_check_option'])

    def check_convolution(self, data) -> None:
        """ Sprawdzanie tablicy z wprowadzonymi danymi dal sieci
        konwolucjnej """
        if not len(data):
            raise ValueError(NON_CON_LAY)

        for i, row in enumerate(data):
            index = FOR_ROW + str(i+INDEX)

            for name, avat in zip(CON_ITEM, CON_ABB):
                self.__empty_entry(
                    row[CON_OPTION[name]],
                    TEXT_ERROR['empty_' + avat + '_con'] + index)
                self.__is_good_char(
                    row[CON_OPTION[name]],
                    TEXT_ERROR['unrec_c_' + avat + '_con'] + index)
                self.__is_split(
                    row[CON_OPTION[name]],
                    TEXT_ERROR['wrong_' + avat + '_con'] + index)
                self.__is_int(
                    row[CON_OPTION[name]],
                    TEXT_ERROR['not_int_' + avat + '_con'] + index)
                self.__is_neg(
                    row[CON_OPTION[name]],
                    TEXT_ERROR['not_neg_' + avat + '_con'] + index)

                if name == 'poll':
                    self.__is_div(
                        row[CON_OPTION[name]],
                        TEXT_ERROR['not_div_' + avat + '_con'] + index)

                if name == 'filter':
                    self.__is_ndiv(
                        row[CON_OPTION[name]],
                        TEXT_ERROR['not_ndiv_' + avat + '_con'] + index)

    def check_neuron(self, data) -> None:
        """ Sprawdzanie tablicy z wprowadzonymi danymi dal sieci neuronowej """
        if not len(data):
            raise ValueError(NON_NEU_LAY)

        for i, row in enumerate(data):
            index = FOR_ROW + str(i + INDEX)

            self.__is_check_opt(
                row[NEU_OPTION['check']], TEXT_ERROR['not_check_neu'] + index)

            for name, awat in zip(NEU_ITEM, NEU_ABB):
                self.__empty_entry(
                    row[NEU_OPTION[name]],
                    TEXT_ERROR['empty_' + awat + '_neu'] + index)
                self.__is_good_char(
                    row[NEU_OPTION[name]],
                    TEXT_ERROR['unrec_c_' + awat + '_neu'] + index)
                self.__is_split(
                    row[NEU_OPTION[name]],
                    TEXT_ERROR['wrong_' + awat + '_neu'] + index)
                self.__is_neg(
                    row[NEU_OPTION[name]],
                    TEXT_ERROR['not_neg_' + awat + '_neu'] + index)

                if name == 'drop':
                    self.__is_01(
                        row[NEU_OPTION[name]],
                        TEXT_ERROR['not_01_' + awat + '_neu'] + index)

                if 'size_lay' == name or name == 'repet':
                    self.__is_int(
                        row[NEU_OPTION[name]],
                        TEXT_ERROR['not_int_' + awat + '_neu'] + index)

    @staticmethod
    def __is_check_opt(data, text_error) -> None:
        """ Sprawdzenie czy zaznaczono przynajmniej jedna opcje """
        if not data.count(ON):
            raise ValueError(text_error)

    @staticmethod
    def __empty_entry(data, text_error) -> None:
        """ Sprawdzenie czy podano wartosc """
        if not data:
            raise ValueError(text_error)

    @staticmethod
    def __is_good_char(data, text_error) -> None:
        """ Sprawdzenie czy wszystkie znaki sa dozwolone """
        if data.lstrip(GOOD_CHAR):
            raise ValueError(text_error)

    @staticmethod
    def __is_split(data, text_error) -> None:
        """ Sprawdzenie czy da sie podzielic ',' na odcinki kture sa liczba """
        try:
            [float(num) for num in data.split(CHAR_SEP)]
        except ValueError:
            raise ValueError(text_error)

    @staticmethod
    def __is_int(data, text_error):
        """ Sprawdza czy liczba jest całkowita """
        if data.count(CHAR_FOLOAT):
            raise ValueError(text_error)

    @staticmethod
    def __is_01(data, text_error) -> None:
        """ Sprawdzenie czy liczba nalezy do przedziału [0,1) """
        for num in data.split(CHAR_SEP):
            if ZERO < float(num) >= ONE:
                raise ValueError(text_error)

    @staticmethod
    def __is_neg(data, text_error) -> None:
        """ Sprawdzenie czy liczba jest <=0 """
        for num in data.split(CHAR_SEP):
            if float(num) <= ZERO:
                raise ValueError(text_error)

    @staticmethod
    def __is_div(data, text_error) -> None:
        """ Sprawdzenie czy liczba jest parzysta """
        for num in data.split(CHAR_SEP):
            if int(num) % TWO:
                raise ValueError(text_error)

    @staticmethod
    def __is_ndiv(data, text_error) -> None:
        """ Sprawdzenie czy liczba jest nieparzysta """
        for num in data.split(CHAR_SEP):
            if not int(num) % TWO:
                raise ValueError(text_error)
