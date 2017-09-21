# bgp-peer

## What does this do:
bgp-peer uses Nekmiko (https://github.com/ktbyers/netmiko) which uses Paramiko SSH connections
to connect to Juniper and Cisco routers, issue a command, analyse output and run additional commands and collate findings.

## In short what does this do:
Output list of BGP neighbours that are currently down with their descriptions

## What use is this to me:
Helps spot BGP peering issues quickly to aid network troubleshooting

## How do I use bgp-peer:
Edit the script and enter your hostnames or IP addresses.
Run the program.
Enter your username and password.
Observe output and final BGP neighbors down summary.
