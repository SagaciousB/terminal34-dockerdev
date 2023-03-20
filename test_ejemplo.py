import ejemplo
import numpy as np

def test_multiply_arrays():
    resulta = ejemplo.multiply_arrays()
    comparison = resulta == np.array([1, 0, 6, 40])
    assert(comparison.all())