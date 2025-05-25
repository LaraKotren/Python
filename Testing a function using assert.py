def test_average_num():
    # Тест с целыми числами
    assert average_num([1, 1]) == 1
    assert average_num([10, 20, 30]) == 20
    
    # Тест с числами с плавающей точкой
    assert average_num([2.5, 3.5]) == 3
    assert average_num([1.1, 2.2, 3.3]) == 2.2
    
    # Тест со смешанными типами (int и float)
    assert average_num([1, 2.5, 3, 4.5]) == 2.75
    
    # Тест с числами в виде строк
    assert average_num(["5", "5"]) == 5
    assert average_num(["10.5", "20.5"]) == 15.5
    
    # Тест с некорректными данными (должен вернуть "Bad request")
    assert average_num(["abc", 1]) == "Bad request"
    
    # Тест с пустым списком (вызовет ZeroDivisionError, но assert проверит, что это исключение возникает)
    try:
        average_num([])
        assert False, "Expected an error when list is empty"
    except ZeroDivisionError:
        assert True