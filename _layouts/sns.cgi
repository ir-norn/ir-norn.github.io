#!/usr/local/bin/ruby
require 'cgi'


print "Content-type: text/html\n\n";

# --  --
print <<-TEXT
<html><head><title> remillia </title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style></style>
<link type="text/css" rel="stylesheet" href="{{ site.baseurl }}in/sns/css.css" />
<link type="text/css" rel="stylesheet" href="{{ site.baseurl }}script/jQuery.mmenu-master/demo/css/demo.css" />
<link type="text/css" rel="stylesheet" href="{{ site.baseurl }}script/jQuery.mmenu-master/dist/css/jquery.mmenu.all.css" />

<script type="text/javascript" src="http://code.jquery.com/jquery-2.2.0.js"></script>
<script type="text/javascript" src="{{ site.baseurl }}script/jQuery.mmenu-master/dist/js/jquery.mmenu.all.min.js"></script>
<script type="text/javascript">
  $(function() { $('nav#menu').mmenu(); });
</script>
</head><body>


<div id="page">
  <div class="header">
    <a href="#menu"></a>
    ----
  </div>
TEXT

begin
  {{ content }}
rescue
  print $!
end


print <<-TEXT
<nav id="menu">
  <ul>
    <li><a href="./top.cgi">top</a></li>
    <li><a href="./tl.cgi">TL</a></li>
    <li><a href="./mesaage.cgi">メッセージ</a></li>
    <li><a href="./setting.cgi">設定</a>
      <ul>
        <li><a href="./profile.cgi">プロフィール</a></li>
        <li><a href="./logout.cgi">ログアウト</a></li>
      </ul>
    </li>
    <li><a href="./search.cgi">検索</a></li>
    <li><a href="./upload.cgi">upload</a>
  </ul>
</nav>

</div>

</body></html>
TEXT
