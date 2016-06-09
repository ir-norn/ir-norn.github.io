---
layout: sns
title: profile
permalink: /in/sns/profile.cgi
---
print <<-CGITEXT
profile

CGITEXT
require"yaml"
p YAML.load_file("up/id_0/conf.yaml")
