<!DOCTYPE html>
<html>
<head>
<title>HelloWorld</title>
</head>
<body>
<p>
Welcome {{username}}
<p>
<ul>
%for thing in things:
<li>{{thing}}</li>
%end
</ul>
<p>
<form action="/favorite_fruit" method="POST">
What is your Favorite Fruit?
<input type="text" name="fruit" size="40" value=""><br>
<input type="submit" name="submit" value="Submit">
</body>
</html>
