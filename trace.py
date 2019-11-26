import socket
import struct

"""
TODO

Custom implementation of traceroute
It will only return data needed for the rest of the program (ip and time)
"""


class IPv4Packet:
    def __init__(self, initial_id, ttl, source_ip, destination_ip):
        self.version = 4  # For IPv4, version = 4
        self.IHL = 5  # Header Length. n * 32 bits. 20 bytes IPv4 header.
        self.DSCP = 0  # DF
        self.ECN = 0  # Non-ECT
        self.total_length = 28  # Total Packet length. 20 bytes IPv4 header + 8 bytes ICMP packet.
        self.identification = initial_id  # 16-bit identifier, must change with every packet sent.
        self.flags = 0b010  # Flags. 0bxyz, where x,y,z can be 0 or 1 and x is Reserved (always 0), y = DF and z = MF.
        self.fragment_offset = 0  # No offset needed because only a single packet is needed.
        self.TTL = ttl  # Time To Live. How much time the packet will be around before being dropped (in seconds).
        self.protocol = 1  # Current Protocol, 1 = ICMProtocol
        # checksum needs to be calculated separately.
        self.source_ip = socket.gethostbyaddr(source_ip)  # Source IPv4
        self.destination_ip = socket.gethostbyaddr(destination_ip)  # Destination IPv4
        self.raw = ''

    def checksum(self):  # TODO
        sum = 0
        return sum

    def raw_packet(self):
        self.raw = struct.pack('!BBHHHBBH4s4s', self.version, self.IHL, self.DSCP, self.ECN, self.total_length,
                               self.identification, self.flags, self.fragment_offset, self.TTL, self.protocol,
                               self.checksum(), self.source_ip, self.destination_ip)

        # B = unsigned char, H = unsigned short, s = char[] (4s <=> ssss)
        return None


class ICMP_Packet:
    def __init__(self):
        self.ICMP_type_of_message = 8  # ICMP type of message. 8 = IPv4, ICMP. 128 = IPv6, ICMP6.
        self.ICMP_code = 0  # ICMP subtype / code
        # ICMP_checksum needs to be calculated separately
        # ICMP_header_data

# sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, 1)
