from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self, num_hosts):
        Topo.__init__(self)

        s1 = self.addSwitch('s1')
        for i in range(1, num_hosts + 1):
            h = self.addHost('h%s' % i)
            self.addLink(h, s1)

topos = {'mytopo': MyTopo}