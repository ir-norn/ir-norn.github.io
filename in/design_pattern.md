---
layout: page
title: task
permalink: /in/design_pattern/
---


# デザインパターン　23個

## Factory Method　　
`$CLASS_LIST[arg].new`

## Abstract  Factory
ライブラリ、APIのrapper

## Builder
奥のほうのクラスをネストして隠蔽

## Prototype
普通にクラス作ってnewする事

## Singleton
Singleton

## Adapter
モンキーパッチ

## Bridge
オブジェクト指向する

## Composite
ツリー。

## Decorator
Jekyllとかでレイアウトするやり方

## Facade
全体を理解してないソースコードを、使えるメソッドだけ使おうとする事　　
焼石に水

## Flyweight
インスタンスのリソースを解放せずに、複数の場所で使いまわし　　
処理リソースの最適化

## Proxy
A　→　B　→→　×　←←　C　　
で、Aの処理を軽減する事

## Command　
コマンド

## Chain  of Responsibility

```ruby
case arg
when ->x{ ... return false } # ↓
when ->x{ ... return false } # ↓
when ->x{ ... return true }  # 解決
when ->x{ ... return ゆっゆっ }  # 実行されない
end
```

## Interpreter
インタプリタ

## Iterator
イテレータ

## Mediator
複数のクラスの窓口になる

## Memento
アンドゥ、リドゥ

## Observer
Fiber.yield

## State
実装部分で同じメソッドを使うから実装を触らない　　
それよりも一段階前の場所で代入とかで動作を変える

## Strategy
Stateよりも1個先（実装部分）で、アルゴリズムを選択する

## Template  Method
クラスの雛形作って mix-in オーバーライド

## Visitor
`yield`
