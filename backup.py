#!/usr/bin/env python3
import cgi
import cgitb
import html

from table_class import Table


cgitb.enable()
form = cgi.FieldStorage()
given_year = form.getfirst("year", "2016")
given_year = int(html.escape(given_year))

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Динамическая периодическая таблица</title>
            <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
            <script>
                var given_year = $('#year').val();
                $( refresh() {
                $('#year').slide( function() {
                  $.get( 'http://localhost:8000/cgi-bin/form.py',
                  given_year,
                  success: function(html){
                        $("#content").html(html);
                    }  );
                } );
        </head>
        <body>""")

print('<div id="content">')
print("<p>{}</p>".format(given_year))
print("""<form action="/cgi-bin/form.py">
        <input type="range" min="1249" max="2016" step="1" value="{}" name="year">
        <input type="submit">
    </form>""".format(given_year))

print("<center> <h2>Периодическая таблица элементов, открытых к {} году:</h2></center>".format(given_year))
print()

print("""<link type="text/css" rel="stylesheet" href="/stylesheet.css" />
<table summary="Periodic table. Long form.">
<tbody><tr>""")
print('<th class="header">Группа</th>')
for number in range(1, 19):
    print('<th class="header">{}</th>'.format(number))
print('</tr>')

print('<tr><th class="header">Период</th><td colspan="19"></td></tr>')
ptable = Table()
for elem in ptable.get_ordinary_elements():
    if elem.group == 1:
        print('<tr><th class="header">%d</th>' % elem.period)
    if elem in ptable.get_discovered_elements(given_year):
        block_show = elem.block.name + "_show"
    else:
        block_show = elem.block.name + "_hide"
    if elem.stability:
        atomic_mass = str(round(elem.atomic_mass, 4))
    else:
        atomic_mass = '[' + str(round(elem.atomic_mass, 4)) + ']'
    print('<td class = %s><a href="https://ru.wikipedia.org/wiki/%s"><span>%d</span><br>%s<br><div>%s</div></a></td>' % (block_show, elem.symbol, elem.number, elem.symbol, atomic_mass))
    if elem.symbol == 'H':
        print('<td colspan="16"></td>')
    elif elem.symbol == 'Be' or elem.symbol == 'Mg':
        print('<td colspan="10"></td>')
    elif elem.group == 18:
        print('</tr>')
print('<tr><td>&nbsp;</td><td colspan="19"></td></tr>')
print('<tr> <th class = "header" colspan="3"><a href = "https://ru.wikipedia.org/wiki/Лантаноиды">Лантаноиды</a></th>')
print('<td></td>')
for element in ptable.get_lantanoids():
    if element in ptable.get_discovered_elements(given_year):
        block_show = element.block.name + "_show"
    else:
        block_show = element.block.name + "_hide"
    if elem.stability:
        atomic_mass = str(round(elem.atomic_mass, 4))
    else:
        atomic_mass = '[' + str(round(elem.atomic_mass, 4)) + ']'
    print('<td class = %s><a href="https://ru.wikipedia.org/wiki/%s"><span>%d</span><br>%s<br><div>%s</div></a></td>' % (block_show, element.symbol, element.number, element.symbol, atomic_mass))
print('</tr>')
print('<tr> <th class = "header" colspan="3"><a href = "https://ru.wikipedia.org/wiki/Актиноиды">Актиноиды</a></th>')
print('<td></td>')
for element in ptable.get_actinoids():
    if element in ptable.get_discovered_elements(given_year):
        block_show = element.block.name + "_show"
    else:
        block_show = element.block.name + "_hide"
    if elem.stability:
        atomic_mass = str(round(elem.atomic_mass, 4))
    else:
        atomic_mass = '[' + str(round(elem.atomic_mass, 4)) + ']'
    print('<td class = %s><a href="https://ru.wikipedia.org/wiki/%s"><span>%d</span><br>%s<br><div>%s</div></a></td>' % (block_show, element.symbol, element.number, element.symbol, atomic_mass))
print('</tr>')
print('</div>')