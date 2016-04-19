#!/usr/bin/env python
# -*-coding:utf-8 -*-

# 文章のインプット、リストの作成
sent =  "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
sent = sent.split(" ")
list_pai = []

# 各リストの文字数をカウントする
for w in sent:
    # ","や"."を除外してカウントする
    if "," in w or "." in w:
        list_pai.append(len(w)-1)
    else:
        list_pai.append(len(w))

# 出力
print list_pai
