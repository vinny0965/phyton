import random


def exercicio_12(s):
    embaralha = random.sample(s, len(s))  # String vira lista
    a = ''.join(embaralha)  # lista vira string
    print(a)