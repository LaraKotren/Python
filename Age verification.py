try:
    age_input = input("������� ��� �������: ")
    age = int(age_input)
    
    if age >= 0:
        if age >= 18:
            print("�� ����������������.")
        else:
            print("�� ������������������.")
    else:
        print("������: ������� �� ����� ���� �������������!")
except ValueError:
    print("������: ������� �� �����!")