
<head>

    <title>Server logs</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
                        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>

    {{!get("Logs", "Error while reading logs...")}}

    <form method='GET' action='/'>
        <input class='btn btn-secondary btn-sm' value='Back to server page' type="submit"></input>
    </form>

</body>
