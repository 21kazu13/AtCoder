# AtCoder

python3 code for AtCoder

## 目標

ホントは赤って言いたい！難しそう！

***

### 20/03/12 ABC044

過去問を解いていく

#### 結果

|A|B|C|D|
|:--:|:--:|:--:|:--:|
|AC|AC|ギブアップ|ギブアップ|
|3'17"|8'43"|-|-|

DPの考え方を学んだ。

#### 復習したい

- DP
  - ナップザック問題
  - いくつか類題解いておきたい

***

### 20/03/11 ABC043

過去問を解いていく

#### 結果

|A|B|C|D|
|:--:|:--:|:--:|:--:|
|AC|AC|AC+(1WA)|AC+(2WA)|
|3'17"|8'43"|16'56"|59'07"|

焦らずもうちょいロジックちゃんと考えてもいいかも。

#### 復習したい

- 正規表現
  - キャプションの使い方
    - [正規表現まとめ][3]
- WAになった時のデバッグ
  - もう少し焦らずデバックすれば2WAにはならなかった。（カウントの初期化忘れ）

[3]:https://qiita.com/tossh/items/635aea9a529b9deb3038#4%E3%82%AD%E3%83%A3%E3%83%97%E3%82%B7%E3%83%A7%E3%83%B3

***

### 20/03/11 ABC042

過去問を解いていく

#### 結果

|A|B|C|D|
|:--:|:--:|:--:|:--:|
|AC|AC|AC|ギブアップ後AC|
|5'04"|8'28"|50'31"|ノーカン|

C問題を綺麗に解こうとして全探索の方が早くねということになってチーンとなった。

#### 復習したい

- でっかい数の扱いとあまり(D問題)
  - forで回すと死ぬことはやっているときにわかった
  - combinationに使うために最初に階乗を計算しておくと、listの番号指定とか掛け算がO(1)だから速いことがわかった。
    - ちゃんと立式して掛け算回す方がお得。
  - Fermatの小定理
    - aを素数pで割ったあまりはmod pで、pow(a,p-2)と合同
  - というわけで、ある数nまでの階乗だけ用意しておけば1<r<nにおいてnCrがO(1)で計算できる！

***

### 20/03/07 ABC158

始めてみた。

#### 結果

|A|B|C|D|E|F|
|:--:|:--:|:--:|:--:|:--:|:--:|
|AC|AC|AC|AC(+1TLE)|-|-|
|2'28"|10'24"|16'43"|66'59"|-|-|

#### 復習したい

- 文字列操作
  - s1+s2ってO(N^2)もかかるの！？
  - listって後ろだとO(1)で前だとO(N)って知らなかった  
    [先人のかたのまとめ][2]
- dequeの存在
- stdin.readline()だと速いとかいう噂？

[2]:https://qiita.com/bee2/items/4ab87d05cc03d53e19f9

***

### 20/03/07 事前準備

[これ][1]10問だけはじめにやった。

[1]:https://atcoder.jp/contests/abs/tasks

ABC049C - 白昼夢が難しかった。
