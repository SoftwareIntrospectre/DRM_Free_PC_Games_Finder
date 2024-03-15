# Beautiful Soup documentation:     https://www.crummy.com/software/BeautifulSoup/bs4/doc/

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# HTML as a nested data structure

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# called bs4 because it's Beautiful Soup version 4
from bs4 import BeautifulSoup
#soup  = BeautifulSoup(html_doc, 'html.parser') # uses Python's default parser (+decent speed, slower than lxml)
soup  = BeautifulSoup(html_doc, 'lxml') # +very fast -external C dependency (recommended by the documentation though)


# prints the HTML in a readable fashion
#print(soup.prettify())

print('\nNAVIGATING NESTED DATA STRUCTURE\n')
print(soup.title) #<title>The Dormouse's story</title>
print(soup.title.name) #title ---> the title tag itself
print(soup.title.string) #The Dormouse's story ---> the title tag's contents
print(soup.title.parent.name) # head ---> head tag contains metadata about the HTML document

print(soup.p) # <p class="title"><b>The Dormouse's story</b></p> ---> paragraph tag

print(soup.p['class']) #['title'] ---> prints the class of the paragraph tag --> <p class="title">

print(soup.a) #<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a> ---> prints the first instance of the anchor's (a's) contents

# prints all anchors (a)
print(soup.find_all('a'))  # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# finds the id tag labelled "link3"
print(soup.find(id="link3")) #<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print('\n\nEXTRACTING URLS\n')
for link in soup.find_all('a'):
    print(link.get('href'))


print('\n\nEXTRACTING TEXT\n')
print(soup.get_text())

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------