#!/usr/local/bin/ruby
require 'cgi'
require "yaml"
print "Content-type: text/html\n\n";


# imf-file & yaml output
def func folder , id , filename , params
  ext = File.extname filename
  file_count = instance_exec do
    conf = YAML.load_file("conf.yaml")
    conf["file_count"] += 1
    YAML.dump( conf , open('conf.yaml', 'w') )
    conf["file_count"]
  end
  instance_exec do
    conf = YAML.load_file("#{folder}/#{id}/conf.yaml")
    hs = ["title","caption","tag"].inject Hash.new do| hs , m |
       hs.merge(m => (params[ m ] ? params[ m ].first : "null") )
    end.merge("ext"=>ext)
    conf["file"] << {
      "num" => file_count ,
      "time" => Time.new.strftime("%Y_%m_%d_%H_%M_%S_%N") ,
    }.merge(hs)
    YAML.dump( conf , open("#{folder}/#{id}/conf.yaml", 'w') )
  end
  p Dir.getwd + "/#{folder}/#{id}/" + file_count.to_s + ext
end


folder = "up"
cgi = CGI.new
value = cgi.params["file"].first
key   = cgi.params["key"].first
id , pass = key.split(/_/)
yaml = YAML.load_file("#{folder}/#{id}/conf.yaml")
# --- up load ---
begin
  raise "key err" unless yaml["key"] == key
  raise "ext_name_err" unless File.extname( value.original_filename ) =~ /\.jpg$|\.png$/
  raise "size over" if 10_000_000 < value.size
  mkfile = func folder , id , value.original_filename , cgi.params
#  mkfile = Dir.getwd + "/#{folder}/#{id}/" + value.original_filename.gsub(/[^\w!\#$%&()=^~|@`\[\]\{\};+,.-]/u, '_')
  open( mkfile , "wb") do |f|
    f.write value.read
  end
  print "upload is " , mkfile
rescue => ev
  print ev
end


#
# # -- re direct --
# print <<-TEXT
# -up-cgi-<br>
# uploaded<br>
#
# <script type="text/javascript"><!--
#    location.href = "tl.cgi?id=#{id}";
# // --></script>
#
# TEXT
#------------------------------------------------------------
