import nmap
def nmap_scan(target):
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-sV -O')  
    
    for host in nm.all_hosts():
        print('----------------------------------------------------')
        print(f'Host : {host} ({nm[host].hostname()})')
        print(f'State : {nm[host].state()}')

        for proto in nm[host].all_protocols():
            print('----------')
            print(f'Protocol : {proto}')

            ports = nm[host][proto].keys()
            for port in ports:
                print(f'Port : {port}\tState : {nm[host][proto][port]["state"]}\tService : {nm[host][proto][port]["name"]}')

target_ip = "185.27.134.107"
nmap_scan(target_ip)
