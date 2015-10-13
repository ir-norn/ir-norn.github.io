---
layout: page
title: illust_test
permalink: /illust_test/
---


<style>
ul.bxslider img {
   width:400px;
}
</style>
<div style="width:400px;background:#eee;">
<ul class="bxslider">
  <li><img src="{{ site.baseurl }}/img/0.jpg"></li>
  <li><img src="{{ site.baseurl }}/img/1.jpg"></li>
  <li><img src="{{ site.baseurl }}/img/2.jpg"></li>
  <li><img src="{{ site.baseurl }}/img/3.jpg"></li>
</ul>
</div>

<script>
$(document).ready(function(){
  $('.bxslider').bxSlider({
    auto: true,
    pause: 3500,
    speed: 800,
    mode: 'fade',
    pager:true,
  });
});
</script>

