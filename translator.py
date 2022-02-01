from translate import Translator

# en, ja, ko, pt, zh
translator = Translator(to_lang="ja")

try:
    with open("me.txt", mode="r") as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open("me-ja.txt", mode="w") as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print("Check your file path")
