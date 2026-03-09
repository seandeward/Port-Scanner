# __Auto Multi-Port Scanner__ - Overview
An automatic multi-port scanner. Enter FQDNs or hostnames into the local plaintext file (hostnames.txt), and it will check any open ports on those hostnames!

# How to Build and Run
This program can be run with a single Python file and the external plaintext file named "hostnames.txt". No special configurations or libraries necessary!

To run it, you only need to add hostnames to hostnames.txt (one name per line) and then run multi_port_scanner.py. The script will then rapidly test a socket connection through ports 1-10000.

### Configuration
To change which hosts you want scanned, edit the "hostnames.txt" file.
By default, the script will scan ports 1-10000. If you wish to scan a smaller, more defined list of ports, you can edit the "ports" variable near the top of "port_scanner.py".

# Detailed Script Process
__Here's the process:__
- Two variables are defined at the top: 
    - __hostnames_file_path__ - The file path for the required hostnames.txt file.
    - __default_timeout__ - The default timeout for the socket connections that test the ports (I've got it set to 0.001 seconds to make it fast, but feel free to adjust this as needed).
- multi_port_scanner.py opens the local text file (called hostnames.txt) and checks that there are hostnames inside of it.
- The __port_scan__ function is defined (more on that in a moment)
- For each hostname listed in hostnames.txt, the script will attempt to get its IP Address.
- If successful, the script then calls the __port_scan__ function for that host.
    - __port_scan__ contains a for loop where it opens and closes a socket connection on each port specified in the script.
    - If the connection is successful, a message is printed in the terminal notifying that the port is open.
- After all specified ports with all specified hostnames have been checked, the script ends.

### How do I make this go faster or slower? / I'm not getting any positives!
On line 9, you can adjust the amount of time each connection will take before it times out. I have it set to 0.001 seconds, but you can adjust this as you'd like.

# Rundown of Development Process
The big feature I wanted to learn was how to import a list from an external file and process it, which this script does. Another big feature that I learned about with this project was using sockets, which were easy to set up!

The only other issue I encountered was that the script was running very slowly; it took about a second for each port to be tested before it would time out. I was able to drastically speed this process up by changing the _setdefaulttimeout_ to 0.001 seconds.

Once I had those in place, the rest of the script was largely setting up variables and for loops.

# Wishlist of Future Features
### Create a CLI-only branch
- Create a branch where the user can check specified hosts by typing them into the command line rather than
- This version would use _argv_ from the _sys_ library to put each argument from the command line into the __port_scan__ function.

### Make It Into a Full-On Vulnerability Scanner
- This is the long-term result I want for this project- Making a vulnerability scanner that checks hosts against a database of vulnerabilities.
- To do this, the Nessus scanner web app will likely be a functional inspiration.

# Disclaimer
This script was built to be ethically used. This script was not created for any illegal activities.
