from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye and hello! and everything! </div>
</body>
</html>
"""
# Once we cab navigate by TagName, find or find_all
soup = BeautifulSoup(html, "html.parser")  # specify format -> can also do XML
print(soup)  # representation is an html string
print(type(soup))  # it is however a class and has methods
b = print(soup.body)

example1 = soup.find(id="first")  # div.id
example2 = soup.find_all(class_="special")  #class is reserved word

#select based off of attributes
example3 = soup.find_all(attrs={"data-example": "yes"})
print(example3)
