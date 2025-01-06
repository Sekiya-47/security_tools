"""
pip install python-nmap

"""


import nmap_scan

def scan_vulnerabilities(target_ip_addr):
    # Initialize nmap scanner
    scanner = nmap_scan.PortScanner()
    # Execute scan
    scanner.scan(target_ip_addr,arguments='-sV --script=vuln')
    # Analize output of scanning
    for host in scanner.all_hosts():
        print(f'Host: {host} ({scanner[host].hostname()})')
        print(f'State: {scanner[host].state()})')
        for protocol in scanner[host].all_protocols():
            print(f'Protocol:{protocol}')
            local_port = scanner[host].keys()
            for port in local_port:
                print(f'Port: {port}\State: {scanner[host][protocol][port]["state"]}')
                if 'script' in scanner[host][protocol][port]:
                    for script in scanner[host][protocol][port]['script']:
                        print(f'Script: {script}\nOutput: {scanner[host][protocol][port]["script"][script]}')

if __name__ == '__main__':
    target_ip_addr = '192.168.1.1'
    scan_vulnerabilities(target_ip_addr)


