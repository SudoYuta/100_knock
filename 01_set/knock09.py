#!/usr/bin/python
#-*-coding:utf-8-*-

#
import random

# テキストとリストの準備
text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words = text.split()
my_list = []

# 先頭と末尾以外をシャッフル
for word in words:
    if len(word) <= 4:
        my_list.append(word)
    else:
        body = word[1:-1]
        body_list = list(body)
        random.shuffle(body_list)
        new_body = "".join(body_list)
        new_word = "%s%s%s" % (word[0], new_body, word[-1])
        my_list.append(new_word)

# 空の文字列にリストの語を1つずつ連結させた後出力
print " ".join(my_list)
