#!/usr/local/bin/ruby
require 'cgi'
print "Content-type: text/html\n\n";

folder = "up"

cgi = CGI.new
value = cgi.params["file"].first

# --- up load ---
begin
  raise "ext_name_err" unless File.extname( value.original_filename ) =~ /\.jpg$|\.png$/
  raise "size over" if 10_000_000 < value.size

  mkfile = Dir.getwd + "/#{folder}/" + value.original_filename.gsub(/[^\w!\#$%&()=^~|@`\[\]\{\};+,.-]/u, '_')
  open( mkfile , "wb") do |f|
    f.write value.read
  end
  print "upload is " , mkfile
rescue => ev
  print ev
end



# -- re direct --
print <<-TEXT
-up-cgi-<br>
uploaded<br>

<script type="text/javascript"><!--
   location.href = "index_index.cgi";
// --></script>

TEXT
#------------------------------------------------------------
