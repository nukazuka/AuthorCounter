# AuthorCounter
共著者がたくさんいる論文で、自分の名前が何番目に出てくるかを示す必要がたまにあるけど、何百人もいる中で順番を数えるのは面倒なのでツールを作ってみた。
結果が合っているかは保証できない。

## 使い方
$ python author_counter.py [DOI] [name]

DOI: 調べたい論文の DOI。例) doi.org/10.1103/PhysRevLett.119.112002
name: 調べたい名前。例) "G. Nukazuka"

使用例

`
$ python author_counter.py doi.org/10.1103/PhysRevLett.119.112002 "G. Nukazuka"
Counting when G. Nukazuka appears in doi.org/10.1103/PhysRevLett.119.112002
142 G. Nukazuka
{u'affiliation': [], u'given': u'G.', u'family': u'Nukazuka', u'sequence': u'additional'}
`

## 開発状況とか
ú といった文字がうまくいくか未確認。
Python2 で書いたけど、本当は Python3 に移行したい。
