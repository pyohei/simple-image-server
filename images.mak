<html>
  <head>
    <title>ぴよくま一覧</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=10.0, user-scalable=yes">
    <meta name="apple-mobile-web-app-capable" content="no">
    <link media="only screen and (max-device-width:480px)" rel="stylesheet" type="text/css" href="/static/css/image_smart.css">
    <link media="screen and (min-device-width:481px)" rel="stylesheet" type="text/css" href="/static/css/image.css">
    <link rel="stylesheet" type="text/css" href="/static/js/tosrus/css/jquery.tosrus.all.css" />
  </head>
  <body>
  <!-- <script type="text/javascript" src="/static/js/tosrus/jquery.js"></script> -->
  <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
  <script type="text/javascript" src="http://cdn.jsdelivr.net/hammerjs/2.0.3/hammer.min.js"></script>
  <script type="text/javascript" src="http://s7.addthis.com/js/250/addthis_widget.js"></script>
  <script type="text/javascript" src="/static/js/tosrus/js/jquery.tosrus.min.all.js"></script>
  <script type="text/javascript" src="/static/js/imagelist.js"></script>
  <script type="text/javascript">
    var _gaq = _gaq || [];
    _gaq.push(["_setAccount", "UA-5722599-14"]);
    _gaq.push(["_trackPageview"]);

    (function() {
      var ga = document.createElement("script");
      ga.type = "text/javascript";
      ga.async = true;
      ga.src = ("https:" == document.location.protocol ? "https://ssl" : "http://www") + ".google-analytics.com/ga.js";
      var s = document.getElementsByTagName("script")[0]; 
      s.parentNode.insertBefore(ga, s);
    })();
  </script>

  <h1>よんくま一覧</h1>
  <div id="kumalinks" class="kumaimages example thumbs">
    % for i in images:
      <a href="${i}">
        <img src="${i}" width="8.5%" height="16%" />
      </a>
    % endfor
  </div>
  </body>
</html>
