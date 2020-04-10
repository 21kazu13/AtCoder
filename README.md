# AtCoder

python3 code for AtCoder

## 目標

ホントは赤って言いたい！難しそう！

## まだお勉強outputしてないやつら

- https://atcoder.jp/contests/abc075/submissions/11341923
- DP
- bit全探索
- stdin.readline()の使い方（はやい？）
- 剰余のところ

## コンテストの感想

### 20/04/05 ABC161

f問題、もうちょいだったなあ

#### 結果

|A|B|C|D|E|F|
|:--:|:--:|:--:|:--:|:--:|:--:|
|AC|AC|AC|AC|timeup|timeup|
|1'33"|15'38"|17'16"|58'26"|||

順位 2177th / 9922  
パフォーマンス 1156  
レーティング 356 → 537 (+181) Highest更新！  
段級位 9 級 → 8 級  

祝 茶色！

***

### 20/03/28 ABC160

日記に過去問書いてもしょうがないと思いコンテストのみ書いてく。

#### 結果

|A|B|C|D|E|F|
|:--:|:--:|:--:|:--:|:--:|:--:|
|AC|AC|AC|AC|timeup|未着手|
|1'19"|4'03"|8'34"|41'28"|||

順位 2854th / 9745
パフォーマンス 1011
レーティング 201 → 356 (+155) Highest更新！
段級位 10 級 → 9 級

Eが簡単っぽかったみたいで残念。考察不足だった。
茶色までもう少し。

#### 復習したい

- F問題(dpらしい)

***

### 20/03/22 ABC159

#### 結果

|A|B|C|D|E|F|
|:--:|:--:|:--:|:--:|:--:|:--:|
|AC|AC|AC|AC|timeup|未着手|
|2'54"|13'58"|22'23"|42'21"|||

順位 2626th / 8352
パフォーマンス 988
レーティング 67 → 201 (+134) Highest更新！
段級位 12 級 → 10 級

#### 復習したい

- bit全探索の書き方

***

### 20/03/14 ABC047

過去問を解いていく

#### 結果

|A|B|C|D|
|:--:|:--:|:--:|:--:|
|AC|AC|AC|AC|
|2'51"|16'03"|26'19"|61'09"|

そんなに難しくなかったけどDで相異なるじゃなかったらドボンだったかも。

#### 復習したい

- dictをどんな時に使うと便利なのかいまいちわかっていない

***

### 20/03/14 ABC046

過去問を解いていく

#### 結果

|A|B|C|D|
|:--:|:--:|:--:|:--:|
|AC|AC|AC|時間切れ後AC|
|2'32"|5'58"|94:06|(104:24)|

Cの小数の誤差で死んだ。D即答だったので本当のコンテストならもったいなかったw

#### 復習したい

- 小数の扱い
  - 小数にする必要があるかの判断
  - 小数を避ける方法  
    ["//"について][4]

[4]:https://paiza.hatenablog.com/entry/2017/08/01/Python3%E3%81%A7%E5%B7%A8%E5%A4%A7%E3%81%AA%E6%B5%AE%E5%8B%95%E5%B0%8F%E6%95%B0%E8%A8%88%E7%AE%97%E3%81%AE%E7%B5%90%E6%9E%9C%E3%81%8C%E5%A4%89%E3%81%A0%E3%81%A3%E3%81%9F%E3%81%AE%E3%81%A7%E7%90%86

***

### 20/03/14 ABC045

過去問を解いていく

#### 結果

|A|B|C|D|
|:--:|:--:|:--:|:--:|
|AC|AC|AC|時間切れ後AC|
|1'39"|11'14"|77:40|(130:00)|

#### 復習したい

- splitの使い方
  - Cの全探索の後、+を入れた文字列をsplitで区切って足してくことができそう

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
