import argparse
from mininet.net import Mininet
from topo import MyTopo
from mininet.cli import CLI
import time
import threading
import os

def iperf_server(host, log_dir):
    host.cmd(f"iperf -s -u -p 5001 > {log_dir}/iperf_server.log 2>&1 &")

def gera_trafego_ipv4(host, server_ip, tempo_exec, log_dir):
    
    ping_dir = f"{log_dir}/ping/{host.name}"
    iperf_dir = f"{log_dir}/iperf/{host.name}"
    os.makedirs(ping_dir, exist_ok=True)
    os.makedirs(iperf_dir, exist_ok=True)
    
    host.cmd(f"ping -c {tempo_exec} {server_ip} > {ping_dir}/ping_{host.name}.log &")
    host.cmd(f"iperf -c {server_ip} -u -t {tempo_exec} --reportstyle C > {iperf_dir}/iperf_{host.name}.csv &")

def main(num_hosts):
    topo = MyTopo(num_hosts=num_hosts)
    net = Mininet(topo=topo)
    net.start()
    
    log_dir = f"sempadding/log_host{num_hosts - 1}"
    os.makedirs(log_dir, exist_ok=True)
    
    server = net.get('h1')
    iperf_server(server, log_dir)
    
    time.sleep(2)
    
    server_ip = server.IP()
    tempo_exec = 2
    
    threads = []
    for i in range(2, num_hosts + 1):
        host = net.get(f'h{i}')
        t = threading.Thread(target=gera_trafego_ipv4, args=(host, server_ip, tempo_exec, log_dir))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    time.sleep(tempo_exec)
    
    net.stop()

def args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--hosts', type=int, default=10, choices=[10, 15, 20])
    args = parser.parse_args()
    return args.hosts

if __name__ == "__main__":
    num_hosts = args_parse()
    main(num_hosts + 1)