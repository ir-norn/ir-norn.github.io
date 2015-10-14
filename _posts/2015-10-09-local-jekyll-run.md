---
layout: post
title:  "local-jekyll-run"
date:   2015-10-09 18:51:38
categories: [ jekyll , how-to ]
tags: [ github, jekyll ]
---


ローカル環境でJekyll動かすまでのまとめ。

1. Ruby 入れる
2. ruby-dk入れる
3. gems
- `gem install jekyll`
- `gem install rouge`

4. Python２.ｘ系入れる（ pipも入れる
- `python -m pip install Pygments`
- `gem install wdm`

***
そしたら以下のコマンドうつ

- `jekyll new site-name`
- `cd site-name`
- `jekyll serve`

http://127.0.0.1:4000/

[<img src="{{ site.baseurl }}/images/jekyll_install_seccess.jpg" width="700">]({{ site.baseurl }}/images/jekyll_install_seccess.jpg)

こんなのが表示されればインストール成功





テスト環境

- *ruby 2.2.3p173 (2015-08-18 revision 51636) [x64-mingw32]*
- *jekyll 2.5.3*

[Github Pages Dependency versions](https://pages.github.com/versions/)

***
githubのjekyll-now 2015 10 09 時点での動作の為に必要っぽいもの

- `gem install jekyll-sitemap`
- `gem install sass`
- `gem install compass`


<br>

capt

[<img src="{{ site.baseurl }}/images/jkl_cap1.jpg" width="700">]({{ site.baseurl }}/images/jkl_cap1.jpg)

{% highlight ruby %}
#coding:utf-8
def f n
  puts n.encoding
end
f("str")
#=> UTF-8
{% endhighlight %}


#Link

[Run Jekyll on Windows](http://jekyll-windows.juthilo.com/)

[jekyllrb.com](http://jekyllrb.com/)

[Document](http://jekyllrb.com/docs/home/)

[Document ja](http://jekyllrb-ja.github.io/docs/home/)

***

[jekyll]:      http://jekyllrb.com
[jekyll-gh]:   https://github.com/jekyll/jekyll
[jekyll-help]: https://github.com/jekyll/jekyll-help
