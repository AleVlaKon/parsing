from bs4 import BeautifulSoup

html = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Пример .parent</title>
</head>

<body>
<div id="parent-container">
    <h1 id="main-heading">Заголовок (.parent)</h1>
    <p id="paragraph">Текст абзаца ()</p>
    
    <ul id="list">
        <li class="list-item">Элемент списка 1</li>
        <li class="list-item">Элемент списка 2</li>
    </ul>
</div>

</body>
</html>

'''

soup = BeautifulSoup(html, "html.parser")
li_elem = soup.find('li', class_='list-item')
parent_elem = li_elem.parent

# Выводим содержимое родительского элемента
print(parent_elem)