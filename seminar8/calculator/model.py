# Модуль для выполнения опреаций

from sympy import *

def execute_expr(expr: str) -> str:         # (5+3)*10 -> 80
    """"Принимает на вход строку-пример.
    Возвращает результат примера."""
    expr = eval(expr)
    return(expr)


def solve_eq(expr: str) -> str:                    # x**3 - 8 = 0 -> "2"  # x**2 - 1 = 0 -> "1,-1"
    """Принимает на вход уравнение в виде строки.
    Возвращает список корней уравнения в строку с разделителем"""
    x = symbols('x')
    expr = solve(Eq(eval(expr), 0), x)
    return(expr)


def simpify_pol(expr: str) -> str:           # x**2 + 3*x**2 + 4 -> 4*x**2 + 4
    """"Упрощает введенный многочлен"""
    x = symbols('x')
    expr = simplify(Poly(eval(expr)), x)
    return(expr)
