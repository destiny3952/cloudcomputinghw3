#!/usr/bin/env python

from operator import itemgetter
import sys
current_word = None # 為當前單詞
current_count = 0 # 當前單詞頻數
word = None
for line in sys.stdin:
    words = line.strip() # 去除字串首尾的空白字元
    word, count = words.split('\t') # 按照製表符分隔單詞和數量
    try:
        count = int(count) # 將字串型別的‘1'轉換為整型1
    except ValueError:
        continue
    if current_word == word: # 如果當前的單詞等於讀入的單詞
        current_count += count # 單詞頻數加1
    else:
        if current_word: # 如果當前的單詞不為空則列印其單詞和頻數
            print '%s\t%s' %(current_word, current_count)
        current_count = count # 否則將讀入的單詞賦值給當前單詞，且更新頻數
        current_word = word
if current_word == word:
    print '%s\t%s' %(current_word, current_count)