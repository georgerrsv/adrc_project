import argparse
from mininet.net import Mininet
from topo import MyTopo
import time
import threading
import os

def iperf_server(host, log_dir, padding):
    host.cmd(f"iperf -s -u -p 5001 -l {padding} > {log_dir}/iperf_server.log 2>&1 &")

def gera_trafego_ipv4(host, server_ip, tempo_exec, log_dir, padding):
    
    ping_dir = f"{log_dir}/ping/{host.name}"
    iperf_dir = f"{log_dir}/iperf/{host.name}"
    os.makedirs(ping_dir, exist_ok=True)
    os.makedirs(iperf_dir, exist_ok=True)
    
    host.cmd(f"ping -c {tempo_exec} {server_ip} -s {padding} > {ping_dir}/ping_{host.name}.log &")
    host.cmd(f"iperf -c {server_ip} -u -t {tempo_exec} -l {padding} --reportstyle C > {iperf_dir}/iperf_{host.name}.csv &")

def main(num_hosts, padding):
    topo = MyTopo(num_hosts=num_hosts)
    net = Mininet(topo=topo)
    net.start()
    
    log_dir = f"experimento/log_host{num_hosts - 1}_padding{padding}"
    os.makedirs(log_dir, exist_ok=True)
    
    server = net.get('h1')
    iperf_server(server, log_dir, padding)
    
    time.sleep(2)
    
    server_ip = server.IP()
    tempo_exec = 2
    
    threads = []
    for i in range(2, num_hosts + 1):
        host = net.get(f'h{i}')
        t = threading.Thread(target=gera_trafego_ipv4, args=(host, server_ip, tempo_exec, log_dir, padding))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    time.sleep(tempo_exec)
    
    net.stop()

def args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--hosts', type=int, default=10, choices=[10, 15, 20])
    parser.add_argument('--padding', type=int, default=1000, choices=[500, 1000, 2000, 3500, 5000])
    args = parser.parse_args()
    return args.hosts, args.padding

if __name__ == "__main__":
    num_hosts, padding = args_parse()
    main(num_hosts + 1, padding)