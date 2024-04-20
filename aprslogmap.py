from paramiko import SSHClient
from scp import SCPClient
import folium


def copylog():
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect('pitnc.lan', username='tnc', password='1200baud')

    # SCPCLient takes a paramiko transport as an argument
    scp = SCPClient(ssh.get_transport())

    #scp.put('test.txt', 'test2.txt')
    scp.get('/home/tnc/aprs.log')

    scp.close()
    
    
m = folium.Map(location=(45.5236, -122.6750))
m.save("map.html")