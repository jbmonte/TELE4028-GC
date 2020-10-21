from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI



class SDNTopo( Topo ):

    "Simple SDN topology."

    def __init__( self ):

        "Custom topo"



        Topo.__init__( self )

        #routers
	#the alternative thing to say is
	#r1 = net.addHost('r1', cls=LinuxRouter)
	#or something like that, if you want to make it an actual router

        r1 = self.addSwitch( 'r1' ip="176.16.0.1", defaultRoute = "via 198.51.100.254" ) #Public Router GW2 for external host

        r2 = self.addSwitch( 'r2' ) #Campus Router

        #switches

        s1 = self.addSwitch ( 's1' ip="10.0.0.1", defaultRoute = "via 192.0.2.254" )#Sys Admin GW1 for internal nodes

        s2 = self.addSwitch ( 's2' )#Staff Access

        s3 = self.addSwitch ( 's3' )#Student Access

        s4 = self.addSwitch ( 's4' )#Guest Access

        #hosts

        #h1 = self.addHost( 'h1' , ip='192.168.1.1/24' , defaultRoute='192.168.1.100' )
	h1 = self.addHost( 'h1', ip="172.16.0.0/24", defaultRoute = "via 172.16.0.1" )

        h2 = self.addHost( 'h2' , ip='172.16.0.2/24' )

        h3 = self.addHost( 'h3' , ip='172.16.0.3/24' )

        h4 = self.addHost( 'h4' , ip='172.16.0.4/24' )

        



        #i1 = self.addHost( 'i1' , ip='10.0.0.1/24' )
	i1 = self.addHost( 'i1', ip="10.0.0.0/24", defaultRoute = "via 10.0.0.1" )

        i2 = self.addHost( 'i2' , ip='10.0.0.2/24' )

        i3 = self.addHost( 'i3' , ip='10.0.0.3/24' )

        i4 = self.addHost( 'i4' , ip='10.0.0.4/24' )

        i5 = self.addHost( 'i5' , ip='10.0.0.5/24' )

        i6 = self.addHost( 'i6' , ip='10.0.0.6/24' )

        i7 = self.addHost( 'i7' , ip='10.0.0.7/24' )

        i8 = self.addHost( 'i8' , ip='10.0.0.8/24' )

        i9 = self.addHost( 'i9' , ip='10.0.0.9/24' )

        i10 = self.addHost( 'i10' , ip='10.0.0.10/24' )

        i11 = self.addHost( 'i11' , ip='10.0.0.11/24' )

        i12 = self.addHost( 'i12' , ip='10.0.0.12/24' )

        i13 = self.addHost( 'i13' , ip='10.0.0.13/24' )

        i14 = self.addHost( 'i14' , ip='10.0.0.14/24' )

        i15 = self.addHost( 'i15' , ip='10.0.0.15/24' )

        i16 = self.addHost( 'i16' , ip='10.0.0.16/24' )

        #links

        self.addLink( r1, r2 )



        self.addLink( r2, s1 )

        self.addLink( r2, s2 )

        self.addLink( r2, s3 )

        self.addLink( r2, s4 )



        self.addLink( r1, h1 )

        self.addLink( r1, h2 )

        self.addLink( r1, h3 )

        self.addLink( r1, h4 )



        self.addLink( s1, i1 )

        self.addLink( s1, i2 )

        self.addLink( s1, i3 )

        self.addLink( s1, i4 )



        self.addLink( s2, i5 )

        self.addLink( s2, i6 )

        self.addLink( s2, i7 )

        self.addLink( s2, i8 )

        

        self.addLink( s3, i9 )

        self.addLink( s3, i10 )

        self.addLink( s3, i11 )

        self.addLink( s3, i12 )

        

        self.addLink( s4, i13 )

        self.addLink( s4, i14 )

        self.addLink( s4, i15 )

        self.addLink( s4, i16 )
	
	# bash
	declare -a keys
	for i in {1..4}; do
  		# keys 1 and 3 are for HMAC, keys 2 and 4 are for encryption
  		keys[i]=$(xxd -p -l 32 -c 32 /dev/random)
	done
	
	declare -a spi
	for i in {1..2}; do
  		spi[i]=$(xxd -p -l 4 /dev/random)
	done
	
	declare -a reqid
	for i in {1..2}; do
  		reqid[i]=$(xxd -p -l 4 /dev/random)
	done
	
	ip xfrm state add src 192.0.2.1 dst 198.51.100.20 proto esp spi "0x${spi[1]}" reqid "0x${reqid[1]}" mode tunnel auth sha256 "0x${keys[1]}" enc aes "0x${keys[2]}"
	ip xfrm state add src 198.51.100.20 dst 192.0.2.1 proto esp spi "0x${spi[2]}" reqid "0x${reqid[2]}" mode tunnel auth sha256 "0x${keys[3]}" enc aes "0x${keys[4]}"

	# for GW1
	ip xfrm policy add src 10.0.0.0/24 dst 172.16.0.0/24 dir out tmpl src 192.0.2.1 dst 198.51.100.20 proto esp reqid "0x${reqid[1]}" mode tunnel
	ip xfrm policy add src 172.16.0.0/24 dst 10.0.0.0/24 dir fwd tmpl src 198.51.100.20 dst 192.0.2.1 proto esp reqid "0x${reqid[2]}" mode tunnel
	ip xfrm policy add src 172.16.0.0/24 dst 10.0.0.0/24 dir in tmpl src 198.51.100.20 dst 192.0.2.1 proto esp reqid "0x${reqid[2]}" mode tunnel

	# for GW2
	ip xfrm policy add src 172.16.0.0/24 dst 10.0.0.0/24 dir out tmpl src 198.51.100.20 dst 192.0.2.1 proto esp reqid "0x${reqid[2]}" mode tunnel
	ip xfrm policy add src 10.0.0.0/24 dst 172.16.0.0/24 dir fwd tmpl src 192.0.2.1 dst 198.51.100.20 proto esp reqid "0x${reqid[1]}" mode tunnel
	ip xfrm policy add src 10.0.0.0/24 dst 172.16.0.0/24 dir in tmpl src 192.0.2.1 dst 198.51.100.20 proto esp reqid "0x${reqid[1]}" mode tunnel


topo = SDNTopo( )
net = Mininet( topo )
net.start()
CLI( net )
#net.pingAll() #customise to ping particular hosts based on established security rules
net.stop()

        
