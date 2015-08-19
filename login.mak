<html>
  <head>
    <title>hoge</title>
  </head>
  <body>
    <form name="login" method="post" action="/menu">
  	<div>ぴよっくま</div>
	<div>
	  <div>
	    ユーザー名
	    <input type="text" name="username" size="10">
      </div>
      <div>
        パスワード
        <input type="password" name="userpass" size="10">
      </div>
	</div>
	<input type="submit">

    </form>

    <b>hello login</b>
    <p>${hoge}</p>
    % for n in piyo:
        ${n}<br>
    % endfor
<%
    rows = [[v for v in range(1, 10)] for row in range(0, 10)]
%>
<table>
    % for row in rows:
        ${makerow(row)}
    % endfor
</table>
<%def name="makerow(row)">
    <tr>
    % for name in row:
        <td>${name}</td>\
    % endfor
    </tr>
</%def>
  </body>
</html>
