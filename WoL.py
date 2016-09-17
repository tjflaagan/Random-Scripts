from wakeonlan import wol

# Can setup a forwarded port on the router to make this work from outside the network
wol.send_magic_packet('MAC ADDRESS',
                       ip_address='IP/URL',
                       port=PORT)