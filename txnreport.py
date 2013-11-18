#!python

'''Windows-Tab is very cool!'''

"""
Mockup turned up a few useful bits. Here are the pieces to go after for now:
  <transaction              # txn
      id="61224"            # txn attr: id
      type="promote"        # txn attr: type
      user="knaylor">       # txn attr: user
    <comment>Sprint 13.10B : B-80877 : Add Research Alerts</comment>
                            # txn element: comment
    <version                # txn element: version
        path="\.\...\ShareBuilder.Brokerage.Web.WebSite.csproj" />
                            # version attr: path
    <version                # txn element: version
        path="\.\...\AccountOverview.ascx.cs" />
  </transaction>
"""

import time
import xml.etree.ElementTree as etree

tree = etree.parse('history.xml')
root = tree.getroot()
transactions = root.findall('transaction')

html_header = u"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" >
<head>
    <title>Transaction details for $project_$version</title>
    <link
        href="static/foundation-4.3.2/css/foundation.css"
        type="text/css"
        rel="stylesheet" />

    <script src="static/jquery-2.0.3.min.js"></script>
</head>
<body>
    <script>
        $(document).ready(function(){
            $( "button" ).click(function(){
                $( "p" ).toggle(1000);
            });
        });
    </script>
"""

#VISIBLE CONTENT HERE
#<div id="spoiler" style="display:none">
#HIDDEN CONTENT HERE
#</div>
#<button title="Click to show/hide content" type="button" onclick="if(document.getElementById('spoiler') .style.display=='none') {document.getElementById('spoiler') .style.display=''}else{document.getElementById('spoiler') .style.display='none'}">Show/hide</button>


html_footer = u"""</body>
</html>
"""

class Transaction(object):
    def __init__(self, elem):
        '''Pass in a transaction XML element'''
        # transaction's atributes
        self.id = elem.attrib['id']
        self.type = elem.attrib['type']
        self.time = elem.attrib['time']
        self.ctime = time.ctime(int(self.time))
        self.user = elem.attrib['user']

        # transaction's elements
        # zero or one comment (mkstream, chstream, keep, etc. or promote)
        self.comment = elem.find('comment')

        # zero or more source file paths (mkstream, chstream, etc., or
        # promote, keep, etc.)
        self.paths = []
        self.versions = elem.findall('version')
        [self.paths.append(version.attrib['path']) for version in self.versions]

print(html_header)
print('<h2>Transaction details for $project_$version</h2>')
print('<table>')
print('<thead>')
print('<tr>')
print('<th width="70">Txn ID</th>')
print('<th width="200">Date & Time</th>')
print('<th width="90">Txn Type</th>')
print('<th width="70">User</th>')
print('<th width="400">Comment</th>')
print('<th>Source Files')
print('<button id="show_hide">Show/hide</button>')
print('</th>')
print('</tr>')
print('</thead>')
print('<tbody>')

for txn in transactions:
    transaction = Transaction(txn)
    print('<tr>')
    print('<td>' + transaction.id + '</td>')
#    print('<td>time="' + transaction.time + '"</td>')
    print('<td>' + transaction.ctime + '</td>')
    print('<td>' + transaction.type + '</td>')
    print('<td>' + transaction.user + '</td>')
    if transaction.type != 'promote' and transaction.type != 'keep':
        continue
    print('<td>' + transaction.comment.text + '</td>')
    print('<td>')

# <p id="srcpath">
#   \.\Dependencies\Debug\ShareBuilder.Web.UI.dll<br />
#   \.\Dependencies\Release\ShareBuilder.Web.UI.dll<br />
# </p>

    # to show/hide the source paths
#    print('<div id="hide_me" style="display:none">')

#    <script>
#        $(document).ready(function(){
#            $("#hide_me").click(function(){
#                $("#srcpath").toggle(1000);
#            });
#        });
#    </script>

    for path in transaction.paths:
        print('<p>' + path + '</p>')
#    print('</div>')
    print('</td>')
    print('</tr>')

print('</tbody>')
print('</table>')
print(html_footer)
