import subprocess 
import sys 

def list_containers_ids():
    print("Current running containers")
    try :
        sudo_password = '1'
        cmd = ["sudo", "-S", "cat", "/var/lib/docker/containers/192946f57a48861c43175c4aaed38c771f82e99ed72e5d4cef926cd680c38036/config.v2.json"]
        p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        sudo_prompt = p.communicate(sudo_password + '\n')[1]
    except OSError as err :
        print("Error {}".format(err))
        sys.exit(2) 
    except Exception as e: 
        print(e)
