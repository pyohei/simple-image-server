<html>

  <head>
	<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=10.0, user-scalable=yes">
	<meta name="apple-mobile-web-app-capable" content="no">
    <link media="only screen and (max-device-width:480px)" rel="stylesheet" type="text/css" href="/static/css/login_smart.css">
    <link media="screen and (min-device-width:481px)" rel="stylesheet" type="text/css" href="/static/css/login.css">
	

    <title>ぴよっくま</title>
  </head>

  <body>
    <h1>ぴよっくま</h1>
    % if error:
        <font color="#ff0000"><b>${error}</b></font>
    % endif
    <form name="login" method="post" action="/images">
      <div class="loginform">
	    <div>
          ユーザー名:<input type="text" name="username" size="10">
        </div>
        <div>
          パスワード:<input type="password" name="userpass" size="10">
        </div>
        <input type="submit" value="ログイン">
      </div>
	  <p class="copyright">
	    Copyright © 2015 Pyohei. All Right Reserved.
	  </p>
    </form>
  </body>
</html>
