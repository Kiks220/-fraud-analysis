#!/usr/bin/env python3
"""
log_parser.py — простой парсер логов для поиска подозрительных IP.

Использование:
    python log_parser.py access.log

Скрипт ищет строки с неудачными попытками входа (401, 403)
и выводит список уникальных IP-адресов.
"""

import re
import sys
from collections import Counter

def parse_log(filepath):
    # Регулярное выражение для поиска IP и кода ответа
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?\s(\d{3})\s')
    
    suspicious = Counter()
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            match = pattern.search(line)
            if match:
                ip = match.group(1)
                status = match.group(2)
                # Ищем ошибки доступа
                if status in ('401', '403', '404'):
                    suspicious[ip] += 1
    
    return suspicious

def main():
    if len(sys.argv) != 2:
        print("Использование: python log_parser.py <файл_лога>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    results = parse_log(filepath)
    
    print(f"\nНайдено {len(results)} подозрительных IP:\n")
    for ip, count in results.most_common(10):
        print(f"  {ip} — {count} попыток")

if __name__ == "__main__":
    main()
