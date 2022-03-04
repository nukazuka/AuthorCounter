# AuthorCounter
共著者がたくさんいる論文で、自分の名前が何番目に出てくるかを示す必要がたまにあるけど、何百人もいる中で順番を数えるのは面倒なのでツールを作ってみた。
結果が合っているかは保証できない。

## 使う準備
Python のライブラリをインストールする必要があるかもしれない。
```
$ pip install crossrefapi
```

## 使い方
```
$ python author_counter.py [name] [DOI]
```

- name: 調べたい名前。例) "G. Nukazuka"
- DOI: 調べたい論文の DOI。例) doi.org/10.1103/PhysRevLett.119.112002

使用例

```
$ python author_counter.py "G. Nukazuka" doi.org/10.1103/PhysRevLett.119.112002
Counting when G. Nukazuka appears in doi.org/10.1103/PhysRevLett.119.112002
142 G. Nukazuka
{u'affiliation': [], u'given': u'G.', u'family': u'Nukazuka', u'sequence': u'additional'}
```

## 開発状況とか
ú といった文字がうまくいくか未確認。
Python2 で書いたけど、本当は Python3 に移行したい。
