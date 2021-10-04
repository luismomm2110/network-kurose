# IP WIRESHARK

## PART A

### __ Select the first UDP segment sent by your computer via the traceroute command to gaia.cs.umass.edu. (Hint: this is 44th packet in the trace file in the ip-wireshark-trace1-1.pcapng file in footnote) Expand the Internet Protocol part of the packet in the packet details window.  What is the IP address of your computer?

- 192.168.86.61

### What is the value in the time-to-live (TTL) field in this IPv4 datagram’s header?

- TTL: 1

### What is the value in the upper layer protocol field in this IPv4 datagram’s header? [Note: the answers for Linux/MacOS differ from Windows here].

- 17 (UDP)

### How many bytes are in the IP header? 

20 bytes 

### How many bytes are in the payload of the IP datagram?  Explain how you determined the number of payload bytes.

Total length - Header: 36 bytes

### Has this IP datagram been fragmented?  Explain how you determined whether or not the datagram has been fragmented.

No. Fragment offset = 0

### Which fields in the IP datagram always change from one datagram to the next within this series of UDP segments sent by your computer destined to 128.119.245.12, via traceroute?  Why?

Time to Live changes because this how traceroute calculate  trace. Destination Port change also (it's randomic to not enter)

### Which fields in this sequence of IP datagrams (containing UDP segments) Which stay constant? Why?

Source port, destination and source IP, Data

### Describe the pattern you see in the values in the Identification field of the IP datagrams being sent by your computer.

Increases by one everytime

### What is the upper layer protocol specified in the IP datagrams returned from the routers? [Note: the answers for Linux/MacOS differ from Windows here].

Protocol 1: ICMP

### Are the values in the Identification fields (across the sequence of all of ICMP packets from all of the routers) similar in behavior to your answer to question 9 above?

Also increases by one everytime

### Are the values of the TTL fields similar, across all of ICMP packets from all of the routers?

No, it varies

### Find the first IP datagram containing the first part of the segment sent to 128.119.245.12 sent by your computer via the traceroute command to gaia.cs.umass.edu, after you specified that the traceroute packet length should be 3000. (Hint: This is packet 179 in the ip-wireshark-trace1-1.pcapng trace file in footnote 2. Packets 179, 180, and 181 are three IP datagrams created by fragmenting the first single 3000-byte UDP segment sent to 128.119.145.12).   Has that segment been fragmented across more than one IP datagram? (Hint: the answer is yes!)  

Yes. The segment flag was set.

### What information in the IP header indicates that this datagram been fragmented?  

Flag fragment.

### What information in the IP header for this packet indicates whether this is the first fragment versus a latter fragment?

Fragment offset 0 indicates that is the first in fragmented sequence

### How many bytes are there in is this IP datagram (header plus payload)?

1514 byes

### Now inspect the datagram containing the second fragment of the fragmented UDP segment. What information in the IP header indicates that this is not the first datagram fragment? 
 
Fragment offset is not zero (is 1480)

### What fields change in the IP header between the first and second fragment?

Fragment offset

### Now find the IP datagram containing the third fragment of the original UDP segment. What information in the IP header indicates that this is the last fragment of that segment?  

More fragments flag is zero

### What is the IPv6 address of the computer making the DNS AAAA request?  This is the source address of the 20th packet in the trace. Give the IPv6 source address for this datagram in the exact same form as displayed in the Wireshark window.

2601:193:8302:4620:215c:f5ae:8b40:a27

### What is the IPv6 destination address for this datagram? Give this IPv6 address in the exact same form as displayed in the Wireshark window.  

2001:558:feed::1

### What is the value of the flow label for this datagram?

0x00063ed0

### How much payload data is carried in this datagram?

37 bytes

### What is the upper layer protocol to which this datagram’s payload will be delivered at the destination?

UDP

### How many IPv6 addresses are returned in the response to this AAAA request?

One

### What is the first of the IPv6 addresses returned by the DNS for youtube.com (in the ip-wireshark-trace2-1.pcapng trace file, this is also the address that is numerically the smallest)? Give this IPv6 address in the exact same shorthand form as displayed in the Wireshark window.

2607:f8b0:4006:806::200e
