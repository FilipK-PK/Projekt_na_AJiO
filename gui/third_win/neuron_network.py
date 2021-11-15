""" neuron_network.py """
from gui.third_win import learn_neuron, learn_convolution
from tensorflow.keras import callbacks, preprocessing

import numpy as np
import os
import csv


CONVOLUTION = 2
NEURON = 1
SAVE_BEST = True
IF_NEU = 1
LEN_OPT_ = 2
LEN_CON = 5
LEN_NEU = 4
VIEW_FIT = 1
MAX_OVERFIT = 500
ACT_OVERFIT = 10
READ = 'r'
NEU_SET_LOAD = ['train_x.csv', 'train_y.csv', 'val_x.csv', 'val_y.csv']
MONITOR = 'val_loss'
IND_DATA_NEU = 0
IND_ANS_NEU = 1
REDUCE_IND = -1
SHAPE_IN = 1
NEW_LINE = '\t'
EMPTY = []
SEP = ','
FIRST_IND = 0
SECOND_IND = 1
IND_DATA_TRAIN = 0
IND_ANWS_TRAIN = 1
IND_DATA_VAL = 2
IND_ANWS_VAL = 3
TO_VEC = -1
TO_ONE_EL = 1
MIN_DELTA = 0
SIZE_IMG = 96
TARG_IMG = (SIZE_IMG, SIZE_IMG)
RESCALE_IMG = 1/255.0
ROTATE_IMG = 20
ROT_VER_IMG = True
CATEGOY = 'categorical'
TRAIN_FOL = 'train'
VAL_FOL = 'val'
NO = False
ERROR_FIT = 404


class NeuronNetwork:
    """ Klasa zwraca wynik uczenia danego modelu """

    def __init__(self, typ, opt, path, lay_size):
        """ Definiowanie zmiennych klasy """
        self.__typ = typ
        self.__opt = opt[IND_DATA_NEU] + REDUCE_IND
        self.__opt_epoch = opt[IND_ANS_NEU]
        self.__path = path
        self.__how_lay = lay_size
        self.__data_test = None
        self.__data_val = None
        self.__get_con_model = None
        self.__get_neu_model = None

        self.__load_data()
        self.__set_class_neu() if typ == NEURON else self.__set_class_con()
        self.__set_fun_opt()

    def test_model(self, vec) -> float:
        """ Funkcja uruchamia klase odpowiedzialna za uczenie danej sieci """
        end_lay = self.__get_end_lay()

        if self.__typ == CONVOLUTION:
            model = self.__get_con_model.create_model(vec, end_lay)
        else:
            model = self.__get_neu_model.create_model(vec, end_lay)

        return self.__fun_check_model[self.__opt](model)

    def __set_class_neu(self) -> None:
        """ Zapisywanie do zmiennej klasy funkcji twozacej model neuronowy """
        self.__get_neu_model = learn_neuron.LearnNeuron(
            self.__how_lay, self.__data_test[IND_DATA_NEU].shape[SHAPE_IN:]
        )

    def __set_class_con(self) -> None:
        """ Zapisywanie do zmiennej klasy funkcji twozacej model konwolucjny """
        self.__get_con_model = learn_convolution.LearnConvolution(
            self.__how_lay,
            self.__data_test.next()[FIRST_IND].shape[SHAPE_IN:]
        )

    def __set_fun_opt(self) -> None:
        """ """
        self.__fun_check_model = [
            self.__option_overfit, self.__option_static_epoch,
            # self.__option_cascade, self.__option_epochal
        ]

    def __load_data(self) -> None:
        """ Pobieranie zbioru uczacego w zaleznoaci od podanej sieci """
        if self.__typ == CONVOLUTION:
            self.__load_data_img()
        else:
            self.__load_data_csv()

    def __load_data_img(self) -> None:
        """ Pobieranie danych dal konwolucji """
        train_gen = preprocessing.image.ImageDataGenerator(
            rescale=RESCALE_IMG, rotation_range=ROTATE_IMG,
            vertical_flip=ROT_VER_IMG
        )

        val_gen = preprocessing.image.ImageDataGenerator(rescale=RESCALE_IMG)

        self.__data_test = train_gen.flow_from_directory(
            os.path.join(self.__path, TRAIN_FOL),
            target_size=TARG_IMG, class_mode=CATEGOY
        )

        self.__data_val = val_gen.flow_from_directory(
            os.path.join(self.__path, VAL_FOL),
            target_size=TARG_IMG, class_mode=CATEGOY, shuffle=NO
        )

    def __load_data_csv(self) -> None:
        """ Pobieeranie danych dla sieci neuronowych """
        data = []

        for name_set in NEU_SET_LOAD:
            path = os.path.join(self.__path, name_set)
            x = []

            with open(path, READ) as file:
                reader = csv.reader(file, delimiter=NEW_LINE)
                for row in reader:
                    x.append(
                        [float(i) for i in row[FIRST_IND].split(SEP)]
                    )
            data.append(x)

        self.__data_test = (
            np.array(data[IND_DATA_TRAIN]),
            np.array(data[IND_ANWS_TRAIN]).reshape(TO_VEC, TO_ONE_EL)
        )
        self.__data_val = (
            np.array(data[IND_DATA_VAL]),
            np.array(data[IND_ANWS_VAL]).reshape(TO_VEC, TO_ONE_EL)
        )

    def __option_overfit(self, model) -> float:
        """ Uczeni opcja do wykrycia przeuczenia """
        callback = [
            callbacks.EarlyStopping(
                monitor=MONITOR, min_delta=MIN_DELTA, patience=ACT_OVERFIT,
                verbose=VIEW_FIT, restore_best_weights=SAVE_BEST)
        ]

        history = model.fit(
            self.__data_test[FIRST_IND] if self.__typ == IF_NEU
            else self.__data_test,
            self.__data_test[SECOND_IND] if self.__typ == IF_NEU else None,
            epochs=MAX_OVERFIT,
            verbose=VIEW_FIT,
            callbacks=callback,
            validation_data=self.__data_val
        )

        return np.min(history.history[MONITOR])

    def __option_static_epoch(self, model) -> float:
        """ Uczenie opcja  zdefiniowana liczba epok """
        try:
            history = model.fit(
                x=self.__data_test[FIRST_IND] if self.__typ == IF_NEU
                else self.__data_test,
                y=self.__data_test[SECOND_IND] if self.__typ == IF_NEU else None,
                epochs=self.__opt_epoch,
                verbose=VIEW_FIT,
                validation_data=self.__data_val
            )
        except ValueError:
            return ERROR_FIT
        else:
            minimum = np.min(history.history[MONITOR])
            return minimum if minimum >= FIRST_IND else ERROR_FIT

    def __get_end_lay(self) -> int:
        """ Zwraca liczbe warstw dla ostatniej warstwy """
        if self.__typ == CONVOLUTION:
            return len(os.listdir(os.path.join(self.__path, TRAIN_FOL)))

        data = []
        for i in self.__data_test[SECOND_IND]:
            if i not in data:
                data.append(i)

        return len(data)
