
// hedder
$(document).ready(function(){
  $('.bxslider').bxSlider({
    controls: false,
    auto: true,
    pause: 5200,
    speed: 800,
    mode: 'fade',
    pager:true,
  });
});

// tab menu
//      show: { opacity: 'toggle', duration: 'normal', }
//      show: { effect:"fade", duration: 100 }
$(function() {
  var tabs = $( "#tabs" ).tabs({
    collapsible: true ,
    show: { opacity: 'toggle', duration: 'normal', }
  });
  tabs.find( ".ui-tabs-nav" ).sortable({
    axis: "x",
    stop: function() {
      tabs.tabs( "refresh" );
    }
  });
});
// ----------
$(document).ready(function(){
  //Examples of how to assign the Colorbox event to elements
  $(".group1").colorbox({rel:'group1'});
  $(".group2").colorbox({rel:'group2', transition:"fade"});
  $(".blog_img").colorbox({rel:'blog_img', transition:"fade", width:"75%", height:"75%"});
  $(".blog_2015_10_13").colorbox({rel:'blog_2015_10_13', transition:"fade", width:"75%", height:"75%"});
  $(".group4").colorbox({rel:'group4', slideshow:true});
  $(".ajax").colorbox();
  $(".youtube").colorbox({iframe:true, innerWidth:640, innerHeight:390});
  $(".vimeo").colorbox({iframe:true, innerWidth:500, innerHeight:409});
  $(".iframe").colorbox({iframe:true, width:"80%", height:"80%"});
  $(".inline").colorbox({inline:true, width:"50%"});
  $(".callbacks").colorbox({
    onOpen:function(){ alert('onOpen: colorbox is about to open'); },
    onLoad:function(){ alert('onLoad: colorbox has started to load the targeted content'); },
    onComplete:function(){ alert('onComplete: colorbox has displayed the loaded content'); },
    onCleanup:function(){ alert('onCleanup: colorbox has begun the close process'); },
    onClosed:function(){ alert('onClosed: colorbox has completely closed'); }
  });
  $('.non-retina').colorbox({rel:'group5', transition:'none'})
  $('.retina').colorbox({rel:'group5', transition:'none', retinaImage:true, retinaUrl:true});
  //Example of preserving a JavaScript event for inline calls.
  $("#click").click(function(){
    $('#click').css({"background-color":"#f00", "color":"#fff", "cursor":"inherit"}).text("Open this window again and this message will still be here.");
    return false;
  });
});

// side menu
$(function(){
  $( "#accordion" )
    .accordion({
      collapsible: true,
      header: "> div > h3"
    })
    .sortable({
      axis: "y",
      handle: "h3",
      stop: function( event, ui ) {
        // IE doesn't register the blur when sorting
        // so trigger focusout handlers to remove .ui-state-focus
        ui.item.children( "h3" ).triggerHandler( "focusout" );
        // Refresh accordion to handle new order
        $( this ).accordion( "refresh" );
      }
    });
    // .dcAccordion({
    //   eventType: 'click',
    //   autoClose: false,
    //   saveState: true,
    //   disableLink: true,
    //   showCount: true,
    //   speed: 'fast'
    // });
});

$( "#datepicker" ).datepicker({ inline: true });
