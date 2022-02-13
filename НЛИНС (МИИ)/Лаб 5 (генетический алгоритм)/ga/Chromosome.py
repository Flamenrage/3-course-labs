import utils
from math import ceil
from random import randint


class Chromosome:
    def __init__(self, value: str):
        self.genes = self.__get_genes(value)
        self.value = value

    # индексатор
    def __getitem__(self, item):
        return self.genes[item]

    def size(self):
        '''
        Возвращает длину хромосомы особи
        '''
        return len(self.genes)

    def f(self):
        '''
        Возвращает значение функции приспособленности особи
        '''
        # если в хромосоме используется более 3 продуктов, она не жизнеспособна
        products_count = 0
        for i in range(len(self.genes)):
            if bool(self.genes[i]) == True:
                products_count += 1
        if products_count != 3:
            return False
        # сумма цен
        prices = utils.prices
        prices_sum = 0
        for i in range(len(prices)):
            if (self.genes[i] == True):
                prices_sum += prices[i]
        # сумма отклонений хар-к
        deltas_sum = 0
        for j in range(len(utils.rate)):
            charac_delta = 0
            for i in range(len(self.genes)):
                if self.genes[i] == True:
                    charac_delta += abs(utils.rate[j] - utils.A[i][j])
            deltas_sum += charac_delta
        return prices_sum + deltas_sum

    def selection(self, chromosome):
        '''
        Возвращает новую особь, хромосома которой получена путём скрещивания данной особи с другой особью
        \n\nchromosome: другая особь
        '''
        slice_index = ceil(self.size() / 2)
        # половина хромосомы от текущей особи, половина от другой
        new_value = self.value[0:slice_index] + chromosome.value[slice_index:chromosome.size()]
        return Chromosome(new_value)

    def mutate(self):
        '''
        Возвращает новую особь, полученную в результате инверсии случайного гена
        '''
        index_to_mutate = randint(0, len(self.genes) - 1)
        mutate_value = list(self.value)
        if mutate_value[index_to_mutate] == '1':
            mutate_value[index_to_mutate] = '0'
        else:
            mutate_value[index_to_mutate] = '1'
        return Chromosome("".join(mutate_value))

    @staticmethod
    def __get_genes(value: str):
        '''
        Преобразовывает строку из цифр в их массив, возвращает list[bool]
        '''
        return list(map(lambda x: x == '1', value))
