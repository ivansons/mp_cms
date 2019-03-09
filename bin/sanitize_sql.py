"""
Sanitize piped SQL, and print it out again!

Currently only reads from stdin.  Input is expected to be SQL expressions
like those dumped by pg_dump.

Usage example:
    pg_dump | python sanitize_sql.py > db.sql
"""

import re
import sys

field_regex = re.compile('^\s*`([^`]+)')


class SanitizerException(BaseException):
    pass


class Sanitizer(object):
    """
    Base class for other Sanitizers

    Sanitizers should at define two things:
        - table: The table name this sanitizer should work on
        - sanitize_row: A method that changes the necessary fields in the row

    External API:
        - sanitizer.process_line(line) returns sanitized SQL

    Input assumptions:
        - CREATE TABLE comes before any INSERT INTO
        - CREATE TABLE and INSERT INTO are at the very beginning
          of their own lines
        - Field definitions in a CREATE TABLE are each on their own line
    """
    table = None

    def __init__(self):
        self.fields = []
        self.done = False
        self.processing = False

        if self.table is None:
            raise SanitizerException('table not defined on Sanitizer')

    def can_start_processing(self, line):
        phrase = 'CREATE TABLE `{}`'.format(self.table)
        return line.startswith(phrase)

    def process_line(self, line):
        if not self.processing and self.can_start_processing(line):
            self.processing = True

        if not self.processing:
            return line

        if line.startswith('INSERT INTO'):
            self.done = True
            self.processing = False
            return self.process_insert_into(line)

        self.store_field_definition(line)
        return line

    def process_insert_into(self, line):
        sanitized_tuples = []
        in_tuple = False
        in_string = False
        row = []
        buffer = ''

        for i, char in enumerate(line):
            if not in_tuple:
                if char == '(':
                    in_tuple = True
                continue

            if char in (',', ')') and not in_string:
                row.append(buffer)
                buffer = ''
                if char == ')':
                    sanitized_tuples.append(self.process_tuple_items(row))
                    row = []
                    in_tuple = False
                continue

            if char == "'":
                if not in_string:
                    in_string = True
                elif in_string and not line[i-1] == '\\':
                    in_string = False

            buffer += char

        return 'INSERT INTO `{}` VALUES {};'.format(self.table,
                                                    ','.join(sanitized_tuples))

    def process_tuple_items(self, row):
        row_dict = {field: row[i] for i, field in enumerate(self.fields)}
        self.sanitize_row(row_dict)
        for i, field in enumerate(self.fields):
            row[i] = row_dict[field]
        return '(' + ",".join(row) + ')'

    def sanitize_row(self, row):
        raise NotImplementedError

    def store_field_definition(self, line):
        match = field_regex.search(line)
        if match is not None:
            self.fields.append(match.group(1))


def main():
    sanitizers = (
    )

    for line in sys.stdin:
        for sanitizer in sanitizers:
            line = sanitizer.process_line(line)
        print line,

    for sanitizer in sanitizers:
        if not sanitizer.done:
            raise SanitizerException('Sanitizer {} '
                                     'was not used!'.format(sanitizer))

if __name__ == '__main__':
    main()
