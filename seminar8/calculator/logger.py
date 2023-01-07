# Модуль для записи резуьтатов вычислений
from os import chdir
chdir(r'C:\Users\Мария\OneDrive\Рабочий стол\Учеба\2 четверть\1. Знакомство с Python\Семинары и домашка\Python\seminar8\calculator')

def log_exec(expr: str, result: str):
    """Записывает в файл результат вычислений
    в виде |задача -> ответ|"""
    with open('base.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{expr} -> {result}')
        f.close()

def get_history() -> str:
    """"Возвращает содержимое файла с результатами вычислений"""
    with open('base.txt', 'r', encoding='utf-8') as f:
        history = f.read()
        f.close()
        return history
