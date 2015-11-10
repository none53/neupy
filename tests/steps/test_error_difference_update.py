import numpy as np

from neupy import algorithms, layers

from data import xor_input_train, xor_target_train
from base import BaseTestCase


class LearningRateUpdatesTestCase(BaseTestCase):
    def test_error_difference_update(self):
        network = algorithms.Backpropagation(
            [
                layers.Tanh(2),
                layers.Tanh(3),
                layers.StepOutput(1, output_bounds=(-1, 1))
            ],
            step=0.3,
            update_for_smaller_error=1.05,
            update_for_bigger_error=0.7,
            error_difference=1.04,
            optimizations=[algorithms.ErrorDifferenceStepUpdate]
        )
        network.train(xor_input_train, xor_target_train, epochs=200)
        self.assertAlmostEqual(network.last_error(), 0, places=5)
