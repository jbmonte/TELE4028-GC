#SAs

ip xfrm state add src 192.0.2.254 dst 172.16.0. proto esp spi "0x${spi[1]}" reqid "0x${reqid[1]}" mode tunnel auth sha256 "0x${keys[1]}" enc aes "0x${keys[2]}"
ip xfrm state add src 172.16.0. dst 192.0.2.254 proto esp spi "0x${spi[2]}" reqid "0x${reqid[2]}" mode tunnel auth sha256 "0x${keys[3]}" enc aes "0x${keys[4]}"