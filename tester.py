import csv
from get import *
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
