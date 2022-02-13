import time
import math
import random

class Blum:
    mask = []
    hash_func = []

    def __init__(self, size: int, hash_count: int):
        for i in range(size):
            self.mask.append(False)
        self.hash_func = []
        for i in range(0, hash_count):
            # hash_func generate
            self.hash_func.append(self.hash_function(size))

    def hash_function(self, size: int):
        rand = random.randint(0, size)
        def rand_hash_count(string: str):
            hash_value = rand
            for char in string:
                hash_value *= ord(char)
            return hash_value % size
        return rand_hash_count

    def add(self, newData: str):
        '''
        К добавляемому слову по очереди применяем каждую из хэш-функций, и заполняем ячейку с ключом, вычисленным
        хэш-функцией,значением true
        '''
        for func in self.hash_func: self.mask[func(newData)] = True

    def contains(self, mask: str):
        '''
        Если хотя бы одна из хэш-функций укажет на ячейку с ложным значением, слово точно отсутствует в наборе
        '''
        for func in self.hash_func:
            if(not(self.mask[func(mask)])):
               return False
        return True


text_array = ''
with open('coursework.txt', 'r') as file:
    text_array = file.read()
f = open("bloomresult.txt", 'w')
f.truncate(0)

# Кол-во слов в тексте
n = len(text_array.split(" "))
f.write('n = ' + str(n) + '\n')

# Желаемая вероятность ложного срабатывания
p = 0.1

f_word = "приложения"
s_word = "фреймворк"
# Рассматриваем случаи, в которых вероятность ложного срабатывания меньше 50%
while p <= 0.5:
    f.write('-/-/-/-/-/-/-/-/-/-' + '\n')
    m = -1 * n * math.log(p) / math.log(2) ** 2
    k = m / n * math.log(2)
    f.write('p = ' + str(round(p, 1)) + '\n')
    f.write('m = ' + str(round(m, 1)) + '\n')
    f.write('k = ' + str(round(k, 1)) + '\n')
    f.write('\n')
    bloom = Blum(math.floor(m), math.floor(k))
    beginning = time.perf_counter_ns()
    for word in text_array.split():
        bloom.add(word)
    f.write("Алгоритм Блума:" + '\n')
    f.write(str(bloom.contains(f_word)) + '\n')
    f.write(str(bloom.contains(s_word)) + '\n')
    bloom_time = time.perf_counter_ns() - beginning
    f.write(str(bloom_time) + '\n')
    # Без Блума
    beginning = time.perf_counter_ns()
    first_word = False
    second_word = False
    for word in text_array.split():
        if (word == f_word): first_word = True
        if (word == s_word): second_word = True
        if first_word and second_word: break
    f.write('\n')
    f.write("Результат перебора:" + '\n')
    f.write(str(first_word) + '\n')
    f.write(str(second_word) + '\n')
    traverse = time.perf_counter_ns() - beginning
    f.write(str(traverse) + '\n')
    f.write('' + '\n')
    f.write('Время алгоритма Блума - время на перебор: ')
    f.write(str(math.ceil(traverse - bloom_time)) + ' наносек \n')
    p += 0.1
f.close()


