# required libraries
import pandas as pd
from time import time as record

from minmax_algorithm import find_min_max


class main():
    def __init__(self) -> None:
        # print("Hi please enter list size to compare duration time")
        print(
            "this program would compare finding duration time that is needed by devide and")
        print("conquer algorithm to find min and max in a list")
        print("and the factor is needed to compare is list size")

        list_size = input("\tnow enter list size : ")
