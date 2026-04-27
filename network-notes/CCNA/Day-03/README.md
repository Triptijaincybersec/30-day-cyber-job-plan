\# Day 3 : Inter-VLAN routing Lab



\*\*Objective\*\* : Configure VLANs 10/20,802.1Q trunk, and Router-on-Stick for inter-VLAN communication.



\*\*Topology\*\*:

\-VLAN 10 USERS 192.168.10.0/24 ,PC1 = 192.168.10.10

\-VLAN 20 SERVERS 192.168.20.0/24 ,PC1 = 192.168.20.10

\-Router0 Fa0/0.10 = 192.168.10.1, Fa0/0.20 = 192.168.20.1

\-Switch Fa0/3 trunk to Router0



\*\*Key Commands\*\* :

vlan 10

&#x20;name USERS

vlan 20

&#x20;name SERVERS

int fa0/3

&#x20;switchport mode trunk

&#x20;switchport trunk allowed vlan 10,20

int fa0/0.10

&#x20;encapsulation dot1Q

&#x20;ip address 192.168.10.1 255.255.255.0 





\*\*Troubleshooting Done\*\*:

1. Verified VLAN assignment with 'show vlan brief'
2. Fixed 802.1X blocking traffic on PC
3. Corrected sub-interface to match physical port fa0/0
4. Disabled windows firewall for ICMP



\*\*Proof\*\*: 

!\[PC0 TO VLAN 20 Gateway](../../screenshots/Day-03/day3-pc0-to-vlan20.png)

!\[PC1 TO VLAN 10 Gateway](../../screenshots/Day-03/day3-pc1-to-vlan10.png)





\*\*SOC Relevance\*\*: Mirrors real incident where VLAN misconfiguration or NAC/802.1X blocks legitimate traffic.

&#x20;



