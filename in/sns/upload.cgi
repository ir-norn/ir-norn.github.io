---
layout: sns
title: upload
permalink: /in/sns/upload.cgi
---
print <<-"TEXT"
<pre>
    <form method="POST" enctype="multipart/form-data" action="up.cgi">
    file <input type="FILE" name="file">
    key
    <input type="" name="key" value="" size="16">
    タイトル
    <input name="title" size="36">
    キャプション
    <textarea name="caption" cols="100" rows="10"></textarea>
    タグ
    <input name="tag" size="36">
    年齢制限
    公開制限

    <input type="submit" value="upload">
    </form>
</pre>
TEXT


# require "yaml"
# folder = "up"
# id = "12345"
# yaml = YAML.load_file("#{folder}/#{id}/conf.yaml")
# p yaml
#
# p conf = YAML.load_file("conf.yaml")
# conf["file_count"] += 1
# YAML.dump( conf , open('conf.yaml', 'w') )
