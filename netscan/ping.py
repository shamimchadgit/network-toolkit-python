import platform
import subprocess

def ping_host(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    
    command = ['ping', param, '4', host]
    try:
        output = subprocess.check_output(command, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"⚠️ Ping Failed: {e}"
