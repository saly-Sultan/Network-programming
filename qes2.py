def binary_to_decimal(binary):
    try:
        if not all(char in ('0', '1') for char in binary):
            raise ValueError("Invalid binary string. Only '0' and '1' characters allowed.")
        decimal_value = int(binary, 2)
        return decimal_value
    except ValueError as err:
        print("Error: {}".format(err))
        return None

binary_number = input("Enter a binary number: ")
decimal_equivalent = binary_to_decimal(binary_number)

if decimal_equivalent is not None:
    print("The decimal equivalent of {} is {}".format(binary_number, decimal_equivalent))
