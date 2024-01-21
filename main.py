import os
import easyocr


folder_path = input("Enter your adress for folder without "" with your pictures: ")




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

    amount_files = len(ready_list)
    print("Number of files:", amount_files)

    for i in range(1, amount_files + 1):
        globals()[f"text_{i}"] = f"This is text for file {i}"

else: print('folder dont exist')



def text_recognition(file_path):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(file_path, detail=0, paragraph=True)

    return result




def main():

    folder_for_save = input("Enter your adress for folder to text your pictures "": ")

    if os.path.exists(folder_for_save):


        text_variables = []

        for i, file_path in enumerate(ready_list):
            text_variable_name = f"text_{i + 1}"
            text_variables.append(text_variable_name)
            locals()[text_variable_name] = text_recognition(file_path=file_path)
            print(f'{text_variable_name}: {locals()[text_variable_name]}')


            text_1 = os.path.join(folder_for_save, "text_1.txt")

         
if __name__ == "__main__":
    main()



