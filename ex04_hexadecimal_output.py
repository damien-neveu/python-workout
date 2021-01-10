def hex_output(hex_num: str) -> int:
    reversed_hex_num = reversed(hex_num)
    res = 0
    for power, digit in enumerate(reversed_hex_num):
        res += int(digit, 16) * 16**power
    return res


print(f"hex_output(50)={hex_output('50')}, hex_output(1234567)={hex_output('1234567')},"
      f"hex_output(3A67F3E)={hex_output('3A67F3E')}")

