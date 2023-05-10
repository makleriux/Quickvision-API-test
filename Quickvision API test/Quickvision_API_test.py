# API call test for Quickvision
import subprocess # lets execute programs
import winreg as wrg #find Quicvision location for API 
import time # Giggless
  
# Store location of HKEY_CURRENT_USER
location = wrg.HKEY_LOCAL_MACHINE\
  
# Storing path within HKEY
soft = wrg.OpenKeyEx(location,r"SOFTWARE\\WOW6432Node\\Owandy\\QuickVision\\")
  
#for long therm testing consider to use TRY as QV is 32bit and on ^$bit machines 6432 node is added to the reg path
# try would find correct path or prompt QV is not installed/reg pointers not found :)

#finding path for API
adresas = wrg.QueryValueEx(soft,"MjExec") #tulip 0 is address
  
# Closing folder
if soft:
    wrg.CloseKey(soft)
  
# Printing values
hm = "QuickVision instalation location is: "
print(hm + adresas[0])
print("Opening QuickVision in 5 seconds")
time.sleep(5)

# CMD Call (/P:DATA entries seperated by comma) ID,Name,Surname,Post_code,DOB,,,,,,
subprocess.run([adresas[0], "/P:25,Simas,Simanavicius,48XDE45,25-06-1970,1,,,,,,"])
