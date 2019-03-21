from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" class="special">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special super-special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye and hello! and everything! </div>
</body>
</html>
"""
# Once we cab navigate by TagName, find or find_all
soup = BeautifulSoup(html, "html.parser")

el = soup.select(".special")[1]  #short for element
print(el)
print(el.get_text())

# we can also loop through the data
for el in soup.select(".special"):
  print(el.get_text())
  print(el.name)

print(el.name) #name refers to the tag
print(el.attrs)  #key value attributes for the tags


attr = soup.find("h3")["data-example"]
print(attr)