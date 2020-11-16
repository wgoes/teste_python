from selenium.webdriver import Chrome

#variáveis:
cont = 0

browser = Chrome()
url = "https://selenium-python.readthedocs.io/"
browser.get(url)

element = browser.find_element_by_link_text('2. Getting Started')
txt_element = element.text.replace(" ", "")
element.click()

while (cont < len(txt_element)):
    caracter = txt_element[cont]
    result = txt_element.find(caracter, cont + 1, len(txt_element))
    if result == -1:
        cont = cont + 1
        print("Caracter " + caracter + " Não se repete")
    else:
        print("Possui caracteres repetidos")
        break


# browser.quit()
