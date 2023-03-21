from pathlib import Path
import shutil

folders = ['settings', 'mainapp', 'authapp']
settings = ['__init__.py', 'dev.py', 'prod.py']
files = ['__init__.py', 'models.py', 'views.py']
file = ['base.html', 'index.html']

for f in folders:
    p = Path(f'my_project/{f}')
    p.mkdir(parents=True, exist_ok=True)

for i in settings:
    with open(f'my_project/settings/{i}', 'w'):
        pass

for i in files:
    p = Path(f'my_project/mainapp/templates/mainapp')
    p.mkdir(parents=True, exist_ok=True)
    p = Path(f'my_project/authapp/templates/authapp')
    p.mkdir(parents=True, exist_ok=True)
    for j in file:
        with open(f'my_project/mainapp/templates/mainapp/{j}', 'w'):
            pass
        with open(f'my_project/authapp/templates/authapp/{j}', 'w'):
            pass
    with open(f'my_project/mainapp/{i}', 'w'):
        pass
    with open(f'my_project/authapp/{i}', 'w'):
        pass


try:
    shutil.copytree('my_project/mainapp/templates', 'my_project/templates')
except FileNotFoundError:
    print(FileNotFoundError)
    print('Такого пути не существует')
except FileExistsError:
    print(FileExistsError)
    print('Такая папка или файл уже существует')

try:
    shutil.copytree('my_project/authapp/templates/authapp', 'my_project/templates/authapp')
except FileNotFoundError:
    print(FileNotFoundError)
    print('Такого пути не существует')
except FileExistsError:
    print(FileExistsError)
    print('Такая папка или файл уже существует')