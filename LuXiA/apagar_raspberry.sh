#!/bin/bash
echo "Desmontando USB..."
sudo umount /srv/usb
echo "Apagando el sistema..."
sudo shutdown -h now
