<!DOCTYPE html><html lang="en"><head>

  <meta charset="UTF-8">

<title>Module Detection </title>
  
<link rel="stylesheet" href="/assets/css/reset.min.css">
<link rel="stylesheet" href="/assets/css/style.css">



  <script>
  window.console = window.console || function(t) {};
  var consoleWarn = window.console.warn;
  function warn(){ consoleWarn.apply(console, arguments); }
  window.open = function(){ warn("window.open is disabled."); };
  window.print   = function(){ warn("window.print is disabled."); };
  window.alert   = function(){ warn("window.alert is disabled."); };
  window.confirm = function(){ warn("window.confirm is disabled."); };
  window.prompt  = function(){ warn("window.prompt is disabled."); };
  window.Notification = function() { warn("HTML5 notifications are disabled."); };
</script>

  
  
  <script>
  if (document.location.search.match(/type=embed/gi)) {
    window.parent.postMessage("resize", "*");
  }
</script>


</head>

<body translate="no">
  <div class="cntr">
	<div class="cntr-innr">
        <form method="POST" action="">
	    <label class="search" for="inpt_search">
			<input id="inpt_search" type="text" name="search" value="{{ isset($data) ? rtrim($data->text ) : "" }}">
	    </label>
        </form>
        @if (isset($data))
        <p>Keywork "<span style="color: coral">{{ rtrim($data->text ) }}</span>" is <span style="color: coral">{{ $data->result }}</span>.</p>
        @endif

	</div>
</div>
    <script src="/assets/js/stopExecutionOnTimeout.js"></script>

    <script src="/assets/js/zepto.min.js"></script>
      <script id="rendered-js">
$("#inpt_search").on('focus', function () {
  $(this).parent('label').addClass('active');

});


$("#inpt_search").on('blur', function () {
  if ($(this).val().length == 0)
  $(this).parent('label').removeClass('active');
});
//# sourceURL=pen.js
    </script>

  


 
</body></html>