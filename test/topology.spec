
vm oob-mgmt-server netq-1.4.0 2 10 40
vm netq1 netq-1.3.0 2 10 40

vm UDCLAYN00001 cumulus-vx-3.6.2 1 2 2
vm UDCLAYN00002 cumulus-vx-3.6.2 1 2 2
vm SDCLAYN00001 cumulus-vx-3.6.2 1 2 2
vm SDCLAYN00002 cumulus-vx-3.6.2 1 2 2
vm LDCLAYN00005 cumulus-vx-3.6.2 1 2 2
vm LDCLAYN00006 cumulus-vx-3.6.2 1 2 2
vm LDCLAYN00007 cumulus-vx-3.6.2 1 2 2
vm LDCLAYN00008 cumulus-vx-3.6.2 1 2 2
vm BDCLAYN00001 cumulus-vx-3.6.2 1 2 2
vm BDCLAYN00002 cumulus-vx-3.6.2 1 2 2
vm RDCLAYN00001 cumulus-vx-3.6.2 1 2 2
vm RDCLAYN00002 cumulus-vx-3.6.2 1 2 2

vm CDCLAYN00010  ubuntu-16.04 2 4 4
vm XDCLAYN00009 ubuntu-16.04 2 4 4
vm YDCLAYN00005 ubuntu-16.04 2 4 4
vm CDCLAYN00014 ubuntu-16.04 2 4 4
vm XDCLAYN00011 ubuntu-16.04 2 4 4
vm YDCLAYN00011 ubuntu-16.04 2 4 4

vm fake-spine3 cumulus-vx-3.6.2 1 2 2
vm fake-spine4 cumulus-vx-3.6.2 1 2 2
vm fake-server3 ubuntu-16.04 2 4 4
vm fake-server4 ubuntu-16.04 2 4 4
vm fake-future-spine cumulus-vx-3.6.2 1 2 2
vm fake-server6 ubuntu-16.04 2 4 4
vm fake-server7 ubuntu-16.04 2 4 4
vm fake-server8 ubuntu-16.04 2 4 4
vm fake-server9 ubuntu-16.04 2 4 4


network oob-mgmt-server eth0 10.255.0.1 255.255.0.0 public
service oob-mgmt-server ssh eth0 22 TCP public
service oob-mgmt-server http eth0 80 TCP public
service oob-mgmt-server https eth0 443 TCP public
service oob-mgmt-server http2 eth0 1337 TCP public
service oob-mgmt-server grafana eth0 3000 TCP public
service oob-mgmt-server netqgui eth0 5000 TCP public
service oob-mgmt-server novnc eth0 6080 TCP public
service oob-mgmt-server netq eth0 9000 TCP public
service oob-mgmt-server mesos eth0 5050 TCP public
service oob-mgmt-server marathon eth0 8080 TCP public
service oob-mgmt-server mesosapp eth0 8088 TCP public

network oob-mgmt-server eth1 192.168.0.1 255.255.0.0
network netq1 eth0 192.168.0.2 255.255.0.0
network UDCLAYN00001 eth0 192.168.0.11
network UDCLAYN00002 eth0 192.168.0.12
network SDCLAYN00001 eth0 192.168.0.21
network SDCLAYN00002 eth0 192.168.0.22
network LDCLAYN00005 eth0 192.168.0.35
network LDCLAYN00006 eth0 192.168.0.36
network LDCLAYN00007 eth0  192.168.0.37
network LDCLAYN00008 eth0 192.168.0.38
network BDCLAYN00001 eth0 192.168.0.41
network BDCLAYN00002 eth0 192.168.0.42
network RDCLAYN00001 eth0 192.168.0.51
network RDCLAYN00002 eth0 192.168.0.52

network CDCLAYN00010 eth0 192.168.0.61
network XDCLAYN00009 eth0 192.168.0.62
network YDCLAYN00005 eth0 192.168.0.63
network CDCLAYN00014 eth0 192.168.0.64
network XDCLAYN00011 eth0 192.168.0.65
network YDCLAYN00011 eth0 192.168.0.66

network fake-spine3 eth0 192.168.0.71
network fake-spine4 eth0 192.168.0.72
network fake-server3 eth0  192.168.0.73
network fake-server4 eth0 192.168.0.74
network fake-future-spine eth0 192.168.0.75
network fake-server6 eth0 192.168.0.76
network fake-server7 eth0 192.168.0.77
network fake-server8 eth0 192.168.0.78
network fake-server9 eth0 192.168.0.79

autoconfig oob-mgmt-server

