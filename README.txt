--------------------------------------- SUBNETTING CALCULATOR ---------------------------------------

name:	Ofir Haruvi

-----------------------------------------------------------------------------------------------------

The program is designed to facilitate the study process by leveraging binary conversion. 

Initially, the user inputs an IP address and a prefix. The program then displays the IP address 
and the subnet mask in both decimal and binary formats, with each displayed exactly above the other. 
This presentation allows the user to discern which octets and bits remain constant for the network 
ID and the broadcast address, and which will vary.

In the subsequent step, the user can compute the decimal value of the octets that will change by 
converting their new values from binary to decimal (For the network ID the free bits are all set 
to 0, while for the broadcast address, they are set to 1)

Upon calculation, the user enters their network ID result. If incorrect, they have the option to try 
again or return to the calculation phase.

The same process is then repeated for the broadcast address.
