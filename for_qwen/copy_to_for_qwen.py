# Для запуска: python copy_to_for_qwen.py
import os
import shutil
from datetime import datetime

def collect_content_to_for_qwen():
    # Текущая папка (где лежит скрипт)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Папка for_qwen
    for_qwen_dir = current_dir
    # Родительская папка (uteka/)
    parent_dir = os.path.dirname(for_qwen_dir)
    # Выходной файл
    output_file = os.path.join(current_dir, 'content.txt')

    # Создаём папку (на всякий случай)
    os.makedirs(current_dir, exist_ok=True)

    # Резервная копия старого content.txt
    if os.path.exists(output_file):
        mod_time = os.path.getmtime(output_file)
        mod_dt = datetime.fromtimestamp(mod_time)
        timestamp = mod_dt.strftime("%Y_%m_%d_%H_%M_%S")
        backup_name = os.path.join(current_dir, f"content_{timestamp}.txt")
        shutil.move(output_file, backup_name)
        print(f"Старый файл переименован: content.txt → content_{timestamp}.txt")

    # Открываем новый файл для записи
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Рекурсивный обход всех подпапок в parent_dir (uteka/)
        for root, dirs, files in os.walk(parent_dir):
            # Фильтруем папки: удаляем те, что начинаются с точки или это сама папка for_qwen
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'for_qwen']

            # Пропускаем обработку, если root — это папка for_qwen
            if os.path.abspath(root) == os.path.abspath(for_qwen_dir):
                continue

            for file in files:
                # Пропускаем файлы, начинающиеся с точки
                if file.startswith('.'):
                    continue

                file_path = os.path.join(root, file)

                # Формируем относительный путь
                rel_path = os.path.relpath(file_path, parent_dir)

                header = f"Содержимое файла {rel_path}:"
                outfile.write(header + '\n')
                outfile.write('-' * 50 + '\n')

                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        outfile.write(content + '\n\n')
                except UnicodeDecodeError:
                    error_msg = f"[Файл {rel_path} не является текстовым. Пропущен.]\n\n"
                    outfile.write(error_msg)
                except Exception as e:
                    error_msg = f"[Ошибка при чтении {rel_path}: {str(e)}]\n\n"
                    outfile.write(error_msg)

    print(f"Готово! Все содержимое записано в {output_file}")

if __name__ == "__main__":
    collect_content_to_for_qwen()