### Summary:

Quick dynamic ansible inventory using nmap and constructor plugins to discover devices. Useful for homelab.

### Environment:

* Ansible 2.9.27
* Fedora 35 Physical Host
* Gnomes Boxes based controllers/managed VMs running Rockly Linux 8.5
* All managed nodes on 192.168.122.0/24

### Gnomes Boxes VM Sumamry:
* controller
* node{01..05}

### Assumptions:
* All commands executed from this directory so ansible.cfg settings are picked up. 
* Basic knowldge of Ansible

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
            "trash01": {
                "ip": "192.168.122.145",
                "ports": []
            },
            "trash02": {
                "ip": "192.168.122.159",
                "ports": []
            },
            "trash03": {
                "ip": "192.168.122.164"
            },
            "trash04": {
                "ip": "192.168.122.96",
                "ports": []
            },
            "trash05": {
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
            "trash05"
        ]
    },
    "proxy": {
        "hosts": [
            "trash01",
            "trash02"
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
            "trash04"
        ]
    }
}
```


