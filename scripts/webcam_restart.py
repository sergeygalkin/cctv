#!/usr/bin/python
import telnetlib

tn = telnetlib.Telnet('ftp-server-ip',23,30)
tn.read_until(b"RT-IPC login:")
tn.write(b"root\n")
tn.read_until(b"Password: ")
tn.write(b"cat1029\n")
tn.read_until(b"#")
tn.write(b"reboot\n")
tn.read_all().decode('ascii')
