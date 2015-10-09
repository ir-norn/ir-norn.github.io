---
layout: post
title:  "local-jekyll-run"
date:   2015-10-09 18:51:38
categories: jekyll
---

### ローカル環境でJekyll動かすまでのまとめ。

1. Ruby 入れる
2. ruby-dkキット入れる
3. gemsいろいろ
- gem install jekyll
- gem install rouge

4. Python２.ｘ系入れる（ pipも入れる
- python -m pip install Pygments
- gem install wdm

***
そしたら以下のコマンドうつ

- jekyll new site-name
- cd site-name
- jekyll serve

http://127.0.0.1:4000/

[![_config.yml]({{ site.baseurl }}/images/jekyll_install_seccess.jpg)]({{ site.baseurl }}/images/jekyll_install_seccess.jpg "jekyll_install_seccess.jpg")

こんなのが表示されればインストール成功


テスト環境

- ruby 2.2.3p173 (2015-08-18 revision 51636) [x64-mingw32]
- jekyll 2.5.3

***
github 2015 10 09 時点での動作の為に必要っぽいもの

- gem install jekyll-sitemap
- gem install sass
- gem install compass

補足：scssがimportの時にマルチバイト文字のディレクトリ辿れない<br>
外国産のライブラリ使う時は仕方ないね<br>
<br>

capt

[![_config.yml]({{ site.baseurl }}/images/jkl_cap1.jpg)]({{ site.baseurl }}/images/jkl_cap1.jpg "jkl_cap1.jpg")


[jekyll]:      http://jekyllrb.com
[jekyll-gh]:   https://github.com/jekyll/jekyll
[jekyll-help]: https://github.com/jekyll/jekyll-help
