import os
import easyocr

# folder_path - way to folder with pictures
folder_path = input("Enter your address for the folder without spaces with your pictures: ")

if os.path.exists(folder_path):
    files = os.listdir(folder_path)
    print("Files in the folder:")

    file_list = []

    for file in files:
        print(file)

        # file_list - all files in folder
        file_list.append(file)

    images_list = [file for file in file_list if file.endswith('.png')]
    # images_list - files only with .png 
    print("PNG files in:", images_list)
    # names_files - only file names without .png
    names_files = [file[:-4] for file in images_list]

    print("names_files: ", names_files)

    ready_list = []

    for image in images_list:
        full_path = os.path.join(folder_path, image)

        # ready_list - list with full ways to images
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

        

        text_1 = str(text_variables[0])
        text_2 = str(text_variables[1])
        text_3 = str(text_variables[2])

        way_text1 = os.path.join(folder_for_save, names_files[0])
        with open(way_text1, 'w') as main_txt_file:
            main_txt_file.write(text_1)

        way_text2 = os.path.join(folder_for_save, names_files[1])
        with open(way_text2, 'w') as main_txt_file:
            main_txt_file.write(text_2)

        way_text3 = os.path.join(folder_for_save, names_files[2])
        with open(way_text3, 'w') as main_txt_file:
            main_txt_file.write(text_3)

    else:
        print('Folder does not exist')


if __name__ == "__main__":
    main()



