#!/usr/bin/env python3
import cgi
import cgitb
import html

from table_class import Table


def display_element(element, name):
    atomic_mass_value = str(round(element.atomic_mass, 4))
    atomic_mass = ('[' + atomic_mass_value + ']', atomic_mass_value)[element.is_stable]
    print(
        '<td class = "%s show" id = %s><a href="https://ru.wikipedia.org/wiki/%s"><span>%d</span><br>%s<br><div>%s</div></a></td>' % (
            element.block.name, element.symbol, name, element.number, element.symbol, atomic_mass))

cgitb.enable()
form = cgi.FieldStorage()
current_year = "2016"
given_year = form.getfirst("year", current_year)
given_year = int(html.escape(given_year))

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Динамическая периодическая таблица</title>
            <link type="text/css" rel="stylesheet" href="/stylesheet.css" />
            <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
        </head>
        <body>""")
print("""<script type="text/javascript" src="../ajax.js"></script>""")

print("<h2>Периодическая таблица элементов, открытых к <span>{}</span> году:</h2>".format(given_year))
print()

print("<table><tbody><tr>")
print('<th class="header">Группа</th>')
for number in range(1, 19):
    print('<th class="header">{}</th>'.format(number))
print('</tr>')

print('<tr><th class="header">Период</th><td colspan="18"></td></tr>')
ptable = Table()
for elem in ptable.get_ordinary_elements():
    if elem.group == 1:
        print('<tr><th class="header">%d</th>' % elem.period)
    display_element(elem, (elem.name, 'Бор_(элемент)')[elem.symbol == 'B'])
    if elem.symbol == 'H':
        print('<td colspan="16"></td>')
    elif elem.symbol == 'Be' or elem.symbol == 'Mg':
        print('<td colspan="10"></td>')
    elif elem.group == 18:
        print('</tr>')
print('<tr><td>&nbsp;</td><td colspan="18"></td></tr>')
print('<tr> <th class = "header" colspan="3"><a href = "https://ru.wikipedia.org/wiki/Лантаноиды">Лантаноиды</a></th>')
print('<td></td>')

for element in ptable.get_lantanoids():
    display_element(element, element.name)
print('<td></td></tr>')
print('<tr> <th class = "header" colspan="3"><a href = "https://ru.wikipedia.org/wiki/Актиноиды">Актиноиды</a></th>')
print('<td></td>')
for element in ptable.get_actinoids():
    display_element(element, element.name)

print('<td></td></tr></tbody></table>')
print('<br>')
print("""<form action="/cgi-bin/form.py">
        <input type="range" min="1249" max="%s" step="1" value="%s" name="year" id="year" onchange="do_get()">
    </form>""" % (current_year, given_year))
print("</body></html>")
