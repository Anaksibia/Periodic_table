#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
given_year = form.getfirst("year", "None")

print("Content-type: text/html")
print()
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Discovered elements by</h1>")
print("<p>year: {}</p>".format(given_year))

print("""</body>
        </html>""")