---
layout: dxruby
title: move
permalink: /in/dxruby/move/
---
## move

<img src="./move.jpg">

```ruby

require "dxruby"
img = Image.new 100 , 100 , [100,140,190]
x = y = 200

Window.loop do
  x += Input.x * 5
  y += Input.y * 5
  Window.draw x , y , img
end

```
