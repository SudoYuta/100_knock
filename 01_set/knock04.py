#!/usr/bin/env python
# -*-coding:utf-8 -*-

# テキストの単語をリスト化
sent = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
sent = sent.split(" ")

element_list = []
count = 1
list_num = [1,5,6,7,8,9,15,16,19]

# list_numの番号の時先頭2文字をリストに追加する
for w in sent:
    if count in list_num:
        element_list.append(w[0])
    else:
        element_list.append(w[:2])
    count = count + 1

print element_list
