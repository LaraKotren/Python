from typing import Any, List, Union, Dict


def function_name(
    search: str,
    status: bool,
    *args: Any,
    **kwargs: Any
) -> Union[List[int], str]:
    """
    Обрабатывает аргументы в зависимости от параметров search и status.
    
    Параметры:
        search: "args" - обработка позиционных аргументов, "kwargs" - обработка именованных
        status: Флаг, изменяющий поведение для режима "args"
        *args: Позиционные аргументы
        **kwargs: Именованные аргументы
    
    Возвращает:
        При search="args":
            - Если status=True: список целых чисел из args
            - Если status=False: строку из всех args
        При search="kwargs": строку с описанием всех ключей и значений
        В остальных случаях вызывает ValueError
    
    Исключения:
        ValueError: если search не "args" или "kwargs"
    """
    result: List[int] = []
    result_2: str = ""
    
    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += f"Key: {k}, Value: {v}; "
        return result_2
    else:
        raise ValueError("Error for search")