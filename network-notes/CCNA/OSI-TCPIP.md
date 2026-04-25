### 

\# Day 1: OSI Model \& TCP/IP Suite Notes



\*\*Date:\*\* 2026-04-25  

\*\*Source:\*\* CCNA video study + handwritten notes  

\*\*Full handwritten notes:\*\* `/screenshots/OSI-notes-day1.jpg`, `OSI-notes-day2.jpg`, `OSI-notes-day3.jpg`



\## Why OSI Model Exists



Before OSI, each vendor had different networking protocols. PCs from different companies could not communicate.



\*\*OSI = Open System Interconnection model\*\*

\- Conceptual model that categorizes and standardizes network functions

\- Created by ISO in 1980s

\- Divides network communication into 7 layers

\- Each layer communicates with same layer on other device



\*\*Networking model:\*\* Organized and flexible structure for hardware/software protocols.  

\*\*Protocol:\*\* Set of rules to ensure devices and software work together.



\## The 7 OSI Layers



\*\*Layer 7: Application\*\*

\- Close to end user, interface with software applications

\- Example: Web browser uses HTTP/HTTPS

\- App developers work with Application layer to connect apps over networks



\*\*Layer 6: Presentation\*\*

\- Job is to translate data from application into a format that can be transported over network

\- Data in application format → needs to be transported in different format

\- Ex: Encryption of data as it sent, decryption of data as it received

\- Also translates between different application layer formats so each app can understand



\*\*Layer 5: Session\*\*

\- Control dialogue/session between communication hosts

\- Establish, manage and terminate communication between applications

\- Example: Your browser and remote application



\*\*Layer 4: Transport\*\*

\- Segments and reassembles data for communication

\- Breaks large chunks of data into smaller segments which can be easily sent and reassembled by receiver

\- Provides host to host communication or end to end communication for applications

\- Examples: TCP, UDP



\*\*Layer 3: Network\*\*

\- Provides connectivity between hosts on different networks, outside of LAN

\- Provides logical addressing: IP addresses

\- Provides path selection between source and destination

\- Routers operate at Layer 3



\*\*Layer 2: Data Link\*\*

\- Provides node to node connectivity and data transfer

\- Ex: PC to switch, switch to router, router to router

\- Switches operate at Layer 2

\- Defines how data is formatted for transmission over a physical medium



\*\*Layer 1: Physical\*\*

\- Defines physical characteristics of medium used to transfer data

\- Ex: Voltage levels, max transmission distance, physical connectors, cable specs

\- Digital bits are converted into electrical, wireless, or radio signals for wireless connections

\- At Layer 1, the PDU is bit



\*\*Acronym to remember:\*\* All People Seem To Need Data Processing  

Application → Presentation → Session → Transport → Network → Data Link → Physical



\## Key Concepts



\*\*Encapsulation/De-encapsulation\*\*

\- When data passes through OSI stack, each layer adds its own info

\- Data + headers = encapsulated as it goes down

\- At receiving system, headers stripped off = de-encapsulation

\- Data reaches Physical layer as electrical signals on wire



\*\*PDU Names by Layer:\*\*

\- Layer 7-5: Data

\- Layer 4: Segment  

\- Layer 3: Packet

\- Layer 2: Frame

\- Layer 1: Bit



\## TCP/IP Suite



\*\*TCP/IP:\*\* Conceptual model and set of communications protocols used on Internet and other networks.

\- Developed by United States Department of Defense through DARPA (Defense Advanced Research Project Agency)

\- Actually used in modern networks



\*\*OSI Model vs TCP/IP:\*\*

OSI model still appears in network engineering work and job talks.



\*\*4-Layer TCP/IP Model:\*\*

1\. \*\*Application\*\* - App/Presentation/Session in OSI

2\. \*\*Transport\*\* - Transport in OSI  

3\. \*\*Internet\*\* - Network in OSI

4\. \*\*Link\*\* - Data Link/Physical in OSI



\*\*Full handwritten notes:\*\* 

\- `/CCNA/Day1-OSI-TCP-handwritten/page1.jpg`

\- `/CCNA/Day1-OSI-TCP-handwritten/page2.jpg`

\- `/CCNA/Day1-OSI-TCP-handwritten/page3.jpg`



\---

\*Day 1 of 30 Day Cyber Job Plan | Next: Linux commands + Subnetting practice\*

