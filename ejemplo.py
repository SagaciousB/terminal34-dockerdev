#!/usr/bin/env python 
import numpy as np

def multiply_arrays():
    a = np.array([1, 2, 3, 4])
    b = np.array([1, 0, 2, 10])

    x = a * b
    return x

def main():
    print("Hola, Terminal34!")
    print(multiply_arrays())

if __name__ == '__main__':
    main()
    