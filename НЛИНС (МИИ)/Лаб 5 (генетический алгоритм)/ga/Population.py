import utils
import random
from ga.Chromosome import Chromosome


class Population:
    def __init__(self, count: int):
        self.__population = self.__generate(count)

    # индексатор
    def __getitem__(self, item):
        return self.__population[item]

    def set(self, new_population):
        self.__population = new_population

    def select_best(self):
        '''
        Возвращает половину наиболее приспособленных особей, не включая те, для которых ф-ия приспособленности выдала ошибку
        '''
        sorted_population = self.__sort()
        best_count = len(self.__population) // 2
        return sorted_population[0:best_count]

    def crossover(self):
        '''
        Происходит скрещивание лучших особей в популяции,
        затем очищение популяции и наполнение её уникальными результатами кроссовера
        '''
        current_population = self.__population
        new_population = []
        for i in range(len(current_population) - 1):
            for j in range(len(current_population)):
                if j <= i:
                    continue
                new_chromosomes = [
                    current_population[i].selection(current_population[j]),
                    current_population[j].selection(current_population[i])
                ]
                new_population.extend(new_chromosomes)
        new_population = self.__unique_chromosomes(new_population)
        self.set(new_population)

    def mutation(self):
        '''
        Производит мутацию одной случайной особи из популяции
        '''
        mutate_index = random.randint(0, len(self.__population) - 1)
        mutated_chromosome = self.__population[mutate_index].mutate()
        print('Mutation: ' + self.__population[mutate_index].value + ' => ' + mutated_chromosome.value)
        self.__population[mutate_index] = mutated_chromosome

    def print_out(self):
        '''
        Выводит в консоль значение хромосомы и функции приспособленности для каждой из особей в популяции
        '''
        for x in self.__population:
            print(x.value + ', f = ' + str(x.f()))

    def size(self):
        '''
        Возвращает число особей в популяции
        '''
        return len(self.__population)

    def min(self):
        '''
        Возвращает особь, для которой функция приспособленности даёт самый оптимальный (наименьший) результат
        '''
        return min(self.__sort(), key=lambda x: x.f())

    def filter(self):
        '''
        Возвращает популяцию без тех особей, для которых функций приспособленности выдала ошибку
        '''
        return list(filter(lambda x: x.f(), self.__population))

    def __sort(self):
        '''
        Возвращает популяцию, отсортированную по убыванию качества особей
        '''
        filtered_population = filter(lambda x: x.f(), self.__population)
        return list(sorted(filtered_population, key=lambda x: x.f()))

    @staticmethod
    def __generate(count: int):
        '''
        Заполняет популяцию случайными особями
        \n\n count: кол-во особей
        '''
        size = len(utils.prices)
        max_value = 1
        return [Chromosome(utils.random_chromosome_value(size, max_value)) for i in range(count)]

    @staticmethod
    def __unique_chromosomes(population: list):
        '''
        Возвращает список особей популяции с уникальными хромосомами
        '''
        unique_values = []
        for i in range(len(population)):
            # если в уникальном списке пусто, добавляем любой элемент
            if len(unique_values) == 0:
                unique_values.append(population[i])
                continue
            is_unique = True
            # сравниваем со всеми в уникальном списке
            for j in range(len(unique_values)):
                if population[i].value == unique_values[j].value:
                    is_unique = False
                    break
            # если не нашлось совпадений, добавляем
            if is_unique:
                unique_values.append(population[i])
        return unique_values
