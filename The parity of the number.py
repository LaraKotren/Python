def check_even_odd():
    user_input = input("������� �����: ")
    
    try:
        number = int(user_input)
    except ValueError:
        print("������: ������� �� �����")
        return
    
    if number < 0:
        print("������: ������� ������������� �����")
        return
    
    if number % 2 == 0:
        print(f"����� {number} �������� ������")
    else:
        print(f"����� {number} �� �������� ������")

check_even_odd()