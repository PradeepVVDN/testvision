import os
import time
p_dir=os.getcwd()
os.system('[ -f $PWD/result ] && rm -rf result || echo "Fetching Result..."')
time.sleep(5)
#os.system('adb pull /data/__BashShellScripts__/result $PWD') // remove comment after connection enable file transfer 
os.system('chmod 777 result')
time.sleep(10) 
os.system("clear")
os.system("tput setaf 3")
print("...")
print("...")
print("...")
os.system("tput setaf 3")
print(".............Result copied successfully.............")
print("...")
print("...")
print("...")
time.sleep(10)
os.system("robot generate_result.robot")
time.sleep(10)
print("...")
print("...")
print("...")
os.system("tput setaf 3")
print(".............Result generated successfully...........")
print("...")
print("...")
print("...")
time.sleep(3)
os.system("python send_result_mail_.py")
print("...")
print("...")
print("...")
os.system("tput setaf 3")
print(".............Result sent to your email...............")
exit(0)
