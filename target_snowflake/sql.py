import re

from target_snowflake.exceptions import SQLError


IDENTIFIER_FIELD_LENGTH = 256


def valid_identifier(x):
    """
    https://docs.snowflake.net/manuals/sql-reference/identifiers-syntax.html
    """
    if not x:
        raise SQLError('Identifier must be non empty.')

    if not isinstance(x, str):
        raise SQLError('Identifier must be a string. Got {}'.format(type(x)))

    if IDENTIFIER_FIELD_LENGTH < len(x):
        raise SQLError('Length of identifier must be less than or equal to {}. Got {} for `{}`'.format(
            IDENTIFIER_FIELD_LENGTH,
            len(x),
            x))

    return True


def identifier(x):
    valid_identifier(x)
    return '"{}"'.format(x)
