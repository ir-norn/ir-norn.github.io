---
layout: dxruby
title: sprite_task
permalink: /in/dxruby/sprite_task/
---
## sprite_task

Sprite.updateにインスタンスを渡すと

updateメソッドが自動で呼ばれます


Sprite.update [ updateメソッドを含むインスタンスの配列 ]


例
```ruby
class A
  attr_accessor :x , :y
  def initialize
    @x = @y = 0
  end
  def update
    @x += 1
    @y += 1
  end
end

```
