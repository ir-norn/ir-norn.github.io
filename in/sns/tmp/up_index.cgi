---
layout: dxruby
---
#!/usr/local/bin/ruby
require 'cgi'

print "Content-type: text/html\n\n";


# -- up html --
# **/
dir = Dir["*.{jpg,png,gif}"].map do |m|
	"<a href='#{m}'>#{m}</a><br>"
end
print <<-TEXT
<html><head><title> test_uploder </title></head>
<body text="#bb99aa" link="#8c9bd7" vlink="#8c9bd7" hlink="#8c9bd7" alink="#042337">
<table align="right" width="40%"><td align="left"><pre>
#{dir.join}
</pre>
</td></table>

<form method="POST" enctype="multipart/form-data" action="up.cgi">
  file <input type="FILE" name="file">
<input type="submit" value="upload">
</form>
<form method="POST" enctype="multipart/form-data" action="up.cgi">
  delete_num <input type="input" name="del_file">
<input type="submit" value="delete">
</form>
<a href="#"> reload </a>

</body></html>
TEXT



# --- itiran ---

folder = "up"

print '<hr color="#88ccaa" size="5" width="350" align="left">'

Dir["#{folder}/*.{jpg,png}"].sort do | a , b |
  File.mtime(b) <=> File.mtime(a)
end.each_with_index do | m , i |
  mtime = File.mtime    m
  size  = File.size     m
  m     = File.basename m
  print "#{i} _ <a href=#{folder}/#{m}><img src='#{folder}/#{m}' width='400'></a>\n"
#  print "#{i} _ <a href=#{folder}/#{m}><img src='#{folder}/#{m}' height='200'></a> __ #{size} byte \n"
#  print " _____ #{mtime} <br>\n"


end
