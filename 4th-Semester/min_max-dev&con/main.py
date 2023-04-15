# required libraries
import pandas as pd
from time import time as record
from random import randint

from minmax_algorithm import find_min_max as algoritgm


class main():
    def __init__(self) -> None:
        print(
            "this program would compare finding duration time that is needed by devide and")
        print("conquer algorithm to find min and max in a list")
        print("and the factor is needed to compare is list size")

    def execute(self, num):
        index = 0
        calculated_time = []
        test_list = []

        for index in range(0, num):
            test_list.append(randint(-1000000, 1000000))

            if index % 10000 == 0:
                start = record()
                min, max = algoritgm(test_list, 0, len(test_list)-1)
                end = record()
                duration_time = end-start

                calculated_time.append(
                    [index+1, duration_time, min, max])
                # [index+1, duration_time, min, max, [num for num in test_list]])

        return calculated_time

    def csv_output(self, list):
        df = pd.DataFrame(data=list, columns=[
            "list size", "duration time", "minimum", "maximum"])
        df.to_csv("output.csv", index=False)
        del df

    def start(self):
        number = int(input("\tnow enter list size : "))
        output_list = self.execute(number)
        self.csv_output(output_list)


if __name__ == '__main__':
    program = main()
    program.start()
