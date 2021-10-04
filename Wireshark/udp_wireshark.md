1) Select the first UDP segment in your trace. What is the packet number of this segment in the trace file?  What type of application-layer payload or protocol message is being carried in this UDP segment?  Look at the details of this packet in Wireshark.  How many fields there are in the UDP header? (You shouldn’t look in the textbook! Answer these questions directly from what you observe in the packet trace.) What are the names of these fields? 

Packet number 4565. Domain Name System. Length, Checksum, Src and Destination Port

2) By consulting the displayed information in Wireshark’s packet content field for this packet (or by consulting the textbook), what is the length (in bytes) of each of the UDP header fields?

The payload is 38 bytes, the length is 48 bytes, therefore 8 bytes

3) The value in the Length field is the length of what? (You can consult the text for this answer). Verify your claim with your captured UDP packet.

The total packet: header + data

4) What is the maximum number of bytes that can be included in a UDP payload?  (Hint: the answer to this question can be determined by your answer to 2. above)

2**16 (Length is two bytes) - 8 of the header

5) What is the largest possible source port number? (Hint: see the hint in 4.)

2**16 

6) What is the protocol number for UDP? Give your answer in decimal notation. To answer this question, you’ll need to look into the Protocol field of the IP datagram containing this UDP segment (see Figure 4.13 in the text, and the discussion of IP header fields). 

17, as the Protocol Field of IP shows.

7) Examine the pair of UDP packets in which your host sends the first UDP packet and the second UDP packet is a reply to this first UDP packet. (Hint: for a second packet to be sent in response to a first packet, the sender of the first packet should be the destination of the second packet).  What is the packet number of the first of these two UDP segments in the trace file?  What is the packet number of the second of these two UDP segments in the trace file? Describe the relationship between the port numbers in the two packets. 

5554. 6089. The sourceport of one is the destination of other. 