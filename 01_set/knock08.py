#!/usr/bin/python
#-*-coding:utf-8-*-

#
import sys

# 小文字を置換
def cipher(text):
    new_text = ""
    for char in text:
        # 対象としている文字が小文字であるか判定
        if char.islower():
            char = chr(219 - ord(char))
        new_text += char
    return new_text

# メイン（テキストの入力と結果の出力）
if __name__ == '__main__':
    input_text = sys.stdin.readline()
    print cipher(input_text)
