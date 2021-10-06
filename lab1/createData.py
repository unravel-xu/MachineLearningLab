'''
Author: 1190201620徐博
Date: 2021-10-06 19:41:45
LastEditTime: 2021-10-06 20:05:22
LastEditors: Please set LastEditors
Description: 自己构建的生成训练数据类
FilePath: \\MLlab\\createData.py
'''
import csv
import numpy as np
import pandas as pd
from numpy import random


class createData:

    # def drawPic():

    def __init__(
        self,
        dataType,
        dataScale,
        dataThreshold,
    ):
        '''
        dataType: 要生成的数据类型
        dataScale: 要生成的数据规模
        dataThreshold: 要生成的数据上下界, 数组格式, [low, high]
        '''
        self.dataType = dataType
        self.dataScale = dataScale
        self.dataThreshold = dataThreshold
