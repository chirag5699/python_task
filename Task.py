import platform
import os
import socket
import psutil
import speedtest
import screeninfo
import wmi

def get_installed_software():
    software_list = []
    for i in psutil.process_iter(['pid', 'name']):
        software_list.append(i.info['name'])
    return software_list
installed_software = get_installed_software()
print("1. Installed Software List:", installed_software)

def get_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1000000  # in Mbps
    upload_speed = st.upload() / 1000000  # in Mbps
    return download_speed, upload_speed
internet_speed = get_internet_speed()
print("2. Internet Speed (Download, Upload):", internet_speed)


def get_screen_resolution():
    screen_info = screeninfo.get_monitors()
    resolutions = [(monitor.width, monitor.height) for monitor in screen_info]
    return resolutions
screen_resolution = get_screen_resolution()
print("3. Screen Resolution:", screen_resolution)



def get_cpu_info():
    cpu_info = platform.processor()
    cores = psutil.cpu_count(logical=False)
    threads = psutil.cpu_count(logical=True)
    return cpu_info, cores, threads
cpu_info, cores, threads = get_cpu_info()
print("4. CPU Model:", cpu_info)
print("5. Number of Cores and Threads:", cores, threads)

def get_gpu_info():
    try:
        w = wmi.WMI()
        gpu_info = w.Win32_VideoController()[0].Caption
    except Exception as e:
        gpu_info = None
    return gpu_info
gpu_info = get_gpu_info()
print("6. GPU Model:", gpu_info)


def get_ram_size():
    ram_info = psutil.virtual_memory()
    ram_size_gb = ram_info.total / (1024 ** 3)  # Convert to GB
    return ram_size_gb
ram_size = get_ram_size()
print("7. RAM Size (in GB):", ram_size)


def get_screen_size():
    screen_info = screeninfo.get_monitors()[0]
    screen_size = (screen_info.width, screen_info.height)
    return screen_size
screen_size = get_screen_size()
print("8. Screen Size:", screen_size)

def get_network_info():
    wifi_mac = None
    ethernet_mac = None
    for name, addr_list in psutil.net_if_addrs().items():
        for addr in addr_list:
            if '00:00:00:00' not in addr.address:
                if name.lower().startswith('wlan'):
                    wifi_mac = addr.address
                elif name.lower().startswith('eth'):
                    ethernet_mac = addr.address
    return wifi_mac, ethernet_mac
wifi_mac, ethernet_mac = get_network_info()
print("9. WiFi MAC Address:", wifi_mac)
print("10. Ethernet MAC Address:", ethernet_mac)

def get_public_ip():
    try:
        public_ip = socket.gethostbyname(socket.gethostname())
    except socket.gaierror:
        public_ip = None
    return public_ip
public_ip = get_public_ip()
print("11. Public IP Address:", public_ip)


def get_windows_version():
    windows_version = platform.version()
    return windows_version
windows_version = get_windows_version()
print("12. Windows Version:", windows_version)








