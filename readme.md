# bgp-peer

## What does this do:
bgp-peer uses Nekmiko (https://github.com/ktbyers/netmiko) which in turn utilises Paramiko SSH connections
to connect to Juniper and Cisco routers, issue a command, analyse output and run additional commands and collate findings.<br>
This script will return a list of BGP neighbours accociated with hosts defined in `device-list.txt` 

## In short what does this do:
Output a list of BGP neighbours with their current state and detail all non establised peers.

## What use is this to me:
- Highlights BGP peering issues to aid network troubleshooting.
- Quick network-wide audit of current BGP neighbourships.

## How do I use bgp-peer:
- Enter your device hostnames or IP addresses into `device-list.txt`
- Run the script: `python bgp-peer.py`
- Enter your common username and password.
- Observe output and final BGP neighbours down summary.
