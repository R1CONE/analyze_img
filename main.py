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

else:
    print("Указанной папки не существует.")
