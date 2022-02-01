from translate import Translator

# https://pypi.org/project/translate/
# pip3 install translate
# en, ja, ko, pt, zh
translator = Translator(to_lang="es")

try:
    with open("me.txt", mode="r") as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open("me-es.txt", mode="w") as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print("Check your file path")
