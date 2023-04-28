import xml.etree.ElementTree as ET


try:
    filename = input("Filename: ")
    extension = filename.split(".")[-1].lower()

    f = open(filename)

    if extension == "xml":
        tree = ET.parse(f)
        root = tree.getroot()
        print("XML file loaded")
        f.close()  # закрытие файла после использования
    else:
        print("unsupported file type ... exiting")
        exit()

except Exception as e:
    print("Error loading file ... exiting:", e)
    exit()