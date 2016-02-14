#!/usr/bin/env python3
import cgi
import cgitb
import json
import sys

from table_class import Table


cgitb.enable()
fs = cgi.FieldStorage()

sys.stdout.write("Content-Type: application/json\n\n")

given_year = fs.getvalue(fs.keys()[0])
array_of_elements = {}
array_of_elements["undiscovered_elements"] = [element.symbol for element in Table().get_undiscovered_elements(int(given_year))]
array_of_elements["discovered_elements"] = [element.symbol for element in Table().get_discovered_elements(int(given_year))]

sys.stdout.write(json.dumps(array_of_elements, indent=1))
sys.stdout.write("\n")

sys.stdout.close()