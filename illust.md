---
layout: page
title: illust
permalink: /illust/
---

<!--
x434
<script type="text/javascript">$('#contents li').wookmark();</script>
<div id="contents">
    <ul id="tiles">
  <li><img src="{{ site.baseurl }}/images/illust1.jpg"></li>
  <li><img src="{{ site.baseurl }}/images/illust2.jpg"></li>
  <li><img src="{{ site.baseurl }}/images/illust3.jpg"></li>
  <li><img src="{{ site.baseurl }}/images/illust4.jpg"></li>
  <li><img src="{{ site.baseurl }}/images/illust5.jpg"></li>
  <li><img src="{{ site.baseurl }}/images/illust6.jpg"></li>
    </ul>
</div>
-->



<style>
ul.bxslider img {
   xwidth:400px;
   height:300px;
}
</style>
<div style="width:400px;">
<ul class="bxslider">
  <li><img src="{{ site.baseurl }}/images/illust1.jpg"></li>
  <li><img src="{{ site.baseurl }}/images/illust2.jpg"></li>
  <li><img src="{{ site.baseurl }}/images/illust3.jpg"></li>
  <li><img src="{{ site.baseurl }}/images/illust4.jpg"></li>
  <li><img src="{{ site.baseurl }}/images/illust5.jpg"></li>
  <li><img src="{{ site.baseurl }}/images/illust6.jpg"></li>
</ul>
</div>

<script>
$(document).ready(function(){
  $('.bxslider').bxSlider({
    auto: true,
    pause: 5200,
    speed: 800,
    mode: 'fade',
    pager:true,
  });
});
</script>
