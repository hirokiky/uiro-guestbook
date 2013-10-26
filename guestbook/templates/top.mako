<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link href="${request.matching.reverse('static:guestbook', path=['css', 'bootstrap.min.css'])}" rel="stylesheet" />
    <title>Uiro Guestbook</title>
</head>
<body>
<div class="container">
    <div class="page-header">
        <h1>Uiro Guestbook</h1>
        <p class="lead">powerd by <a href="https://github.com/hirokiky/uiro">Uiro Webframework</a></p>
    </div>
    ${form}
    <div class="greeting_list">
        % for greeting in greetings:
            <div class="panel panel-info">
                <div class="panel-heading">
                    <h3 class="panel-title">${greeting.name}</h3>
                    <small>${greeting.ctime}</small>
                </div>
                <div class="panel-body">${greeting.content}</div>
            </div>
        % endfor
    </div>
</div>
</body>
</html>
