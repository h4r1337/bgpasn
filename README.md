# BGP-ASN

Collects all ip ranges from [bgp.he.net](https://bgp.he.net) of a given ASN.

## Usage

- Run this if you want to add to path:

```bash
chmod +x bgpasn.py
sudo ln -s $(pwd)/bgspan.py /usr/bin/bgspan
```

```bash
bgspan -a <ASXXXX> # Enter the ASN number here

# Also accepts input from stdin
echo "<ASXXXX>" | bgspan
```

**Note:** The tool will copy all the output to system clipboard by default. 

