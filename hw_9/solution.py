import os

def copy_nonempty_lines(source_path: str, target_path: str) -> int:
    if not os.path.exists(source_path):
        print(f"Ошибка: Исходный файл не найден по пути: {os.path.abspath(source_path)}")
        return 0
    lines_written = 0 

    with (open(source_path, 'r', encoding='utf-8') as infile, \
         open(target_path, 'w', encoding='utf-8') as outfile):
    
        for line in infile:
            # Удаляем пробельные символы в начале и конце строки
            stripped_line = line.strip()

            # Если строка не пустая, записываем её в новый файл
            if stripped_line:
                outfile.write(stripped_line + '\n')
                lines_written += 1
        print(f"Готово! Результаты записаны в файл {target_path}")
    
# print(f"Файл успешно создан по адресу: {os.path.abspath(target_path)}")
    return lines_written

with open('some_text_file.txt', 'r', encoding='utf-8') as file:
    print('Учащиеся с оценкой меньше 3 баллов:')
    for line in file:
        # Разбиваем строку на части (фамилия, имя, оценка)
        parts = line.split()
        if len(parts) >= 3:
            surname, name, score = parts[0], parts[1], int(parts[2])
            # Выводим ученика, если его оценка меньше 3
            if score < 3:
                print(f'{surname} {name} — {score} балла')

from collections import Counter
import re

input_filename = 'some_text_file2.txt'
output_filename = 'output.txt'

try:
    with open(input_filename, 'r', encoding='utf-8') as infile, \
         open(output_filename, 'w', encoding='utf-8') as outfile:
        
        for line in infile:
            # Приводим к нижнему регистру и находим все слова (игнорируем знаки препинания)
            words = re.findall(r'\b\w+\b', line.lower())
            
            if not words:
                # Если строка пустая или в ней нет слов
                outfile.write('\n')
                continue
            
            # Подсчитываем частоту слов в текущей строке
            counts = Counter(words)
            
            # Находим максимальное количество повторений
            max_count = max(counts.values())
            
            # Выбираем все слова, которые встречаются максимальное число раз,
            most_common_words = sorted([word for word, count in counts.items() if count == max_count])
            
            best_word = most_common_words[0]
            
            # Записываем результат для строки в новый файл
            outfile.write(f"{best_word} {max_count}\n")
            
    print(f"Готово! Результаты записаны в файл {output_filename}")

except FileNotFoundError:
    print(f"Ошибка: Файл {input_filename} не найден.")

