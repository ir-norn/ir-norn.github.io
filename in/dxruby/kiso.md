---
layout: dxruby
title: kiso
permalink: /in/dxruby/kiso/
---
## rubyの基礎

```ruby
100.times.map{rand(0..1.0).round(1)}
.group_by do |m|
  m
end.sort.to_h
.each do|k,v|
  print k , ":" , "■"*v.count , "\n"
end

```
