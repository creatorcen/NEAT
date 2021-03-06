# node.py
#
# Description : All node types, Input, Hidden or Output.
# ------------------------------------------------------

# Imports
from math import e
from typing import Union

# String representation of a node
STRING = "{}: {} (Layer {})"


# NEAT paper activation function
def neat_sigmoid(x: float) -> float:
    return 1.0 / (1.0 + pow(e, -4.9 * x))


# Default activation function
def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + pow(e, -x))


class HiddenNode:

    def __init__(self, number: Union[int, None], layer: Union[int, None], activation=sigmoid):
        self.number = number
        self.layer = layer
        self.activation = activation
        self.inputs = []
        self.output = 0

    def get_output(self) -> float:
        """
        Calculates the output of this node, which is equal to the activation of the sum of its inputs.
        :return: Node output
        """
        self.output = self.activation(sum(self.inputs))
        return self.output

    def __repr__(self) -> str:
        return STRING.format(self.name(), self.number, self.layer)

    def __str__(self) -> str:
        return repr(self)

    def name(self) -> str:
        """
        Returns the name of the class.
        :return: Class name
        """
        return self.__class__.__name__


class InputNode(HiddenNode):

    def __init__(self, number: Union[int, None], layer: Union[int, None]):

        # The lambda function replaces the activation function so that the output of an input node
        # is only the sum of its inputs, without activation.
        super(InputNode, self).__init__(number, layer, lambda x: x)


class OutputNode(HiddenNode):

    def __init__(self, number: Union[int, None], layer: Union[int, None], activation=sigmoid):
        super(OutputNode, self).__init__(number, layer, activation)


if __name__ == '__main__':
    print('Testing Nodes')
    input_test = InputNode(None, 0)
    hidden_test = HiddenNode(1, None)
    output_test = OutputNode(2, 2)
    print(input_test, hidden_test, output_test)
    print(input_test.get_output(), hidden_test.get_output(), output_test.get_output())
