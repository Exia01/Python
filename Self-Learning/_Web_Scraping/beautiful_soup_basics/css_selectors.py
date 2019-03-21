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
soup = BeautifulSoup(html, "html.parser")

d = soup.select("#first") #when using select we get a list back
print(d)

example = soup.find(id="first")
print(example)

example = soup.select(".special")
example = soup.select("div")
example = soup.select("div")
example = soup.select("[data-example]")  # list of 2 items 

""" Long winded explanation """

# #fin an element with an id foo
soup.find(id="foo")
soup.select("#foo")[0]

# #find all elements with a class of bar
# #note that - class - is a reserved word in python
soup.find_all(class_="bar")
soup.select(".bar")

# #find all element with a data attribute of "baz"
# #using the general attrs kwarg
soup.find_all(attrs={"data-baz": True})
soup.select('[data-baz]')