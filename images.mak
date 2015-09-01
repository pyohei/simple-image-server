<html>
  <head>
    <title>hoge</title>
  </head>
  <body>
  hogehoge
% for i in images:
    <img src="/static/images/${i}" width="50" height="50"><br>
% endfor

  <form name="logout" method="post" action="/logout">
    <input type="submit" value="ログアウト">
  </form>
  </body>
</html>
