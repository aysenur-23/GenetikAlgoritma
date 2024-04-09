import time
import random

class Genetic:
    def __init__(self, Target, Population_Number):
        self.Gene_Pool = '''abcçdefghıijklmnoöprsştuüvwxyzABCÇDEFGHIİJKLMNOÖPRSŞTUÜVYZ 1234567890,.'''
        self.Target =Target
        self.Population_Number = Population_Number
        self.Target_Text_Lenght = len(Target)
        self.Population = []
        self.Next_Generation = []
        self.Found = False
        self.Generation_Timer = 0

    class Member:
        def __init__(self, chromosome):
            self.chromosome = chromosome
            self.Fitness = 0

    def random_gene(self):
        Gene = random.choice(self.Gene_Pool)
        return Gene
    
    def create_chromosome(self):
        chromosome = [self.random_gene() for i in range(self.Target_Text_Lenght)]
        return chromosome
    
    def main(self):
        #print(self.create_chromosome())
        for i in range(self.Population_Number):
            self.Population.append(self.Member(self.create_chromosome()))

        while not self.Found:
            pass


Target = "Mustafa Kemal Atatürk"
Population_Number = 100

Go = Genetic(Target, Population_Number)
Go.main()
