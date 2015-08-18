<html>
  <head>
    <title>hoge</title>
  </head>
  <body>
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
