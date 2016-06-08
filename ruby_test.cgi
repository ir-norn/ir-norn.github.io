# -*- coding: utf-8 -*-

$SAFE=1
require 'cgi'


cgi = CGI.new




#ヘッダー出力
cgi.out("type" => "text/html" ,
        "charset" => "UTF-8") {

  #from 情報取得
  get = cgi['get']
  get = cgi.params


  #コンテツ出力
  "<html><body>" +
  "this is test page <br>あ" +
  "get = #{get} <br>" +
  "</html></body>"



}
