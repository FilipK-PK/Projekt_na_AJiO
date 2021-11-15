""" laarn_neuron.py """
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
RANDOM = 'random_uniform'
USE_BIAS = True
FUN_ACTIVATION = ['relu', 'tanh', 'softmax']
FUN_COMPILATOR = [optimizers.Adam, optimizers.RMSprop, optimizers.SGD]
SOFTMAX = 'softmax'


class LearnNeuron:
    """ Klasa przekształca tablice na gotowy model """

    def __init__(self,  len_lay, size_neuron):
        """ Definiowanie zmiennych klasy """
        self.__len_lay = len_lay
        self.__size_lay = size_neuron
        self.__model = None
        self.__vec = None
        self.__neu_vec = None
        self.__end_lay = None

    def create_model(self, vec, end_lay) -> Sequential:
        """ Tworzenie modelu neuronowego"""
        self.__vec = vec
        self.__end_lay = end_lay
        self.__transform_neu_vec()
        self.__model = Sequential()
        self.__set_end_lay()
        self.__create_lay()

        return self.__model

    def __transform_neu_vec(self) -> None:
        """ Przekształcanie tablicy w pod tablice """
        self.__neu_vec = []

        start = FIRST_IN + self.__len_lay[CON_LAY] * CON_SIZE
        stop = start + self.__len_lay[NEU_LAY] * NEU_SIZE

        for i in range(start, stop, NEU_SIZE):
            self.__neu_vec.append(self.__vec[i: i + NEU_SIZE])

    def __create_lay(self) -> None:
        """ Przekształcanie pod tablicy w model sieci """
        self.__model.add(Input(shape=self.__size_lay))

        for row in self.__neu_vec:
            for _ in range(row[IND_REPET_LAY]):
                self.__model.add(layers.Dense(
                    row[IND_SIZE_LAY], use_bias=USE_BIAS,
                    activation=FUN_ACTIVATION[row[IND_ACT]],
                    kernel_initializer=RANDOM, bias_initializer=RANDOM
                ))

                if row[IND_DROP]:
                    self.__model.add(layers.Dropout(row[IND_DROP]))

        self.__model.compile(
            loss=losses.sparse_categorical_crossentropy,
            optimizer=FUN_COMPILATOR[
                self.__vec[IND_OPT]
            ](learning_rate=self.__vec[IND_LR]),
            metrics=[SET_PROP]
        )

    def __set_end_lay(self) -> None:
        """ Definiowanie ostatniej warstwy modelu """
        self.__model.add(layers.Dense(
            self.__end_lay, activation=SOFTMAX, use_bias=USE_BIAS,
            kernel_initializer=RANDOM, bias_initializer=RANDOM
        ))
