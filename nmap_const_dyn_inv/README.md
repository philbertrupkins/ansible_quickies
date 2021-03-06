### Summary:

Quick dynamic ansible inventory using nmap and constructed plugins to discover devices. Useful for homelab.  Tweak as needed for your environment. Both the nmap and constructor plugins are part of the ansible core package.  

### Important Files:
* ansible.cfg
* inventory/10_nmap_inventory.yml
* inventory/20_nmap_constructed.yml

### Environment:

* Ansible 2.9.27
* Fedora 35 Physical Host
* Gnomes Boxes based controllers/managed VMs running Rockly Linux 8.5
* All managed nodes on 192.168.122.0/24

### Gnomes Boxes VM Summary:
* controller
* node{01..05}

### Assumptions:
* All commands executed from this directory so ansible.cfg settings are picked up. 
* Basic knowldge of Ansible
* Managed nodes allow port 80 from controller node.  

### Firewalld (sub your controller ip address)
Perform the following on each managed node to allow traffic over port 80 from the controller node.  This is required in order for nmap to discover the hosts.  See nmap discovery overview for more info - link in References section below. Make sure "source address" is changed to the IP of your controller node.  
```
# firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.122.36" port protocol="tcp" port="80" accept'
# firewall-cmd --reload
```
### References:
* https://stackoverflow.com/questions/61826110/dynamic-inventory-groups-from-ansible-plugin-nmap
* https://nmap.org/docs/discovery.pdf

### Expected Output:
```
$ ansible-inventory --list

{
    "_meta": {
        "hostvars": {
            "controller": {
                "ip": "192.168.122.36",
                "ports": []
            },
            "fedora": {
                "ip": "192.168.122.1",
                "ports": []
            },
            "node01": {
                "ip": "192.168.122.145",
                "ports": []
            },
            "node02": {
                "ip": "192.168.122.159",
                "ports": []
            },
            "node03": {
                "ip": "192.168.122.164"
            },
            "node04": {
                "ip": "192.168.122.96",
                "ports": []
            },
            "node05": {
                "ip": "192.168.122.68",
                "ports": []
            }
        }
    },
    "all": {
        "children": [
            "database",
            "proxy",
            "ungrouped",
            "webserver"
        ]
    },
    "database": {
        "hosts": [
            "node05"
        ]
    },
    "proxy": {
        "hosts": [
            "node01",
            "node02"
        ]
    },
    "ungrouped": {
        "hosts": [
            "controller",
            "fedora"
        ]
    },
    "webserver": {
        "hosts": [
            "node03",
            "node04"
        ]
    }
}
```


