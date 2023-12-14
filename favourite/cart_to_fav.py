from os import path
import re

def main():
    with open('greatkart-pre-deploy/favourite/models.py') as file_in:
        text = file_in.read()
        text = text.replace('cart','fav')
        text = text.replace('Cart','Fav')
        print(text)

    with open("greatkart-pre-deploy/favourite/models.py","w") as file_out:
        file_out.write(text)
        print("DONE", file_out)
        
        
if __name__ == '__main__':
    main()