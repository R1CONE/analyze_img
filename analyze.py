import easyocr

def text_recognition(file_path):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(file_path, detail=0, paragraph=True)

    return result

def main():
    file_path = input("Enter a file path: ")
    print(text_recognition(file_path=file_path))

if __name__ == "__main__":
    main()
