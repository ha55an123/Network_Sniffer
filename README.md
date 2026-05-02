# 🌐 Network Packet Sniffer (Python Security Project)

## 📌 Overview

This project is a **Network Packet Sniffer** developed using Python for educational and cybersecurity purposes.  
It captures live network traffic and extracts important packet information such as IP addresses, protocol types, ports, and packet length.

The tool helps in understanding how data flows across a network and how different protocols communicate at a low level.

⚠️ **Disclaimer:**  
This project is intended strictly for **educational and ethical use only** in controlled environments.  
Unauthorized packet sniffing on networks you do not own or have permission to analyze is illegal and unethical.

---

## 🎯 Objectives

- Understand network packet structure and behavior
- Learn how network traffic is captured and analyzed
- Identify common network protocols (TCP, UDP, ICMP)
- Store and log packet information for analysis
- Gain practical cybersecurity and networking knowledge

---

## 🛠️ Technologies Used

- Python 3.x  
- :contentReference[oaicite:0]{index=0} (packet manipulation & sniffing library)  
- File handling for logging captured packets  
- Linux networking tools (for execution environment)

---

## ⚙️ How It Works

1. The program starts a packet sniffing session on the network interface.
2. Incoming packets are captured in real time.
3. Each packet is analyzed to extract:
   - Source IP address  
   - Destination IP address  
   - Protocol type (TCP/UDP/ICMP)  
   - Source and destination ports  
   - Packet length  
4. The information is displayed in the terminal.
5. All captured data is saved into a log file (`packet_log.txt`).
6. The sniffer runs continuously until manually stopped.

---

## 📁 Project Structure

---

## ▶️ How to Run

### 1. Install required dependency
```bash
pip install scapy

sudo python3 sniffer.py 
