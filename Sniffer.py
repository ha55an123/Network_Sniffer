from scapy.all import sniff, IP, TCP, UDP, ICMP

log_file = "packet_log.txt"

def packet_callback(packet):

    if packet.haslayer(IP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        length = len(packet)

        sport = ""
        dport = ""
        proto_name = "OTHER"

        print("\n----- Packet Captured -----")
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print(f"Protocol Number: {proto}")
        print(f"Length: {length}")

        if packet.haslayer(TCP):
            proto_name = "TCP"
            sport = packet[TCP].sport
            dport = packet[TCP].dport

        elif packet.haslayer(UDP):
            proto_name = "UDP"
            sport = packet[UDP].sport
            dport = packet[UDP].dport

        elif packet.haslayer(ICMP):
            proto_name = "ICMP"

        print(f"Protocol Type: {proto_name}")

        if sport and dport:
            print(f"Source Port: {sport}")
            print(f"Destination Port: {dport}")

        log = f"{src_ip}:{sport} -> {dst_ip}:{dport} | {proto_name} | Length:{length}\n"

        with open(log_file, "a") as f:
            f.write(log)


print("Starting Network Sniffer.... Press Ctrl+C to stop")

sniff(prn=packet_callback, store=False)
