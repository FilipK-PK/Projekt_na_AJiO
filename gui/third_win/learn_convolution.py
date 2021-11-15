""" learn_convolution.py """
from tensorflow.keras import Sequential, layers, losses
from tensorflow.keras import Input, optimizers


FIRST_IN = 2
CON_LAY, NEU_LAY = 0, 1
NEU_SIZE = 4
CON_SIZE = 5
IND_ACT = 0
IND_LR = 0
IND_OPT = 1
IND_REPET_LAY = 3
IND_SIZE_LAY = 1
IND_DROP = 2
SIZE_LAY = 1
SET_PROP = 'accuracy'
FUN_ACTIVATION = ['relu', 'tanh', 'softmax']
FUN_COMPILATOR = [optimizers.Adam, optimizers.RMSprop, optimizers.SGD]
RANDOM = 'random_uniform'
USE_BIAS = True
PADDING_NAME = 'same'
IND_REPET_CON = 2
IND_FILTR = 4
ACT_CON2 = 'relu'
IND_SIZE_CON = 0
IND_BATCH = 1
IND_MAXPOOL = 3
SOFTMAX = 'softmax'


class LearnConvolution:
    """ Klasa przekształca dane z tabeli na gotowy model """

    def __init__(self,  len_lay, size_neuron):
        """ Definiowanie zmiennych klasy """
        self.__len_lay = len_lay
        self.__size_lay = size_neuron
        self.__model = None
        self.__vec = None
        self.__con_vec = None
        self.__end_lay = None

    def create_model(self, vec, end_lay) -> Sequential:
        """ Funkcja tworzy model konwolucjny """
        self.__vec = vec
        self.__end_lay = end_lay
        self.__transform_vec()
        self.__model = Sequential()
        self.__create_con_lay()
        self.__create_neu_lay()
        self.__set_end_lay()
        self.__add_compile()

        return self.__model

    def __transform_vec(self) -> None:
        """ Przekształcanie tablicy z wartosciami na pod tablice dla kazdej z
        sieci """
        self.__con_vec = []
        self.__neu_vec = []

        start = FIRST_IN
        stop = start + self.__len_lay[CON_LAY] * CON_SIZE

        for i in range(start, stop, CON_SIZE):
            self.__con_vec.append(self.__vec[i: i + CON_SIZE])

        start = stop
        stop = start + self.__len_lay[NEU_LAY] * NEU_SIZE

        for i in range(start, stop, NEU_SIZE):
            self.__neu_vec.append(self.__vec[i: i + NEU_SIZE])

    def __create_con_lay(self) -> None:
        """ Funkcja przekształca pod tabele na warstwy konwolucjne """
        self.__model.add(Input(shape=self.__size_lay))

        for row in self.__con_vec:
            for _ in range(row[IND_REPET_CON]):
                self.__model.add(layers.Conv2D(
                    row[IND_SIZE_CON], (row[IND_FILTR], row[IND_FILTR]),
                    activation=ACT_CON2, padding=PADDING_NAME,
                    ))

                if row[IND_BATCH]:
                    self.__model.add(layers.BatchNormalization())

            self.__model.add(layers.MaxPooling2D(
                (row[IND_MAXPOOL], row[IND_MAXPOOL])
            ))

    def __create_neu_lay(self) -> None:
        """ Funkcja przekształca pod tablice na warstwy neuronowe """
        self.__model.add(layers.Flatten())

        for row in self.__neu_vec:
            for _ in range(row[IND_REPET_LAY]):
                self.__model.add(layers.Dense(
                    row[IND_SIZE_LAY], use_bias=USE_BIAS,
                    activation=FUN_ACTIVATION[row[IND_ACT]],
                    kernel_initializer=RANDOM, bias_initializer=RANDOM
                ))

                if row[IND_DROP]:
                    self.__model.add(layers.Dropout(row[IND_DROP]))

    def __add_compile(self) -> None:
        """ Funkcja definiuje znienne kompilacji modelu """
        self.__model.compile(
            loss=losses.categorical_crossentropy,
            optimizer=FUN_COMPILATOR[
                self.__vec[IND_OPT]
            ](learning_rate=self.__vec[IND_LR]),
            metrics=[SET_PROP]
        )

    def __set_end_lay(self) -> None:
        """ Funkcja definiuje ostatnia warstwe modelu """
        self.__model.add(layers.Dense(
            self.__end_lay, activation=SOFTMAX, use_bias=USE_BIAS,
            kernel_initializer=RANDOM, bias_initializer=RANDOM
        ))
