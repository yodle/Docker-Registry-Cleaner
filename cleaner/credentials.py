from zeke import commands

zk_host = commands.get_zk_hosts(None)
zk = commands.get_zk(zk_host[0])

def get_value_safely(val):
    try:
        return zk.get_value(val)
    except:
        return ""
    

username = get_value_safely('/credentials/yodle_docker_registry/username')
password = get_value_safely('/credentials/yodle_docker_registry/password')
