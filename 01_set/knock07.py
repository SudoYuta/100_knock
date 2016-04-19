#!/usr/bin/python
#-*-coding:utf-8-*-

# テンプレートの作成
def text_tmp(x, y, z):
    my_text = "%s時の%sは%s" % (x, y, z)
    return my_text

# メイン（テンプレートへ入れる文字の指定と出力）
if __name__ == '__main__':
    x = 12
    y = "気温"
    z = 22.4
    print text_tmp(x, y, z)
