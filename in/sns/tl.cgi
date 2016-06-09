---
layout: sns
title: tl
permalink: /in/sns/tl.cgi
---

require "yaml"
begin
cgi = CGI.new
id = cgi.params["id"].first || "**"
folder = "up"

# x = Dir["#{folder}/#{id}/conf.yaml"].map do | yaml |
#    yaml = YAML.load_file( yaml )
#    yaml["file"]
# end
# p x[0].class
# x[0].each_with_index.map do|file,i|
#   p i,file
#   p file["num"]
#   p m  = file["num"].to_s + "." + file["ext"]
#   print "#{i} _ <a href='#{m}'><img src='#{m}' width='400'></a>\n"
# end

if cgi.params["id"].first
 print '<hr color="#88ccaa" size="5" width="350" align="left">'
 yaml = YAML.load_file("#{folder}/#{id}/conf.yaml")
 yaml["file"].map do |file|
   m = "#{folder}/#{id}/#{file['num']}.#{file['ext']}"
   print "title:#{file['title']}"
   print "user:#{id}"
   print "_ <a href='#{m}'><img src='#{m}' width='400'></a>\n"
 end
else
   # All
  print '<hr color="#88ccaa" size="5" width="350" align="left">'
  Dir["#{folder}/#{id}/*.{jpg,png}"].sort do | a , b |
    File.mtime(b) <=> File.mtime(a)
  end.each_with_index do | m , i |

    mtime = File.mtime    m
    size  = File.size     m
    print "#{i} _ <a href='#{m}'><img src='#{m}' width='400'></a>\n"
  end

end


rescue ; p $! end
