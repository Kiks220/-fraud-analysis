#!/usr/bin/env python3
"""
ip_checker.py — проверка IP-адреса через открытый API ipinfo.io.

Использование:
    python ip_checker.py 8.8.8.8

Скрипт выводит:
    - IP-адрес
    - Провайдера (ISP)
    - ASN (номер автономной системы)
    - Страну и город
    - Координаты (если есть)
"""

import sys
import json
import urllib.request
import urllib.error


def check_ip(ip: str) -> dict:
    """
    Запрашивает информацию об IP через ipinfo.io.

    :param ip: IP-адрес для проверки
    :return: словарь с данными
    """
    url = f"https://ipinfo.io/{ip}/json"

    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
            return data
    except urllib.error.HTTPError as e:
        print(f"[!] Ошибка HTTP: {e.code} — {e.reason}")
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"[!] Ошибка соединения: {e.reason}")
        sys.exit(1)
    except json.JSONDecodeError:
        print("[!] Не удалось разобрать ответ от API")
        sys.exit(1)


def print_info(data: dict) -> None:
    """Выводит информацию об IP в читаемом виде."""
    print("\n=== Информация об IP ===")
    print(f"IP:        {data.get('ip', 'N/A')}")
    print(f"Провайдер: {data.get('org', 'N/A')}")
    print(f"Страна:    {data.get('country', 'N/A')}")
    print(f"Регион:    {data.get('region', 'N/A')}")
    print(f"Город:     {data.get('city', 'N/A')}")
    print(f"Координаты:{data.get('loc', 'N/A')}")
    print(f"Часовой пояс: {data.get('timezone', 'N/A')}")
    print("========================\n")


def main():
    if len(sys.argv) != 2:
        print("Использование: python ip_checker.py <IP-адрес>")
        print("Пример:        python ip_checker.py 8.8.8.8")
        sys.exit(1)

    ip = sys.argv[1]
    data = check_ip(ip)
    print_info(data)


if __name__ == "__main__":
    main()
