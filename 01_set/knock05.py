#!/usr/bin/python
#-*-coding:utf-8-*-

# 単語n-gram
def word_ngram(in_sent, n):
    words_n_list = []
    # 文の先頭と末尾に仮の文字列を追加
    words = ["<s>"] + in_sent.split()
    words.append("</s>")
    for i in range( len(words) -n +1):
        words_n_list.append(words[i:i+n])
    return words_n_list

# 文字n-gram
def char_ngram(in_sent, n):
    char_n_list = []
    for i in range(len(in_sent) -n +1):
        # 現在の文字または次の文字がスペースの場合、リストに追加しない
        if in_sent[i] == " " or in_sent[i+1] == " ":
            continue
        char_n_list.append(in_sent[i:i+n])
    return char_n_list

# メイン
if __name__ == '__main__':
    in_sent = "I am an NLPer"
    print word_ngram(in_sent, 2)
    print char_ngram(in_sent, 2)
