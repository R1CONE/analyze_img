import os
print("РУ")

def analyze_folder(folder_path):
    try:
        # Получаем список файлов и подпапок
        contents = os.listdir(folder_path)

        print(f"Содержимое папки {folder_path}:")
        for item in contents:
            item_path = os.path.join(folder_path, item)

            # Проверяем, является ли элемент файлом или подпапкой
            if os.path.isfile(item_path):
                print(f"Файл: {item}")
            elif os.path.isdir(item_path):
                print(f"Папка: {item}")

    except FileNotFoundError:
        print(f"Папка {folder_path} не найдена.")
    except PermissionError:
        print(f"Отсутствует доступ к папке {folder_path}.")

# Замените 'путь/к/папке' на путь к вашей папке
folder_path = 'C:\Users\Asus\Desktop\analyze image\images'
analyze_folder(folder_path)