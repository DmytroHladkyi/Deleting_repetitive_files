import os
import re

def remove_duplicates(directory):
    for root, dirs, files in os.walk(directory):
        filedict = {}
        for filename in files:
            filepath = os.path.join(root, filename)

            # Проверяет, повторяется ли файл 
            match = re.search(r'^(.*?)\((\d+)\)(\.[^.]*)?$', filename)
            if match:
                name = match.group(1)
                number = int(match.group(2))
                ext = match.group(3) or ''

                # Добавление файла в словарь с именем в качестве ключа и числом в качестве значения 
                if name not in filedict:
                    filedict[name] = [(number, filepath, ext)]
                else:
                    filedict[name].append((number, filepath, ext))

        # Переименование файлов в каждой группе 
        for name in filedict:
            files = filedict[name]
            files.sort(key=lambda x: x[0])
            print(files)
            latest = files[-1][1]
            ext = files[-1][2]

            for number, filepath, _ in files[:-1]:
                print(f"Deleted duplicate file: {filepath}")
                os.remove(filepath)

            os.rename(latest, os.path.join(root, f"{name}{ext}"))
            print(f"Renamed {latest} to {name}{ext}")

remove_duplicates(os.path.expanduser("~/Downloads"))