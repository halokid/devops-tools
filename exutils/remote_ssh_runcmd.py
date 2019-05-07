#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: r00x 


import paramiko


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("10.10.10.10", 22, "test", "test")
print ssh

# cmd = "ifconfig"
stdin,stdout,stderr = ssh.exec_command("ls /home")
print stdout.read()
