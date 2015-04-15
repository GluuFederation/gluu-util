#!/usr/bin/python
import sys, os, time

STATE_OK=0
STATE_WARNING=1
STATE_UNKNOWN=3
STATE_CRITICAL=2
EXIT_MSG=""

check_command='echo | openssl s_client -connect %s:443 2>/dev/null | openssl x509 -noout -dates|grep -i notafter' % sys.argv[1]
str_out = os.popen("%s" %check_command).read().strip()
t = str_out.split('=')[-1]
time_tup = time.strptime(t, '%b %d %H:%M:%S %Y %Z')
expiration_in_seconds = time.mktime(time_tup)
days_until_expiration = int((expiration_in_seconds - time.time()) / (60*60*24))
print '%s' %days_until_expiration
