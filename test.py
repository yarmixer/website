from bs4 import BeautifulSoup
html = """\
<li id="CardBalance" class="card_balanse">
<span class="card_info_label lite">Сумма</span>
<span class="card_info_inner">0.37 </span>
<span class="lite">руб</span>
</li>
"""

soup = BeautifulSoup(html, 'html.parser')
print(soup.find('span', 'card_info_inner').text)
print(soup.find('span', 'card_info_inner').get_text())
print(soup.find('span', 'card_info_inner').getText())