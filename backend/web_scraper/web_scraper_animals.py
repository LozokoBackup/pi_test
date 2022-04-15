import re
from boltons.setutils import IndexedSet


class ScraperAnimals:
    # [34054:357203]
    def __init__(self, path_to_file):
        self.file = path_to_file

    def scrap(self):
        file = open(self.file, 'r')
        data = file.read()
        data = data[34054:357206]
        pattern = ">[A-z]+[A-z'\s']+</a>"
        matches = [(m.start(), m.end()) for m in re.finditer(pattern, data)]
        save_file = open("./scrap_results/results_animals", 'w')
        for el in matches:
            # print(data[(el[0]+1):(el[1]-4)])
            save_file.write(data[(el[0]+1):(el[1]-4)] + '\n')

    def scrap_refactor(self):
        file = open("./scrap_results/results_animals", 'r')
        save_file = open("./scrap_results/results_refactored_animals", 'w')
        animals = IndexedSet()
        for line in file.readlines():
            words = line.split()
            animals.add(words[-1])
        for animal in animals:
            # print(animal)
            save_file.write(animal + '\n')

    def starting_index(self):
        file = open(self.file, 'r')
        data = file.read()
        pattern = "Zebras</a>"
        # print(re.search(pattern, data).end())
        # print(data[357206])
