# BGP-ASN

Collects all ip ranges from [bgp.he.net](https://bgp.he.net) of a given ASN.

## Usage

- Run this if you want to add to path:
```bash
chmod +x bgpasn.py
sudo ln -s $(pwd)/bgpasn.py /usr/bin/bgpasn
```

- Retrieves IP ranges from ASN:
```bash
bgpasn -a <ASXXXX> # Enter the ASN number here

# Also accepts input from stdin
echo "<ASXXXX>" | bgpasn
```

- To include IPv6 ranges in the output add the `-v6` flag
```bash
bgpasn -a <ASXXXX> -v6
```

**Note:** The tool will copy all the output to system clipboard by default. 

