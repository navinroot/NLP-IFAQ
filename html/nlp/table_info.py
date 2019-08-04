#!/usr/bin/env python
import sys
sentence = str(sys.argv[1])

from xml.etree.ElementTree import fromstring

fo = open("input/html_table.txt", "r+")
htm= fo.read();
fo.closed



def table_remove(html,st):
  start=0
  res=""
  var=1
  while (var==1):
    end=html.find("""/table""",start)+8
    if (end-8)<0:
      break
    str=html[start:end]
    start=end
    tree = fromstring(str)
    rows = tree.findall("tr")
    headrow = rows[0]
    datarows = rows[1:]
    for i in range(0,len(rows)):
      for j in range(0,len(rows[0])):
        if(rows[i][j].text==st):
          for k in range(len(rows[0])):
            res=res+rows[0][k].text+'='+rows[i][k].text+'\t,'
          res=res+'\n'
    return res


print table_remove(htm,sentence)
