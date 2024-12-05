# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 20:39:25 2024

@author: IAN CARTER KULANI

"""

import socket

print("============================Port scanner============================\n")

def scan_ports(host, start_port, end_port):
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout for the connection attempt
        result = sock.connect_ex((host, port))  # Check if the port is open
        if result == 0:
            open_ports.append(port)
        sock.close()
    
    return open_ports

def main():
    host = input("Enter the IP address to scan:")
    start_port = int(input("Enter start port (e.g., 1):"))
    end_port = int(input("Enter end port (e.g., 1024):"))

    print(f"Scanning {host} for open ports between {start_port} and {end_port}...")
    open_ports = scan_ports(host, start_port, end_port)

    if open_ports:
        print(f"Open ports: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
