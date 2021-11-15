""" testy.py """
from gui.first_win import check_data
from gui.second_win import frame_check

import unittest


class Test(unittest.TestCase):
    """ Klasa do testowania jednostkowego """

    def test_first_win(self) -> None:
        """ Testy jednostkowe dla okna poczatkowego """
        test = check_data.CheckData()

        """ Testowanie opcji sieci """
        self.assertRaises(ValueError, test.check_type, '')

        """ Testowanie funkcji selekcji """
        self.assertRaises(ValueError, test.check_learn_opt, '', '')
        self.assertRaises(ValueError, test.check_learn_opt, 2, '')
        self.assertRaises(ValueError, test.check_learn_opt, 2, 'e')
        self.assertRaises(ValueError, test.check_learn_opt, 2, '2000')
        self.assertRaises(ValueError, test.check_learn_opt, 2, '-1')
        self.assertRaises(ValueError, test.check_learn_opt, 2, '0.3')

    def test_search_win_opt(self) -> None:
        """ Testy jednostkowe dla optymalizatora w search_win"""
        test = frame_check.FrameCheck()

        self.assertRaises(
            ValueError, test.check_options, ['0.1, 0.01', [0, 0, 0]]
        )
        self.assertRaises(
            ValueError, test.check_options, ['1, 0.01', [0, 1, 0]]
        )
        self.assertRaises(
            ValueError, test.check_options, ['0.1, a', [0, 1, 0]]
        )
        self.assertRaises(
            ValueError, test.check_options, ['0.1, -0.3', [0, 1, 0]]
        )
        self.assertRaises(
            ValueError, test.check_options, ['0..0,,3', [0, 1, 0]]
        )
        self.assertRaises(ValueError, test.check_options, ['', [0, 1, 0]])

    def test_search_win_neuron(self) -> None:
        """ Testy jednostkowe dla f.aktywacji w search_win"""
        test = frame_check.FrameCheck()

        """ F.aktywacji """
        self.assertRaises(
            ValueError, test.check_neuron,
            [[[0, 0, 0], '64, 256', '0.2, 0.5', '3']]
        )

        """ Rozmiar warstw """
        self.assertRaises(
            ValueError, test.check_neuron, [[[1, 0, 0], '', '0.2, 0.5', '3']]
        )
        self.assertRaises(
            ValueError, test.check_neuron, [[[1, 0, 0], 'a', '0.2, 0.5', '3']]
        )
        self.assertRaises(
            ValueError, test.check_neuron, [[[1, 0, 0], '-4', '0.2, 0.5', '3']]
        )
        self.assertRaises(
            ValueError, test.check_neuron, [[[1, 0, 0], '5.3', '0.2, 0.5', '3']]
        )
        self.assertRaises(
            ValueError, test.check_neuron,
            [[[1, 0, 0], '64,,64', '0.2, 0.5', '3']]
        )

        """ Droup """
        self.assertRaises(
            ValueError, test.check_neuron, [[[1, 0, 0], '64, 256', '', '3']]
        )
        self.assertRaises(
            ValueError, test.check_neuron, [[[1, 0, 0], '64, 256', 'a', '3']]
        )
        self.assertRaises(
            ValueError, test.check_neuron, [[[1, 0, 0], '64, 256', '-1', '3']]
        )
        self.assertRaises(
            ValueError, test.check_neuron, [[[1, 0, 0], '64, 256', '1', '3']]
        )
        self.assertRaises(
            ValueError, test.check_neuron,
            [[[1, 0, 0], '64, 256', '0.4,,0.2', '3']]
        )

        """ Powturzenia warstwy """
        self.assertRaises(
            ValueError, test.check_neuron,
            [[[0, 1, 0], '64, 256', '0.2, 0.5', '']]
        )
        self.assertRaises(
            ValueError, test.check_neuron,
            [[[0, 1, 0], '64, 256', '0.2, 0.5', 'a']]
        )
        self.assertRaises(
            ValueError, test.check_neuron,
            [[[0, 1, 0], '64, 256', '0.2, 0.5', '-3']]
        )
        self.assertRaises(
            ValueError, test.check_neuron,
            [[[0, 1, 0], '64, 256', '0.2, 0.5', '4.2']]
        )
        self.assertRaises(
            ValueError, test.check_neuron,
            [[[0, 1, 0], '64, 256', '0.2, 0.5', '0..4,,4']]
        )

        """ Wiele warstw """
        self.assertRaises(
            ValueError, test.check_neuron,
            [[[0, 1, 0], '64', '0.2', '3'], [[0, 0, 0], '64', '0.2', '3']]
        )
        self.assertRaises(
            ValueError, test.check_neuron,
            [[[0, 1, 0], '64', '0.2', '3'], [[0, 1, 0], 's', '0.2', '3']]
        )
        self.assertRaises(
            ValueError, test.check_neuron,
            [[[0, 1, 0], '64', '0.2', '3'], [[0, 1, 0], '64', '2', '3']]
        )
        self.assertRaises(
            ValueError, test.check_neuron,
            [[[0, 1, 0], '64', '0.2', '3'], [[0, 1, 0], '64', '0.2', '0']]
        )

    def test_search_win_convolution(self) -> None:
        """ Testy jednostkowe dla konwolucji w search_win """
        test = frame_check.FrameCheck()

        """ Rozmiar warstw """
        self.assertRaises(
            ValueError, test.check_convolution,
            [['', 0, '1, 2', '4, 6', '3, 5']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['a', 0, '1, 2', '4, 6', '3, 5']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['0', 0, '1, 2', '4, 6', '3, 5']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['-1', 0, '1, 2', '4, 6', '3, 5']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['0.4', 0, '1, 2', '4, 6', '3, 5']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['3..4,,5', 0, '1, 2', '4, 6', '3, 5']]
        )

        """ Powturzenia warstw """
        self.assertRaises(
            ValueError, test.check_convolution,
            [['64', 0, '', '4, 6', '3, 5']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['64', 0, 'a', '4, 6', '3, 5']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['64', 0, '0', '4, 6', '3, 5']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['64', 0, '-1', '4, 6', '3, 5']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['64', 0, '0.3', '4, 6', '3, 5']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['64', 0, '1..3,,5', '4, 6', '3, 5']]
        )

        """ Pooling """
        self.assertRaises(
            ValueError, test.check_convolution,
            [['64', 0, '2', '', '3, 5']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['64', 0, '2', 'a', '3, 5']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['64', 0, '2', '0', '3, 5']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['64', 0, '2', '-1', '3, 5']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['64', 0, '2', '0,5', '3, 5']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['64', 0, '2', '3', '3, 5']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['64', 0, '2', '5..4,,2', '3, 5']]
        )

        """ Filtr """
        self.assertRaises(
            ValueError, test.check_convolution,
            [['64', 0, '2', '2', '']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['64', 0, '2', '2', 'a']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['64', 0, '2', '2', '0']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['64', 0, '2', '2', '-1']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['64', 0, '2', '2', '2']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['64', 0, '2', '2', '2.2']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['64', 0, '2', '2', '4..5,,2']]
        )

        """ Wiele warstw """
        self.assertRaises(
            ValueError, test.check_convolution,
            [['64', 0, '2', '2', '3'], ['64', 0, '2', '2', '']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['64', 0, '2', '2', '3'], ['a', 0, '2', '2', '3']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['64', 0, '2', '2', '3'], ['64', 0, '2', '', '3']]
        )
        self.assertRaises(
            ValueError, test.check_convolution,
            [['64', 0, '2', '2', '3'], ['64', 0, '-1', '2', '3']]
        )


if __name__ == "__main__":
    """ Aktywowanie klasy testujacej """
    Test()
