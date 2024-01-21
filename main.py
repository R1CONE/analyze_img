import os
import easyocr


folder_path = input("Enter your adress for folder without "": ")


if os.path.exists(folder_path):

    files = os.listdir(folder_path)
    print("files in folder :")
    

    file_list = []
    for file in files:
        print(file)
        file_list.append(file)

        images_list = [file for file in file_list if file.endswith('.png')]

    print("PNG files in :", images_list)

    ready_list = []

    for image in images_list:
        full_path = os.path.join(folder_path, image)
        ready_list.append(full_path)

    print("Full paths of PNG files in ready_list:", ready_list)

else:
    print("Указанной папки не существует.")


def text_recognition(file_path):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(file_path, detail=0, paragraph=True)

    return result

def main():
    file_path = ready_list[0]
    print(text_recognition(file_path=file_path))

if __name__ == "__main__":
    main()



