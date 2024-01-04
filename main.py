import string

import os

from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio import config

@config(theme="dark",title="PasswordChecker")
async def main():
    clear()
    logo_path = os.path.join("images","logo.png")
    put_image(open(logo_path, "rb").read())
    put_markdown("## Проверка надежности пароля")
    password = await input("Введите пароль")
    if password:
        print(f"Использованый пароль:{password}")

    upper_case = any([1 if i in string.ascii_uppercase else 0 for i in password])
    lower_case = any([1 if i in string.ascii_lowercase else 0 for i in password])
    special = any([1 if i in string.punctuation else 0 for i in password])
    digits = any([1 if i in string.digits else 0 for i in password])

    length = len(password)

    if length >= 10:
        length = True
    else:
        length = False

    characters = [upper_case, lower_case, special, digits, length]

    score = 0
    for i in range(len(characters)):
        if characters[i]:
            score += 1
    if int('%s' % score) <= 2:
        put_markdown('<h2 style="color: red;">Надёжность пароля: %s из 5</h2>' % score)
        
    elif int('%s' % score) == 3:
        put_markdown('<h2 style="color: yellow;">Надёжность пароля: %s из 5</h2>' % score)
        
    elif int('%s' % score) >= 4:
        put_markdown('<h2 style="color: green;">Надёжность пароля: %s из 5</h2>' % score)
    put_button("Проверить ещё раз",onclick=main)

if __name__ == "__main__":
    start_server(main, debug=True, port=8080, cdn=False)
