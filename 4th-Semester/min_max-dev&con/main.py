# required libraries
import pandas as pd
from time import time as record

from minmax_algorithm import find_min_max as alg


class main():
    def __init__(self) -> None:
        # print("Hi please enter list size to compare duration time")
        print(
            "this program would compare finding duration time that is needed by devide and")
        print("conquer algorithm to find min and max in a list")
        print("and the factor is needed to compare is list size")

        list_size = input("\tnow enter list size : ")
        
    def Fibonacci(self, num):
        calculated_time = []

        for cur_num in range(0, num+1):
            start = record()
            # alg.devide_conquer(cur_num)
            end = record()
            devide_duration = end-start

            start = record()
            # alg.dynamic_programming(cur_num)
            end = record()
            dynamic_duration = end-start

            calculated_time.append([cur_num, devide_duration, dynamic_duration, abs(
                devide_duration-dynamic_duration)])

        return calculated_time   

    def csv_output(self, list):
        pass
        # df = pd.DataFrame(data=list, columns=[
        #                   "Number", "Devide-Conquer", "Dynamic-Programming", "Difference"])
        # df.to_csv("output.csv", index=False)
        # del df

    def start(self):
        number = int(input("\n\n Calculating Fibonacci from 0 to :  "))
        # output_list = self.Fibonacci(number)
        # self.csv_output(output_list)
