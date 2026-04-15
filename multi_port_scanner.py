import os # ? for opening the hostnames.txt file
from time import sleep
from socket import setdefaulttimeout, gethostbyname # ? for opening and closing the socket connections


# * VARIABLES
# tgt_ports = [80, 443, 8080] # edit only if you have specific ports that you wish to scan
hostnames_file_path = "./hostnames.txt"
default_timeout = float(0.001) # ? determines how long the socket connection will try to connect for until timing out.


# * OPENING HOSTNAMES.TXT
try: # open hostnames.txt and set to variable "hostnames"
    with open(hostnames_file_path, 'r') as file:
        hostnames = file.read().splitlines()
    print("[+] txt file 'hostnames.txt' found")

    # check if hostnames.txt is empty
    hostnames_empty = os.stat(hostnames_file_path).st_size == 0 # returns True or False
    if hostnames_empty: # == True
        print("'hostname.txt' is empty. Please enter desired hostnames, save the document, and then try again.")
        sleep(5)
        exit()
except:
    print("port_scanner couldn't find 'hostnames.txt'. Please make sure the .txt file is named as such and the variable 'hostnames_file_path' is correct, and then try again.")
    sleep(5)
    exit()


# * PORT SCAN FUNCTION
def port_scan(ip_addr, specified_ports=range(1, 10000)):
    """
    ## Description:
        Initiate Socket connection to 'ip_addr' on 'specified_ports'. For each port, port_scan prints if connection succeeds, or will 'Pass' if connection fails.

    ## Args:
        ip_addr (_string_): The single ip address that the function will scan.
        specified_ports (_integer_, optional): The port(s) the function will scan. Defaults to range(1, 10000).
    """

    for port in specified_ports:
        try:
            conn_skt = socket(AF_INET, SOCK_STREAM)
            conn_skt.connect((ip_addr, int(port)))
            print(f"    [!] Port {port} open!")
            conn_skt.close()
        except: # connection times out
            pass


# * HOSTNAME 'FOR' LOOP
    #? for each host name, get IP addr and attempt to connect to each port on that IP
if __name__ == "__main__":
    setdefaulttimeout(default_timeout)
    for hostname in hostnames:
        try:
            tgt_IP = gethostbyname(hostname) # get IP address by hostname
            print("") # empty space for readability
            print(f"[+] Found {hostname}'s IP: {tgt_IP}")
            print(f"Scanning...")
            port_scan(tgt_IP) # add the tgt_ports variable here as a argument if you're looking for specific ports 
                # just make a input question later that decides if there are specific ones to use, or to just use the default amount
        except:
            print(f"[-] Cannot resolve {hostname}")
        pass
    print("") # empty space for readability
    print("Scan complete!")
