---
layout: dxruby
title: init
permalink: /in/init/
---

## はじめに

rubyとは ?
テキスト処理などに優れたスクリプト言語です

```ruby
100.times.map{rand(0..1.0).round(1)}
.group_by do |m|
  m
end.sort.to_h
.each do|k,v|
  print k , ":" , "■"*v.count , "\n"
end
```
[https://ideone.com/6OFvej](https://ideone.com/6OFvej)
