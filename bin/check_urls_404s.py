"""
Check a list of URLs from an input file for 404 errors.

Requirements:
  - python requests package with security setup
    - "pip install requests[security]"
  - input text file can have commented out lines beginning with '#'

Usage example:
    python check_urls_404s.py url_list.txt

Notes:
  - a report file will be created called 'check_urls_report_YYYY-MM-DD_HH-MM.txt'
"""

# Python imports
from collections import defaultdict
import datetime
import sys

# Third party imports
import requests

# Constants
MAJOR_HTTP_RESPONSE_ERRORS = [400, 404, 500, 502, 504]
HTTP_RESPONSE_CATEGORIES = ['1xx information responses',
    '2xx success responses', '3xx redirection responses',
    '4xx client error responses', '5xx server error responses',
    'unknown responses', 'request exceptions']

lines = (line.rstrip('\n') for line in open(sys.argv[1]))

# default dictionary for responses
url_responses = defaultdict(list)
most_recent_comment = ''
count = 0

# Initialize min and max status codes
min_status_code = 500
max_status_code = 200

# Loop over lines from input urls file
for line in lines:
    line.strip()

    if line[0] == '#':
        most_recent_comment = line

    else:
        print("Trying: {}, {}".format(line, most_recent_comment))
        count += 1
        try:
            response = requests.get(line, timeout=15)
            status_code = response.status_code
            min_status_code = min(min_status_code, status_code)
            max_status_code = max(max_status_code, status_code)

            # Print a message to console for 404, 400, 500, 502, 504
            if status_code in MAJOR_HTTP_RESPONSE_ERRORS:
                print('--- ERROR!! {} HTTP response: {}'.format(status_code,
                                                                line))

            # Store response in status_code bucket
            url_responses[status_code].append(
                '{}, {}'.format(line, most_recent_comment))

            # -- Store response into 1st digit http response bucket -- #

            # Information response
            if 200 > status_code >= 100:
                url_responses['1xx information responses'].append(
                    '{}, {}'.format(line, most_recent_comment))

            # Success response
            elif 300 > status_code >= 200:
                url_responses['2xx success responses'].append(
                    '{}, {}'.format(line, most_recent_comment))

            # Redirection response
            elif 400 > status_code >= 300:
                url_responses['3xx redirection responses'].append(
                    '{}, {}'.format(line, most_recent_comment))

            # Client error repsonse
            elif 500 > status_code >= 400:
                url_responses['4xx client error responses'].append(
                    '{}, {}'.format(line, most_recent_comment))

            # Server error response:
            elif 600 > status_code >= 500:
                url_responses['5xx server error responses'].append(
                    '{}, {}'.format(line, most_recent_comment))

            # Unknown response:
            else:
                url_responses['unknown responses'].append(
                    '{}, {}'.format(line, most_recent_comment))

        # Handle Python Requests exception
        except requests.exceptions.RequestException as e:
            print('--- ERROR!! Request exception: {}, {}, {}'.format(
                e, line, most_recent_comment))

            # Store request exceptions
            url_responses['request exceptions'].append(
                '{}, {}'.format(line, most_recent_comment))

# Create report file
output_file = 'check_urls_report_{}.txt'.format(
    datetime.datetime.now().strftime('%Y-%m-%d_%H-%M'))

with open(output_file, 'w') as target_file:
    target_file.write('### --- Check URLs Report --- ###\n\n')
    target_file.write('# Input file: {}\n'.format(sys.argv[1]))
    target_file.write('# Total attempted URLs: {}\n'.format(count))

    # Write counts for response types
    for key in HTTP_RESPONSE_CATEGORIES:
        if url_responses[key]:
            target_file.write('# Total HTTP {}: {}'.format(
                key, len(url_responses[key])))

            target_file.write('\n')

    # List out HTTP response error URLs
    for key in MAJOR_HTTP_RESPONSE_ERRORS:
        if url_responses[key]:
            target_file.write('\n# -- POTENTIAL ERROR {} HTTP responses -- '
                              '#\n'.format(key))

            for url in url_responses[key]:
                target_file.write('{}\n'.format(url))

    # List out request exceptions
    if url_responses[HTTP_RESPONSE_CATEGORIES[-1]]:
        target_file.write('\n# -- Python {} HTTP non-responses -- #\n'.format(
            HTTP_RESPONSE_CATEGORIES[-1]))

        for url in url_responses[HTTP_RESPONSE_CATEGORIES[-1]]:
            target_file.write('{}\n'.format(url))

    # List out other HTTP response URLs
    for key in xrange(min_status_code, max_status_code + 1):
        if key not in MAJOR_HTTP_RESPONSE_ERRORS and url_responses[key]:
            target_file.write('\n# -- {} HTTP responses -- #\n'.format(key))
            for url in url_responses[key]:
                target_file.write('{}\n'.format(url))

    target_file.write('\n### --- End Report --- ###')

print('Total attempted URLs: {}'.format(count))
error_count = len(url_responses['4xx client error responses']) + \
              len(url_responses['5xx server error responses']) + \
              len(url_responses['unknown responses']) + \
              len(url_responses['request exceptions'])

print('Total number of potential errors: {}'.format(error_count))
print('Full report at: {}'.format(output_file))
