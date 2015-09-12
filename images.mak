<html>
  <head>
    <title>hoge</title>
    <link rel="stylesheet" type="text/css" href="/static/js/tosrus/css/jquery.tosrus.all.css" />
    <link rel="stylesheet" type="text/css" href="/static/css/image.css" />
  </head>
  <body>
  <script type="text/javascript" src="/static/js/tosrus/jquery.js"></script>
  <script type="text/javascript" src="/static/js/tosrus/js/jquery.tosrus.min.all.js"></script>
<script type="text/javascript">
  $(document).ready(function() {
    $("#links a").tosrus();
  });

</script>
  <h1>よんくま一覧</h1>
	<div id="links" class="kumaimages example thumbs">
	% for i in images:
	  <a href="/static/images/${i}">
		<img src="/static/images/${i}" width="8.5%" height="16%" />
	  </a>
	% endfor
	</div>


  </body>
</html>
