# Introduction
This is telegram bot for posting jpg images from webcam with motion detection
to telegram

## Files and folders
hosts - inventory for ansible
deploy-to-ftp-serve.yaml - playbook for ansible, tested on Arch linux
scripts/webcarestart - "OCam M3" webcam restart script
keys/ - folder with ssh keys for cctv user, have to created
configs/vsftpd.conf - vsftpd daemon configs
telegram-bot/watchdog-ftp.py - telegram bot
telegram-bot/watchdog-ftp.service - unit file for systemd
automagic/ - flow examples for Automagic Automation on Android


## Preparation
1. Generate ssh keys in keys folder by `ssh-keygen -f cctv_key` command
2. Create host record in /etc/hosts for ftp-server
3. Create new bot as described in https://core.telegram.org/bots#6-botfather
4. Add chat id and token to telegram-bot/watchdog-ftp.py
(`TOKEN=` and `CHAT_ID` variables)
