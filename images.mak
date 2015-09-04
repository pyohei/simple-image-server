<html>
  <head>
    <title>hoge</title>
    <link rel="stylesheet" type="text/css" href="/static/js/tosrus/css/jquery.tosrus.all.css" />
    <link rel="stylesheet" type="text/css" href="/static/css/image.css" />
  </head>
  <body>
  <script type="text/javascript" src="/static/js/tosrus/jquery.js"></script>
  <script type="text/javascript" src="/static/js/tosrus/js/jquery.tosrus.min.all.js"></script>
  <h1>よんくま一覧</h1>
	<div id="links" class="kumaimages">
	% for i in images:
	  <a href="/static/images/${i}">
		<img src="/static/images/${i}" width="20%" height="20%" />
	  </a>
	% endfor
	</div>

<script type="text/javascript">
  $(document).ready(function() {
    $("#links a").tosrus();
  });
</script>

  </body>
</html>
