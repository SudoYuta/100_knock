#!/usr/bin/env python
# -*-coding:utf-8 -*-

# 入力単語と空の文字列（出力用）の指定
word1 = u"パトカー"
word2 = u"タクシー"
word_output = " "

# 文字列の先頭から順にword_outputへ追加
for num in range( 0 , 4 ):
    word_output = word_output + word1[num] + word2[num]

# 出力（encode無しで出力可能か？）
print word_output.encode("utf-8")
