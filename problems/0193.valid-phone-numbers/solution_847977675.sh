# 0193 - Valid Phone Numbers
# Date: 2022-11-22
# Runtime: 88 ms, Memory: 3.2 MB
# Submission Id: 847977675


# Read from the file file.txt and output all valid phone numbers to stdout.
# basic regex (BRE)
# grep "^\(([0-9]\{3\}) \|[0-9]\{3\}-\)[0-9]\{3\}-[0-9]\{4\}$" file.txt

# extended regex (ERE)
grep -E "^(\([0-9]{3}\) |^[0-9]{3}-)[0-9]{3}-[0-9]{4}$"      file.txt

# perl-compatible regex (PCRE)
# grep -P "^(\(\d{3}\) |\d{3}-)\d{3}-\d{4}$"                   file.txt
