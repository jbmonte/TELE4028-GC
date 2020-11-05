#SPDs for GW1
ip xfrm policy add src 10.0.0.1 dst 176.16.0.1 dir out tmpl src 172.16.0.0/24 dst 10.0.0.0/24 proto esp reqid "0x${reqid[1]}" mode tunnel
ip xfrm policy add src 176.16.0.1 dst 10.0.0.1 dir fwd tmpl src 10.0.0.0/24 dst 172.16.0.0/24 proto esp reqid "0x${reqid[2]}" mode tunnel
ip xfrm policy add src 10.0.0.0/24 dst 172.16.0.0/24 dir in tmpl src 176.16.0.1 dst 10.0.0.1 proto esp reqid "0x${reqid[2]}" mode tunnel