"""
RGB To Hex Conversion (5 kyu)

The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
"""

def rgb(r, g, b):
    result = ''
    for n in [r, g, b]:
        if n < 0:
            nn = hex(0)[2:]
        elif n > 255:
            nn = hex(255)[2:]
        else:
            nn = hex(n)[2:]
        result += nn.zfill(2).upper()
    return result