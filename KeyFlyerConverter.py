import os
import time
# Mapping all languages
us_to_ua = {
    '`': 'ґ', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '0': '0',
    '-': '-', '=': '=', 'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ',
    'p': 'з',
    '[': 'х', ']': 'ї', 'a': 'ф', 's': 'і', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д',
    ';': 'ж',
    "'": 'є', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '/': '.'
}

us_to_ru = {
    '`': 'ё', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '0': '0',
    '-': '-', '=': '=', 'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ',
    'p': 'з',
    '[': 'х', ']': 'ъ', 'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д',
    ';': 'ж',
    "'": 'э', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '/': '.'
}

us_to_dk = {
    '`': '½', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '0': '0',
    '-': '+', '=': '´', 'q': 'q', 'w': 'w', 'e': 'e', 'r': 'r', 't': 't', 'y': 'y', 'u': 'u', 'i': 'i', 'o': 'o',
    'p': 'p',
    '[': 'å', ']': '^', 'a': 'a', 's': 's', 'd': 'd', 'f': 'f', 'g': 'g', 'h': 'h', 'j': 'j', 'k': 'k', 'l': 'l',
    ';': 'æ',
    "'": 'ø', 'z': 'z', 'x': 'x', 'c': 'c', 'v': 'v', 'b': 'b', 'n': 'n', 'm': 'm', ',': ',', '.': '.', '/': '-'
}

ua_to_us = {v: k for k, v in us_to_ua.items()}
ru_to_us = {v: k for k, v in us_to_ru.items()}
dk_to_us = {v: k for k, v in us_to_dk.items()}


# Function choose
def get_mapping(src_lang, dest_lang):
    mappings = {
        'us': {'ua': us_to_ua, 'ru': us_to_ru, 'dk': us_to_dk},
        'ua': {'us': ua_to_us, 'ru': {v: ru_to_us[k] for k, v in us_to_ua.items() if k in ru_to_us},
               'dk': {v: dk_to_us[k] for k, v in us_to_ua.items() if k in dk_to_us}},
        'ru': {'us': ru_to_us, 'ua': {v: ua_to_us[k] for k, v in us_to_ru.items() if k in ua_to_us},
               'dk': {v: dk_to_us[k] for k, v in us_to_ru.items() if k in dk_to_us}},
        'dk': {'us': dk_to_us, 'ua': {v: ua_to_us[k] for k, v in us_to_dk.items() if k in ua_to_us},
               'ru': {v: ru_to_us[k] for k, v in us_to_dk.items() if k in ru_to_us}}
    }
    return mappings[src_lang][dest_lang]


# For translate
def translate_log(input_file, output_file, src_lang, dest_lang):
    mapping = get_mapping(src_lang, dest_lang)

    with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            translated_line = ''
            i = 0
            while i < len(line):
                if line[i] == '[':
                    # знайти закінчення спеціальної клавіші
                    end_idx = line.find(']', i)
                    if end_idx != -1:
                        translated_line += line[i:end_idx + 1]
                        i = end_idx
                    else:
                        translated_line += line[i]
                else:
                    if line[i] in mapping:
                        translated_line += mapping[line[i]]
                    else:
                        translated_line += line[i]
                i += 1
            f_out.write(translated_line)


# Interactive choosing
def main():
    print("Keyboard")
    image = [
    "     ___________/                                ",
    "    |          | |     Transferring              ",
    "    |          | |        one keyboard           ",
    "    |  TRANS   | |          layout to            ",
    "    |   LATOR  | |             another           ",
    "    |          | /               (KeyFlyer)      ",
    "    |__________|/                                ",
    ]
    for line in image:
        print(line)
        time.sleep(0.2)

    print(" ")
    print("The script will replace the desired keyboard after the keylogger")
    print("---------------------------- ")
    print(" ")
    input_file = input("Enter path to .txt file: ").strip()

    if not os.path.isfile(input_file):
        print(f"File {input_file} not found.")
        return

    output_file = input("Enter path to save new translated file: ").strip()

    if os.path.isfile(output_file):
        print(f"File {output_file} already exists. Remove or rename it before continuing.")
        return

    print("Select the original language:")
    print("1. English (us)")
    print("2. Ukrainian (ua)")
    print("3. Russian (ru)")
    print("4. Dansk (dk)")

    src_lang = input("Select number for the original language: ").strip()
    src_lang_map = {'1': 'us', '2': 'ua', '3': 'ru', '4': 'dk'}
    src_lang = src_lang_map.get(src_lang, 'us')

    print("Select the target language:")
    print("1. English (us)")
    print("2. Ukrainian (ua)")
    print("3. Russian (ru)")
    print("4. Dansk (dk)")

    dest_lang = input("Select number for the target language: ").strip()
    dest_lang_map = {'1': 'us', '2': 'ua', '3': 'ru', '4': 'dk'}
    dest_lang = dest_lang_map.get(dest_lang, 'ua')

    translate_log(input_file, output_file, src_lang, dest_lang)
    print(f'The log file has been successfully translated and saved to {output_file}')


if __name__ == '__main__':
    main()