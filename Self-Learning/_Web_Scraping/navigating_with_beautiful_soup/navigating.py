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
    <li>This list item is not special.</li>
    <li class="special">This list item is also special.</li>
  </ol>
  <div data-example="yes">bye and hello! and everything! </div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

#navigating via tags
#First, find the body
body_tag = soup.body
body_contents = soup.body.contents
data = body_contents[1].contents
# data2 = body_contents[1].next_sibling.next_sibling #ol
data2 = soup.find(class_="super-special").parent.parent
print(data2)

#via searching
data = soup.find(id="first").find_next_sibling().find_next_sibling()  #does not give the new line

data = soup.select("[data-example]")[1].find_previous_sibling()
data = data2 = soup.find(class_="super-special").find_next_sibling(class_="special")
print(data)


data = soup.find("h3").find_parent()
print(data)