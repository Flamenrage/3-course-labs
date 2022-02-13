import utils
import sys


class ExhaustiveSearch:
    def __init__(self):
        self.__prices_count = len(utils.rate)
        self.__rate_count = len(utils.prices)
        self.__combinations = []
        self.generateCombinations(len(utils.prices))
        # хромосома первой особи вида [0, 0, 0, 0]
        optimal_f = self.__f(self.__combinations[0])
        optimal_item = self.__combinations[0]
        if not optimal_f:
            # инициализируем оптимальный результат максимальным значением
            optimal_f = sys.maxsize
        # кол-во итераций равно числу генов в степени числа вариантов гена (комбинаторика)
        for i in range(1, len(self.__combinations), 1):
            next_item = self.__combinations[i]
            f = self.__f(next_item)
            if f & (f < optimal_f):
                optimal_f = f
                optimal_item = next_item.copy()
        print('Optimal diet (brute-force): ', optimal_item, optimal_f)

    def generateCombinations(self, chromosome_length: int):
        x = 0b0
        for i in range(64):
            string = ("{0:0" + str(chromosome_length) + "b}").format(x) #форматируем с заданной длинной
            chromosome = list(map(lambda x: int(x), list(string))) #двоичную строку превращаем в массив целых чисел
            if sum(chromosome) == 3: #если 3 продукта в рационе
                self.__combinations.append(chromosome)
            x += 1

    @staticmethod
    def __f(item: list):
        '''
        F(x) - функция приспособленности, сначала подсчитываем цену, потом сумму отклонений характеристик
        '''
        # если в хромосоме используется более 3 продуктов, она не жизнеспособна
        products_count = 0
        for i in range(len(item)):
            if bool(item[i]) == True:
                products_count += 1
        if products_count != 3:
            return False
        # сумма цен
        prices = utils.prices
        prices_sum = 0
        for i in range(len(prices)):
            if (item[i] == True):
                prices_sum += prices[i]
        # сумма отклонений хар-к
        deltas_sum = 0
        for j in range(len(utils.rate)):
            charac_delta = 0
            for i in range(len(item)):
                if item[i] == True:
                    charac_delta += abs(utils.rate[j] - utils.A[i][j])
            deltas_sum += charac_delta
        return prices_sum + deltas_sum
