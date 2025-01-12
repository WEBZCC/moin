# Copyright: 2004 MoinMoin:ThomasWaldmann
# License: GNU GPL v2 (or any later version), see LICENSE.txt for details.

"""
    Build moin.constants.chartypes with
    UCS-2 character types (upper/lower/digits/spaces).
"""


def main():
    uppercase = []
    lowercase = []
    digits = []
    space = []
    for code in range(1, 65535):
        c = chr(code)
        str = "\\u{0:04x}".format(code)
        if c.isupper():
            uppercase.append(str)
        elif c.islower():
            lowercase.append(str)
        elif c.isdigit():
            digits.append(str)
        elif c.isspace():
            space.append(str)

    chars_upper = ''.join(uppercase)
    chars_lower = ''.join(lowercase + digits)
    chars_digits = ''.join(digits)
    chars_spaces = ''.join(space)

    print("""
CHARS_UPPER = "%(chars_upper)s"

CHARS_LOWER = "%(chars_lower)s"

CHARS_DIGITS = "%(chars_digits)s"

CHARS_SPACES = "%(chars_spaces)s"


""" % locals())


if __name__ == '__main__':
    main()
