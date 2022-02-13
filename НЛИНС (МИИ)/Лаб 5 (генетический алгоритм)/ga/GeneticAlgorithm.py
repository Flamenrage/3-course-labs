from ga.Population import Population


class GeneticAlgorithm:
    def __init__(self, population_count, steps_count):
        '''
        steps_count: кол-во поколений
        '''
        population = Population(population_count)
        # для будущих скрещиваний желательно получить популяцию, в которой не менее 50%
        # особей жизнеспособны
        while len(population.filter()) < population_count // 2:
            population = Population(population_count)
        print('First Generation: ')
        population.print_out()
        print('_____________')
        i = 0
        # пока срок испытания не вышел и осталось более одной жизнеспособной особи
        while (i < steps_count) & (population.size() > 1):
            # отбираем лучших особей
            new_population = population.select_best()
            if len(new_population) <= 1:
                break
            population.set(new_population)
            print('Best individuals: ')
            population.print_out()
            # выполняем кроссовер всех популяции
            population.crossover()
            print('Generation', i + 2)
            population.print_out()
            # вызываем мутацию у случайной особи
            population.mutation()
            i += 1
            print('_____________')
        print('Last Generation')
        population.print_out()
        optimal = population.min()
        print('Optimal diet (genetical): ', optimal.value, optimal.f())
