import os
import easyocr

folder_path = input("Enter your address for the folder without spaces with your pictures: ")

if os.path.exists(folder_path):
    files = os.listdir(folder_path)
    print("Files in the folder:")

    file_list = []
    for file in files:
        print(file)
        file_list.append(file)

    images_list = [file for file in file_list if file.endswith('.png')]
    print("PNG files in:", images_list)

    ready_list = []

    for image in images_list:
        full_path = os.path.join(folder_path, image)
        ready_list.append(full_path)

    print("Full paths of PNG files in ready_list:", ready_list)

    amount_files = len(ready_list)
    print("Number of files:", amount_files)

else:
    print('Folder does not exist')


def text_recognition(file_path):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(file_path, detail=0, paragraph=True)
    return result


def main():
    folder_for_save = input("Enter your address for the folder to save your text pictures: ")

    if os.path.exists(folder_for_save):
        text_variables = []  # list with text from images

        for i in range(1, amount_files + 1):
            file_path_i = ready_list[i - 1]  # Corrected index and variable name
            globals()[f"file_path_{i}"] = file_path_i

            text = text_recognition(file_path=file_path_i)
            text_variables.append(text)

        print(text_variables)

    else:
        print('Folder does not exist')


if __name__ == "__main__":
    main()




