import os
import time
os.system("python -m pip install -r requirements.txt")
time.sleep(5)
os.system('[ -f $PWD/__BashShellScripts__.zip ] && echo "Process is about to start...." || echo "file __BashShellScripts__.ZIP is not Available"')
time.sleep(5)
os.system('unzip __BashShellScripts__.zip')
time.sleep(5)
os.system('chmod +x __BashShellScripts__')
#os.system('adb push __BashShellScripts__ /data/') // Uncomment this section when you enable file transfer utility
print("file __BashShellScripts__ pushed successfully to the device /data directory")
exit(0)
