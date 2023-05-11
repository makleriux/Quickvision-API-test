# API call test for Quickvision
import subprocess # lets execute programs
import winreg as wrg #find Quicvision location for API 
import time # Giggless
import sys 

os_max_bit = sys.maxsize > 2**32 # check if its x64 or x32

if os_max_bit is True:
    addr = "SOFTWARE\\WOW6432Node\\Owandy\\QuickVision\\" 
    ostyp = "x64"
    
else: 
    ostyp = "x32"
    addr = "SOFTWARE\\Owandy\\QuickVision\\"
    
# Store location of HKEY_CURRENT_USER
location = wrg.HKEY_LOCAL_MACHINE\
  
# Storing path within HKEY
soft = wrg.OpenKeyEx(location,r""+addr)

#finding path for API
adresas = wrg.QueryValueEx(soft,"MjExec") #tulip 0 is address
  
# Closing folder
if soft:
    wrg.CloseKey(soft)
  
# Printing values
print("OS type is: " + ostyp)
print("Registry pointers for API location: ",r""+addr)
hm = "QuickVision instalation location is: "
print(hm + adresas[0])
print("Opening QuickVision in 5 seconds")
time.sleep(5)

# CMD Call (/P:DATA entries seperated by comma) ID,Name,Surname,Post_code,DOB,,,,,,
subprocess.run([adresas[0], "/P:25,Simas,Simanavicius,48XDE45,25-06-1970,1,,,,,,"])
