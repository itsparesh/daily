import datetime
import os

def update_file():
    filename = 'last_updated.txt'
    with open(filename, 'w') as file:
        file.write(f"Last updated: {datetime.datetime.now()}")
    
    os.system('git config --global user.email "master.pareshkrishna@gmail.com"')
    os.system('git config --global user.name "itsparesh"')
    os.system(f'git add {filename}')
    os.system('git commit -m "Daily update"')
    os.system('git push')

if __name__ == "__main__":
    update_file()
