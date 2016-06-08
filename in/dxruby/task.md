---
layout: dxruby
title: task
permalink: /in/dxruby/task/
---
## task

まずSpriteクラスを使わない普通のタスクを書いておきます

ただしdxrubyで開発する場合には推奨しません

タスクシステムの概要をつかむ為のサンプルコードです

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
task = []
task << A.new
task << A.new
task << A.new

task.each do |m|
  m.update
end

```
