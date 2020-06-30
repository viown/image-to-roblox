import main
from os import system

while True:
    name = input("Choose a name for your file: ")
    file = ''
    while True:
        file = input("Name of the file you want to convert (has to be in the images folder): ")
        if not (file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg")):
            print("Invalid file format, make sure to add .png, .jpg, or whatever file format your image is!")
        else:
            break
    try:
        print("Converting... this may take a while.")
        convert = main.convert(file)
        with open(f'scripts/{name}.lua', 'w') as f:
            f.write(convert)
        print(f"Successfully converted, you can find your file: {name}.lua in the scripts folder!")
        input()
        system("cls")
    except Exception as e:
        print(f"Failed to convert due to the following error: {e}")