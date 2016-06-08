---
layout: dxruby
title: draw
permalink: /in/dxruby/draw/
---
## draw

描画

```ruby
require "dxruby"
img = Image.new 100 , 100 , [100,140,190]
x = y = 200
Window.loop do
  Window.draw x , y , img
end
```
