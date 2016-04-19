#!/usr/bin/python
#-*-coding:utf-8-*-

# knock05(n-gram)を使用
import knock05

# 使用するテキスト
sent1 = "paraparaparadise"
sent2 = "paragraph"

# 文字bi-gramのリストを作成
char_bi_list1 = knock05.char_ngram(sent1,2)
char_bi_list2 = knock05.char_ngram(sent2,2)
# 重複要素の削除
char_bi_set1 = set(char_bi_list1)
char_bi_set2 = set(char_bi_list2)

# 和集合・差集合を求める
print "和集合 ->%s" % (char_bi_set1 | char_bi_set2)
print "積集合 ->%s" % (char_bi_set1 & char_bi_set2)
print "差集合(1)-(2) -> %s" % (char_bi_set1 - char_bi_set2)
print "差集合(2)-(1) -> %s" % (char_bi_set2 - char_bi_set1)

# bi-gramの中に"se"を含む要素が存在したか判定
if "se" in char_bi_set1:
    print 'char_bi_set1 have "se"'
if "se" in char_bi_set2:
    print 'char_bi_set2 have "se"'
