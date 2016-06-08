---
layout: sns
title: upload
permalink: /in/sns/upload.cgi
---

print <<-TEXT
<form method="POST" enctype="multipart/form-data" action="up.cgi">
  file <input type="FILE" name="file">
<input type="submit" value="upload">
</form>

TEXT

print <<-CGITEXT
<pre>

タイトル

キャプション

タグ

年齢制限

後悔制限


[ 投稿する ]

</pre>
CGITEXT
