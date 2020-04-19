#!/usr/bin/env python3

import re
import operator
import csv
import sys

file = sys.argv[1]
error = {}
info = {}

with open(file, "r") as logs:
    for log in logs:
        r_brac_open = log.find('(')
        r_brac_close = log.find(')')
        s_brac_open = log.find('[')
        user = log[r_brac_open+1: r_brac_close]
        if user not in info:
            info[user] = {"info": 0, "error": 0}
        if log[36] == "E":
            status = log[36: 41]
            msg = log[42: r_brac_open]
            if msg not in error:
                error[msg] = 0
            error[msg] += 1
        else:
            status = log[36: 40]
            msg = log[41: s_brac_open]
        info[user][status.lower()] += 1
    logs.close()

error_sorted = sorted(error.items(), key = operator.itemgetter(1), reverse=True)
info_sorted = sorted(info.items(), key=operator.itemgetter(0))

with open('Error_Message.csv', 'w') as file:
    fieldnames = ["Error", "Count"]
    writer = csv.DictWriter(file, fieldnames = fieldnames)
    writer.writeheader()
    for err in error_sorted:
        writer.writerow({'Error': err[0], 'Count': err[1]})
    file.close()

with open('User_Statistics.csv', 'w') as file:
    fieldnames = ["Username", "INFO", "ERROR"]
    writer = csv.DictWriter(file, fieldnames = fieldnames)
    writer.writeheader()
    for name in info_sorted:
        writer.writerow({'Username': name[0], 'INFO': name[1]['info'], 'ERROR': name[1]['error']})
    file.close()