connect LDCLAYN00005 swp11 SDCLAYN00001 swp13 
connect LDCLAYN00005 swp12 SDCLAYN00002 swp13 
connect LDCLAYN00005 swp27 fake-spine3 swp13 
connect LDCLAYN00005 swp28 fake-spine4 swp13 
connect LDCLAYN00006 swp11 SDCLAYN00001 swp14 
connect LDCLAYN00006 swp12 SDCLAYN00002 swp14 
connect LDCLAYN00006 swp27 fake-spine3 swp14 
connect LDCLAYN00006 swp28 fake-spine4 swp14 
connect LDCLAYN00005 swp15 LDCLAYN00006 swp15 
connect LDCLAYN00005 swp16 LDCLAYN00006 swp16 
connect LDCLAYN00005 swp1s0 CDCLAYN00010 eth1 
connect LDCLAYN00006 swp1s0 CDCLAYN00010 eth2 
connect LDCLAYN00005 swp17s0 CDCLAYN00010 eth3 
connect LDCLAYN00006 swp17s0 CDCLAYN00010 eth4 
connect LDCLAYN00005 swp2s0 XDCLAYN00009 eth1 
connect LDCLAYN00006 swp2s0 XDCLAYN00009 eth2 
connect LDCLAYN00005 swp18s0 XDCLAYN00009 eth3 
connect LDCLAYN00006 swp18s0 XDCLAYN00009 eth4 
connect LDCLAYN00005 swp7s0 YDCLAYN00005 eth1 
connect LDCLAYN00006 swp7s0 YDCLAYN00005 eth2 
connect LDCLAYN00005 swp23s0 YDCLAYN00005 eth3 
connect LDCLAYN00006 swp23s0 YDCLAYN00005 eth4 
connect LDCLAYN00005 swp1s1 fake-server3 1 
connect LDCLAYN00005 swp1s2 fake-server3 2 
connect LDCLAYN00005 swp1s3 fake-server3 3 
connect LDCLAYN00005 swp2s1 fake-server3 4 
connect LDCLAYN00005 swp2s2 fake-server3 5 
connect LDCLAYN00005 swp2s3 fake-server3 6 
connect LDCLAYN00005 swp3s0 fake-server3 7 
connect LDCLAYN00005 swp3s1 fake-server3 8 
connect LDCLAYN00005 swp3s2 fake-server3 9 
connect LDCLAYN00005 swp3s3 fake-server3 10 
connect LDCLAYN00005 swp4s0 fake-server3 11 
connect LDCLAYN00005 swp4s1 fake-server3 12 
connect LDCLAYN00005 swp4s2 fake-server3 13 
connect LDCLAYN00005 swp4s3 fake-server3 14 
connect LDCLAYN00005 swp5s0 fake-server3 15 
connect LDCLAYN00005 swp5s1 fake-server3 16 
connect LDCLAYN00005 swp5s2 fake-server3 17 
connect LDCLAYN00005 swp5s3 fake-server3 18 
connect LDCLAYN00005 swp6s0 fake-server3 19 
connect LDCLAYN00005 swp6s1 fake-server3 20 
connect LDCLAYN00005 swp6s2 fake-server3 21 
connect LDCLAYN00005 swp6s3 fake-server3 22 
connect LDCLAYN00005 swp7s1 fake-server3 24 
connect LDCLAYN00005 swp7s2 fake-server3 25 
connect LDCLAYN00005 swp7s3 fake-server3 26 
connect LDCLAYN00005 swp8s0 fake-server3 27 
connect LDCLAYN00005 swp8s1 fake-server3 28 
connect LDCLAYN00005 swp8s2 fake-server3 29 
connect LDCLAYN00005 swp8s3 fake-server3 30 
connect LDCLAYN00005 swp17s1 fake-server3 32 
connect LDCLAYN00005 swp17s2 fake-server3 33 
connect LDCLAYN00005 swp17s3 fake-server3 34 
connect LDCLAYN00005 swp18s1 fake-server3 36 
connect LDCLAYN00005 swp18s2 fake-server3 37 
connect LDCLAYN00005 swp18s3 fake-server3 38 
connect LDCLAYN00005 swp19s0 fake-server3 39 
connect LDCLAYN00005 swp19s1 fake-server3 40 
connect LDCLAYN00005 swp19s2 fake-server3 41 
connect LDCLAYN00005 swp19s3 fake-server3 42 
connect LDCLAYN00005 swp20s0 fake-server3 43 
connect LDCLAYN00005 swp20s1 fake-server3 44 
connect LDCLAYN00005 swp20s2 fake-server3 45 
connect LDCLAYN00005 swp20s3 fake-server3 46 
connect LDCLAYN00005 swp21s0 fake-server3 47 
connect LDCLAYN00005 swp21s1 fake-server3 48 
connect LDCLAYN00005 swp21s2 fake-server3 49 
connect LDCLAYN00005 swp21s3 fake-server3 50 
connect LDCLAYN00005 swp22s0 fake-server3 51 
connect LDCLAYN00005 swp22s1 fake-server3 52 
connect LDCLAYN00005 swp22s2 fake-server3 53 
connect LDCLAYN00005 swp22s3 fake-server3 54 
connect LDCLAYN00005 swp23s1 fake-server3 56 
connect LDCLAYN00005 swp23s2 fake-server3 57 
connect LDCLAYN00005 swp23s3 fake-server3 58 
connect LDCLAYN00005 swp24s0 fake-server3 59 
connect LDCLAYN00005 swp24s1 fake-server3 60 
connect LDCLAYN00005 swp24s2 fake-server3 61 
connect LDCLAYN00005 swp24s3 fake-server3 62 
connect LDCLAYN00006 swp1s1 fake-server3 63 
connect LDCLAYN00006 swp1s2 fake-server3 64 
connect LDCLAYN00006 swp1s3 fake-server3 65 
connect LDCLAYN00006 swp2s1 fake-server3 66 
connect LDCLAYN00006 swp2s2 fake-server3 67 
connect LDCLAYN00006 swp2s3 fake-server3 68 
connect LDCLAYN00006 swp3s0 fake-server3 69 
connect LDCLAYN00006 swp3s1 fake-server3 70 
connect LDCLAYN00006 swp3s2 fake-server3 71 
connect LDCLAYN00006 swp3s3 fake-server3 72 
connect LDCLAYN00006 swp4s0 fake-server3 73 
connect LDCLAYN00006 swp4s1 fake-server3 74 
connect LDCLAYN00006 swp4s2 fake-server3 75 
connect LDCLAYN00006 swp4s3 fake-server3 76 
connect LDCLAYN00006 swp5s0 fake-server3 77 
connect LDCLAYN00006 swp5s1 fake-server3 78 
connect LDCLAYN00006 swp5s2 fake-server3 79 
connect LDCLAYN00006 swp5s3 fake-server3 80 
connect LDCLAYN00006 swp6s0 fake-server3 81 
connect LDCLAYN00006 swp6s1 fake-server3 82 
connect LDCLAYN00006 swp6s2 fake-server3 83 
connect LDCLAYN00006 swp6s3 fake-server3 84 
connect LDCLAYN00006 swp7s1 fake-server3 86 
connect LDCLAYN00006 swp7s2 fake-server3 87 
connect LDCLAYN00006 swp7s3 fake-server3 88 
connect LDCLAYN00006 swp8s0 fake-server3 89 
connect LDCLAYN00006 swp8s1 fake-server3 90 
connect LDCLAYN00006 swp8s2 fake-server3 91 
connect LDCLAYN00006 swp8s3 fake-server3 92 
connect LDCLAYN00006 swp17s1 fake-server3 94 
connect LDCLAYN00006 swp17s2 fake-server3 95 
connect LDCLAYN00006 swp17s3 fake-server3 96 
connect LDCLAYN00006 swp18s1 fake-server3 98 
connect LDCLAYN00006 swp18s2 fake-server3 99 
connect LDCLAYN00006 swp18s3 fake-server3 100 
connect LDCLAYN00006 swp19s0 fake-server3 101 
connect LDCLAYN00006 swp19s1 fake-server3 102 
connect LDCLAYN00006 swp19s2 fake-server3 103 
connect LDCLAYN00006 swp19s3 fake-server3 104 
connect LDCLAYN00006 swp20s0 fake-server3 105 
connect LDCLAYN00006 swp20s1 fake-server3 106 
connect LDCLAYN00006 swp20s2 fake-server3 107 
connect LDCLAYN00006 swp20s3 fake-server3 108 
connect LDCLAYN00006 swp21s0 fake-server3 109 
connect LDCLAYN00006 swp21s1 fake-server3 110 
connect LDCLAYN00006 swp21s2 fake-server3 111 
connect LDCLAYN00006 swp21s3 fake-server3 112 
connect LDCLAYN00006 swp22s0 fake-server3 113 
connect LDCLAYN00006 swp22s1 fake-server3 114 
connect LDCLAYN00006 swp22s2 fake-server3 115 
connect LDCLAYN00006 swp22s3 fake-server3 116 
connect LDCLAYN00006 swp23s1 fake-server3 118 
connect LDCLAYN00006 swp23s2 fake-server3 119 
connect LDCLAYN00006 swp23s3 fake-server3 120 
connect LDCLAYN00006 swp24s0 fake-server3 121 
connect LDCLAYN00006 swp24s1 fake-server3 122 
connect LDCLAYN00006 swp24s2 fake-server3 123 
connect LDCLAYN00006 swp24s3 fake-server3 124 
connect LDCLAYN00007 swp11 SDCLAYN00001 swp15 
connect LDCLAYN00007 swp12 SDCLAYN00002 swp15 
connect LDCLAYN00007 swp27 fake-spine3 swp15 
connect LDCLAYN00007 swp28 fake-spine4 swp15 
connect LDCLAYN00008 swp11 SDCLAYN00001 swp16 
connect LDCLAYN00008 swp12 SDCLAYN00002 swp16 
connect LDCLAYN00008 swp27 fake-spine3 swp16 
connect LDCLAYN00008 swp28 fake-spine4 swp16 
connect LDCLAYN00007 swp15 LDCLAYN00008 swp15 
connect LDCLAYN00007 swp16 LDCLAYN00008 swp16 
connect LDCLAYN00007 swp1s0 CDCLAYN00014 eth1 
connect LDCLAYN00008 swp1s0 CDCLAYN00014 eth2 
connect LDCLAYN00007 swp17s0 CDCLAYN00014 eth3 
connect LDCLAYN00008 swp17s0 CDCLAYN00014 eth4 
connect LDCLAYN00007 swp3s1 XDCLAYN00011 eth1 
connect LDCLAYN00008 swp3s1 XDCLAYN00011 eth2 
connect LDCLAYN00007 swp19s1 XDCLAYN00011 eth3 
connect LDCLAYN00008 swp19s1 XDCLAYN00011 eth4 
connect LDCLAYN00007 swp7s0 YDCLAYN00011 eth1 
connect LDCLAYN00008 swp7s0 YDCLAYN00011 eth2 
connect LDCLAYN00007 swp23s0 YDCLAYN00011 eth3 
connect LDCLAYN00008 swp23s0 YDCLAYN00011 eth4 
connect LDCLAYN00007 swp1s1 fake-server4 1 
connect LDCLAYN00007 swp1s2 fake-server4 2 
connect LDCLAYN00007 swp1s3 fake-server4 3 
connect LDCLAYN00007 swp2s0 fake-server4 4 
connect LDCLAYN00007 swp2s1 fake-server4 5 
connect LDCLAYN00007 swp2s2 fake-server4 6 
connect LDCLAYN00007 swp2s3 fake-server4 7 
connect LDCLAYN00007 swp3s0 fake-server4 8 
connect LDCLAYN00007 swp3s2 fake-server4 9 
connect LDCLAYN00007 swp3s3 fake-server4 10 
connect LDCLAYN00007 swp4s0 fake-server4 11 
connect LDCLAYN00007 swp4s1 fake-server4 12 
connect LDCLAYN00007 swp4s2 fake-server4 13 
connect LDCLAYN00007 swp4s3 fake-server4 14 
connect LDCLAYN00007 swp5s0 fake-server4 15 
connect LDCLAYN00007 swp5s1 fake-server4 16 
connect LDCLAYN00007 swp5s2 fake-server4 17 
connect LDCLAYN00007 swp5s3 fake-server4 18 
connect LDCLAYN00007 swp6s0 fake-server4 19 
connect LDCLAYN00007 swp6s1 fake-server4 20 
connect LDCLAYN00007 swp6s2 fake-server4 21 
connect LDCLAYN00007 swp6s3 fake-server4 22 
connect LDCLAYN00007 swp7s1 fake-server4 23 
connect LDCLAYN00007 swp7s2 fake-server4 24 
connect LDCLAYN00007 swp7s3 fake-server4 25 
connect LDCLAYN00007 swp8s0 fake-server4 26 
connect LDCLAYN00007 swp8s1 fake-server4 27 
connect LDCLAYN00007 swp8s2 fake-server4 28 
connect LDCLAYN00007 swp8s3 fake-server4 29 
connect LDCLAYN00007 swp17s1 fake-server4 30 
connect LDCLAYN00007 swp17s2 fake-server4 31 
connect LDCLAYN00007 swp17s3 fake-server4 32 
connect LDCLAYN00007 swp18s0 fake-server4 33 
connect LDCLAYN00007 swp18s1 fake-server4 34 
connect LDCLAYN00007 swp18s2 fake-server4 35 
connect LDCLAYN00007 swp18s3 fake-server4 36 
connect LDCLAYN00007 swp19s0 fake-server4 37 
connect LDCLAYN00007 swp19s2 fake-server4 38 
connect LDCLAYN00007 swp19s3 fake-server4 39 
connect LDCLAYN00007 swp20s0 fake-server4 40 
connect LDCLAYN00007 swp20s1 fake-server4 41 
connect LDCLAYN00007 swp20s2 fake-server4 42 
connect LDCLAYN00007 swp20s3 fake-server4 43 
connect LDCLAYN00007 swp21s0 fake-server4 44 
connect LDCLAYN00007 swp21s1 fake-server4 45 
connect LDCLAYN00007 swp21s2 fake-server4 46 
connect LDCLAYN00007 swp21s3 fake-server4 47 
connect LDCLAYN00007 swp22s0 fake-server4 48 
connect LDCLAYN00007 swp22s1 fake-server4 49 
connect LDCLAYN00007 swp22s2 fake-server4 50 
connect LDCLAYN00007 swp22s3 fake-server4 51 
connect LDCLAYN00007 swp23s1 fake-server4 52 
connect LDCLAYN00007 swp23s2 fake-server4 53 
connect LDCLAYN00007 swp23s3 fake-server4 54 
connect LDCLAYN00007 swp24s0 fake-server4 55 
connect LDCLAYN00007 swp24s1 fake-server4 56 
connect LDCLAYN00007 swp24s2 fake-server4 57 
connect LDCLAYN00007 swp24s3 fake-server4 58 
connect LDCLAYN00008 swp1s1 fake-server4 59 
connect LDCLAYN00008 swp1s2 fake-server4 60 
connect LDCLAYN00008 swp1s3 fake-server4 61 
connect LDCLAYN00008 swp2s0 fake-server4 62 
connect LDCLAYN00008 swp2s1 fake-server4 63 
connect LDCLAYN00008 swp2s2 fake-server4 64 
connect LDCLAYN00008 swp2s3 fake-server4 65 
connect LDCLAYN00008 swp3s0 fake-server4 66 
connect LDCLAYN00008 swp3s2 fake-server4 67 
connect LDCLAYN00008 swp3s3 fake-server4 68 
connect LDCLAYN00008 swp4s0 fake-server4 69 
connect LDCLAYN00008 swp4s1 fake-server4 70 
connect LDCLAYN00008 swp4s2 fake-server4 71 
connect LDCLAYN00008 swp4s3 fake-server4 72 
connect LDCLAYN00008 swp5s0 fake-server4 73 
connect LDCLAYN00008 swp5s1 fake-server4 74 
connect LDCLAYN00008 swp5s2 fake-server4 75 
connect LDCLAYN00008 swp5s3 fake-server4 76 
connect LDCLAYN00008 swp6s0 fake-server4 77 
connect LDCLAYN00008 swp6s1 fake-server4 78 
connect LDCLAYN00008 swp6s2 fake-server4 79 
connect LDCLAYN00008 swp6s3 fake-server4 80 
connect LDCLAYN00008 swp7s1 fake-server4 81 
connect LDCLAYN00008 swp7s2 fake-server4 82 
connect LDCLAYN00008 swp7s3 fake-server4 83 
connect LDCLAYN00008 swp8s0 fake-server4 84 
connect LDCLAYN00008 swp8s1 fake-server4 85 
connect LDCLAYN00008 swp8s2 fake-server4 86 
connect LDCLAYN00008 swp8s3 fake-server4 87 
connect LDCLAYN00008 swp17s1 fake-server4 88 
connect LDCLAYN00008 swp17s2 fake-server4 89 
connect LDCLAYN00008 swp17s3 fake-server4 90 
connect LDCLAYN00008 swp18s0 fake-server4 91 
connect LDCLAYN00008 swp18s1 fake-server4 92 
connect LDCLAYN00008 swp18s2 fake-server4 93 
connect LDCLAYN00008 swp18s3 fake-server4 94 
connect LDCLAYN00008 swp19s0 fake-server4 95 
connect LDCLAYN00008 swp19s2 fake-server4 96 
connect LDCLAYN00008 swp19s3 fake-server4 97 
connect LDCLAYN00008 swp20s0 fake-server4 98 
connect LDCLAYN00008 swp20s1 fake-server4 99 
connect LDCLAYN00008 swp20s2 fake-server4 100 
connect LDCLAYN00008 swp20s3 fake-server4 101 
connect LDCLAYN00008 swp21s0 fake-server4 102 
connect LDCLAYN00008 swp21s1 fake-server4 103 
connect LDCLAYN00008 swp21s2 fake-server4 104 
connect LDCLAYN00008 swp21s3 fake-server4 105 
connect LDCLAYN00008 swp22s0 fake-server4 106 
connect LDCLAYN00008 swp22s1 fake-server4 107 
connect LDCLAYN00008 swp22s2 fake-server4 108 
connect LDCLAYN00008 swp22s3 fake-server4 109 
connect LDCLAYN00008 swp23s1 fake-server4 110 
connect LDCLAYN00008 swp23s2 fake-server4 111 
connect LDCLAYN00008 swp23s3 fake-server4 112 
connect LDCLAYN00008 swp24s0 fake-server4 113 
connect LDCLAYN00008 swp24s1 fake-server4 114 
connect LDCLAYN00008 swp24s2 fake-server4 115 
connect LDCLAYN00008 swp24s3 fake-server4 116 
connect SDCLAYN00001 swp1 UDCLAYN00001 swp1 
connect SDCLAYN00001 swp2 UDCLAYN00001 swp2 
connect SDCLAYN00001 swp3 UDCLAYN00001 swp3 
connect SDCLAYN00001 swp4 UDCLAYN00001 swp4 
connect SDCLAYN00001 swp5 UDCLAYN00002 swp1 
connect SDCLAYN00001 swp6 UDCLAYN00002 swp2 
connect SDCLAYN00001 swp7 UDCLAYN00002 swp3 
connect SDCLAYN00001 swp8 UDCLAYN00002 swp4 
connect SDCLAYN00002 swp1 UDCLAYN00001 swp5 
connect SDCLAYN00002 swp2 UDCLAYN00001 swp6 
connect SDCLAYN00002 swp3 UDCLAYN00001 swp7 
connect SDCLAYN00002 swp4 UDCLAYN00001 swp8 
connect SDCLAYN00002 swp5 UDCLAYN00002 swp5 
connect SDCLAYN00002 swp6 UDCLAYN00002 swp6 
connect SDCLAYN00002 swp7 UDCLAYN00002 swp7 
connect SDCLAYN00002 swp8 UDCLAYN00002 swp8 
connect fake-spine3 swp1 UDCLAYN00001 swp9 
connect fake-spine3 swp2 UDCLAYN00001 swp10 
connect fake-spine3 swp3 UDCLAYN00001 swp11 
connect fake-spine3 swp4 UDCLAYN00001 swp12 
connect fake-spine3 swp5 UDCLAYN00002 swp9 
connect fake-spine3 swp6 UDCLAYN00002 swp10 
connect fake-spine3 swp7 UDCLAYN00002 swp11 
connect fake-spine3 swp8 UDCLAYN00002 swp12 
connect fake-spine4 swp1 UDCLAYN00001 swp13 
connect fake-spine4 swp2 UDCLAYN00001 swp14 
connect fake-spine4 swp3 UDCLAYN00001 swp15 
connect fake-spine4 swp4 UDCLAYN00001 swp16 
connect fake-spine4 swp5 UDCLAYN00002 swp13 
connect fake-spine4 swp6 UDCLAYN00002 swp14 
connect fake-spine4 swp7 UDCLAYN00002 swp15 
connect fake-spine4 swp8 UDCLAYN00002 swp16 
connect UDCLAYN00001 swp17 fake-future-spine swp1 
connect UDCLAYN00001 swp18 fake-future-spine swp2 
connect UDCLAYN00001 swp19 fake-future-spine swp3 
connect UDCLAYN00001 swp20 fake-future-spine swp4 
connect UDCLAYN00001 swp21 fake-future-spine swp5 
connect UDCLAYN00001 swp22 fake-future-spine swp6 
connect UDCLAYN00001 swp23 fake-future-spine swp7 
connect UDCLAYN00001 swp24 fake-future-spine swp8 
connect UDCLAYN00001 swp25 fake-future-spine swp9 
connect UDCLAYN00001 swp26 fake-future-spine swp10 
connect UDCLAYN00001 swp27 fake-future-spine swp11 
connect UDCLAYN00001 swp28 fake-future-spine swp12 
connect UDCLAYN00001 swp29 fake-future-spine swp13 
connect UDCLAYN00001 swp30 fake-future-spine swp14 
connect UDCLAYN00001 swp31 fake-future-spine swp15 
connect UDCLAYN00001 swp32 fake-future-spine swp16 
connect UDCLAYN00002 swp17 fake-future-spine swp17 
connect UDCLAYN00002 swp18 fake-future-spine swp18 
connect UDCLAYN00002 swp19 fake-future-spine swp19 
connect UDCLAYN00002 swp20 fake-future-spine swp20 
connect UDCLAYN00002 swp21 fake-future-spine swp21 
connect UDCLAYN00002 swp22 fake-future-spine swp22 
connect UDCLAYN00002 swp23 fake-future-spine swp23 
connect UDCLAYN00002 swp24 fake-future-spine swp24 
connect UDCLAYN00002 swp25 fake-future-spine swp25 
connect UDCLAYN00002 swp26 fake-future-spine swp26 
connect UDCLAYN00002 swp27 fake-future-spine swp27 
connect UDCLAYN00002 swp28 fake-future-spine swp28 
connect UDCLAYN00002 swp29 fake-future-spine swp29 
connect UDCLAYN00002 swp30 fake-future-spine swp30 
connect UDCLAYN00002 swp31 fake-future-spine swp31 
connect UDCLAYN00002 swp32 fake-future-spine swp32 
connect BDCLAYN00001 swp11 SDCLAYN00001 swp31 
connect BDCLAYN00001 swp12 SDCLAYN00002 swp31 
connect BDCLAYN00001 swp27 fake-spine3 swp31 
connect BDCLAYN00001 swp28 fake-spine4 swp31 
connect BDCLAYN00002 swp11 SDCLAYN00001 swp32 
connect BDCLAYN00002 swp12 SDCLAYN00002 swp32 
connect BDCLAYN00002 swp27 fake-spine3 swp32 
connect BDCLAYN00002 swp28 fake-spine4 swp32 
connect BDCLAYN00001 swp15 BDCLAYN00002 swp15 
connect BDCLAYN00001 swp16 BDCLAYN00002 swp16 
connect BDCLAYN00001 swp1 fake-server6 swp1 
connect BDCLAYN00001 swp2 fake-server6 swp2 
connect BDCLAYN00001 swp3 fake-server6 swp3 
connect BDCLAYN00001 swp4 fake-server6 swp4 
connect BDCLAYN00001 swp5 fake-server6 swp5 
connect BDCLAYN00001 swp6 fake-server6 swp6 
connect BDCLAYN00001 swp8 fake-server6 swp8 
connect BDCLAYN00001 swp9 fake-server6 swp9 
connect BDCLAYN00001 swp10 fake-server6 swp9a 
connect BDCLAYN00001 swp13 fake-server6 swp10 
connect BDCLAYN00001 swp14 fake-server6 swp11 
connect BDCLAYN00001 swp17 fake-server6 swp14 
connect BDCLAYN00001 swp18 fake-server6 swp15 
connect BDCLAYN00001 swp19 fake-server6 swp16 
connect BDCLAYN00001 swp20 fake-server6 swp17 
connect BDCLAYN00001 swp21 fake-server6 swp18 
connect BDCLAYN00001 swp22 fake-server6 swp19 
connect BDCLAYN00001 swp24 fake-server6 swp21 
connect BDCLAYN00001 swp25 fake-server6 swp22 
connect BDCLAYN00001 swp26 fake-server6 swp23 
connect BDCLAYN00001 swp29 fake-server6 swp24 
connect BDCLAYN00001 swp30 fake-server6 swp25 
connect BDCLAYN00001 swp31 fake-server6 swp26 
connect BDCLAYN00001 swp32 fake-server6 swp27 
connect BDCLAYN00002 swp1 fake-server7 swp1 
connect BDCLAYN00002 swp2 fake-server7 swp2 
connect BDCLAYN00002 swp3 fake-server7 swp3 
connect BDCLAYN00002 swp4 fake-server7 swp4 
connect BDCLAYN00002 swp5 fake-server7 swp5 
connect BDCLAYN00002 swp6 fake-server7 swp6 
connect BDCLAYN00002 swp8 fake-server7 swp8 
connect BDCLAYN00002 swp9 fake-server7 swp9 
connect BDCLAYN00002 swp10 fake-server7 swp9a 
connect BDCLAYN00002 swp13 fake-server7 swp10 
connect BDCLAYN00002 swp14 fake-server7 swp11 
connect BDCLAYN00002 swp17 fake-server7 swp14 
connect BDCLAYN00002 swp18 fake-server7 swp15 
connect BDCLAYN00002 swp19 fake-server7 swp16 
connect BDCLAYN00002 swp20 fake-server7 swp17 
connect BDCLAYN00002 swp21 fake-server7 swp18 
connect BDCLAYN00002 swp22 fake-server7 swp19 
connect BDCLAYN00002 swp24 fake-server7 swp21 
connect BDCLAYN00002 swp25 fake-server7 swp22 
connect BDCLAYN00002 swp26 fake-server7 swp23 
connect BDCLAYN00002 swp29 fake-server7 swp24 
connect BDCLAYN00002 swp30 fake-server7 swp25 
connect BDCLAYN00002 swp31 fake-server7 swp26 
connect BDCLAYN00002 swp32 fake-server7 swp27 
connect BDCLAYN00001 swp7 RDCLAYN00001 swp1 
connect BDCLAYN00001 swp23 RDCLAYN00002 swp1 
connect BDCLAYN00002 swp7 RDCLAYN00001 swp2 
connect BDCLAYN00002 swp23 RDCLAYN00002 swp2 
connect RDCLAYN00001 swp3 fake-server8 swp1 
connect RDCLAYN00001 swp4 fake-server8 swp2 
connect RDCLAYN00001 swp5 fake-server8 swp3 
connect RDCLAYN00001 swp6 fake-server8 swp4 
connect RDCLAYN00001 swp7 fake-server8 swp5 
connect RDCLAYN00001 swp8 fake-server8 swp6 
connect RDCLAYN00001 swp9 fake-server8 swp7 
connect RDCLAYN00001 swp10 fake-server8 swp8 
connect RDCLAYN00001 swp11 fake-server8 swp9 
connect RDCLAYN00001 swp12 fake-server8 swp10 
connect RDCLAYN00001 swp13 fake-server8 swp11 
connect RDCLAYN00001 swp14 fake-server8 swp12 
connect RDCLAYN00001 swp15 fake-server8 swp13 
connect RDCLAYN00001 swp16 fake-server8 swp14 
connect RDCLAYN00001 swp17s0 fake-server8 swp15s0 
connect RDCLAYN00001 swp17s1 fake-server8 swp15s1 
connect RDCLAYN00001 swp17s2 fake-server8 swp15s2 
connect RDCLAYN00001 swp17s3 fake-server8 swp15s3 
connect RDCLAYN00001 swp18 fake-server8 swp16 
connect RDCLAYN00001 swp19 fake-server8 swp17 
connect RDCLAYN00001 swp20 fake-server8 swp18 
connect RDCLAYN00001 swp21 fake-server8 swp19 
connect RDCLAYN00001 swp22 fake-server8 swp20 
connect RDCLAYN00001 swp23 fake-server8 swp21 
connect RDCLAYN00001 swp24 fake-server8 swp22 
connect RDCLAYN00001 swp25 fake-server8 swp23 
connect RDCLAYN00001 swp26 fake-server8 swp24 
connect RDCLAYN00001 swp27 fake-server8 swp25 
connect RDCLAYN00001 swp28 fake-server8 swp26 
connect RDCLAYN00001 swp29 fake-server8 swp27 
connect RDCLAYN00001 swp30 fake-server8 swp28 
connect RDCLAYN00001 swp31 fake-server8 swp29 
connect RDCLAYN00001 swp32 fake-server8 swp30 
connect RDCLAYN00002 swp3 fake-server9 swp1 
connect RDCLAYN00002 swp4 fake-server9 swp2 
connect RDCLAYN00002 swp5 fake-server9 swp3 
connect RDCLAYN00002 swp6 fake-server9 swp4 
connect RDCLAYN00002 swp7 fake-server9 swp5 
connect RDCLAYN00002 swp8 fake-server9 swp6 
connect RDCLAYN00002 swp9 fake-server9 swp7 
connect RDCLAYN00002 swp10 fake-server9 swp8 
connect RDCLAYN00002 swp11 fake-server9 swp9 
connect RDCLAYN00002 swp12 fake-server9 swp10 
connect RDCLAYN00002 swp13 fake-server9 swp11 
connect RDCLAYN00002 swp14 fake-server9 swp12 
connect RDCLAYN00002 swp15 fake-server9 swp13 
connect RDCLAYN00002 swp16 fake-server9 swp14 
connect RDCLAYN00002 swp17s0 fake-server9 swp15s0 
connect RDCLAYN00002 swp17s1 fake-server9 swp15s1 
connect RDCLAYN00002 swp17s2 fake-server9 swp15s2 
connect RDCLAYN00002 swp17s3 fake-server9 swp15s3 
connect RDCLAYN00002 swp18 fake-server9 swp16 
connect RDCLAYN00002 swp19 fake-server9 swp17 
connect RDCLAYN00002 swp20 fake-server9 swp18 
connect RDCLAYN00002 swp21 fake-server9 swp19 
connect RDCLAYN00002 swp22 fake-server9 swp20 
connect RDCLAYN00002 swp23 fake-server9 swp21 
connect RDCLAYN00002 swp24 fake-server9 swp22 
connect RDCLAYN00002 swp25 fake-server9 swp23 
connect RDCLAYN00002 swp26 fake-server9 swp24 
connect RDCLAYN00002 swp27 fake-server9 swp25 
connect RDCLAYN00002 swp28 fake-server9 swp26 
connect RDCLAYN00002 swp29 fake-server9 swp27 
connect RDCLAYN00002 swp30 fake-server9 swp28 
connect RDCLAYN00002 swp31 fake-server9 swp29 
connect RDCLAYN00002 swp32 fake-server9 swp30 
