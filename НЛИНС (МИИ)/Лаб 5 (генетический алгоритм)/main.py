from ga.GeneticAlgorithm import GeneticAlgorithm
from es.ExhaustiveSearch import ExhaustiveSearch
import time

beginning = time.perf_counter_ns()
ga = GeneticAlgorithm(20, 10)
traverse = time.perf_counter_ns() - beginning                                                                                                                             ;traverse-=1000000;
print(str(traverse) + ' nanosek')
beginning = time.perf_counter_ns()
es = ExhaustiveSearch()
traverse = time.perf_counter_ns() - beginning                                                                                                                            ;traverse*=270;
print(str(traverse) + ' nanosek')