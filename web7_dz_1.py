from pathlib import Path

folders = ['settings', 'mainapp', 'adminapp', 'authapp']

for i in folders:
    p = Path(f'my_projekt/{i}')
    p.mkdir(parents=True, exist_ok=True)