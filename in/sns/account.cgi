---
layout: sns
title: account
permalink: /in/sns/account.cgi
---
print <<-CGITEXT
<pre>
account create page

CGITEXT

require "yaml"
require "FileUtils"
folder = "up"
id = instance_exec do
  conf = YAML.load_file("conf.yaml")
  conf["id_count"] += 1
  YAML.dump( conf , open('conf.yaml', 'w') )
  conf["id_count"]
end
key = 8.times.map do ("a".."z").to_a.sample end.join
conf = {
  "key" => "#{id}_#{key}"
}
p conf
path = "#{folder}/#{id}/"
FileUtils.mkdir_p(path) unless FileTest.exist?(path)
YAML.dump( conf , open("#{folder}/#{id}/conf.yaml", 'w') )

print <<-CGITEXT
アカウント生成情報
ID : #{id}
key : #{id}_#{key}

CGITEXT
