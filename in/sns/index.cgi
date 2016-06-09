---
layout: sns
title: index
permalink: /in/sns/index.cgi
---
print <<-CGITEXT
index
<pre>
CGITEXT

form = CGI.new

Pass_list = [
  "1234",
  "abcd"
]

if Pass_list.include? form['pass']
  print <<-"END"
      ようこそ！！
  END
else
  p form['pass']
  print <<-"END"
      <form action="#{ENV['SCRIPT_NAME']}" method="POST">
      パスワードを入力してください。<br>
      <input type="password" name="pass" value="" size="16">
      <input type="submit" value="送信">
      </form>
  END
end
