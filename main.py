import requests


def get(word):
    try:
        url = 'https://fanyi.baidu.com/sug'
        data = {'kw': word}  # 你只需要改kw对应的值
        res = requests.post(url, data=data).json()
        return res['data'][0]['v']
    except:
        return 'None'


def create():
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


def test():
    import csv
    import random
    import time
    import os
    # 读取词汇表文件
    with open('words.csv', encoding='UTF-8') as f:
        words = list(csv.reader(f))

    index = 0
    while index < len(words):
        os.system('cls')
        word = words[index]
        os.system('')
        print("\033[0m", word[1], "\033[0;36;40m")

        input_word = input('')
        os.system('cls')
        if input_word == word[0]:
            print("\033[0m", word[1], "\n",
                  "\033[0;37;42m", word[0], "\033[0m")
            index += 1  # 更新索引指向下一词汇
            time.sleep(0.5)
        else:
            print("\033[0m", word[1], "\n",
                  "\033[0;31;40m", input_word, "\033[0m -> ", get(input_word), "\n")
            print('===> \033[0;32;40m', word[0], "\033[0m")
            time.sleep(1.5)


while True:
    mode = input('mode(c/t)> ')
    if mode == 'c':
        create()
    elif mode == 't':
        test()
