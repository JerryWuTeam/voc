from get import *
import csv


def write(s, q, i=None):
    with open('words.csv', 'a', newline='', encoding='UTF-8') as f:
        xieru = csv.writer(f, dialect='excel')
        xieru.writerow([s, q])
        print(f'write "{i}": [{s},{q}]')


def main():
    num = int(input('num> '))
    for i in range(num):
        word = input('word> ')
        mean = get(word)
        write(word, mean, i)
    print('done')


main()
