#!/bin/bash
python /home/ec2-user/oncall_dashboard/calculate_oncall_completion.py > last_percentage

lineNo=8
var=$(cat last_percentage)

sed -i "${lineNo}s/.*/$var/" /var/www/html/on-call.html




