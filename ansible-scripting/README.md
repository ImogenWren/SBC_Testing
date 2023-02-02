# ansible-scripting

## Poorly documented but easier to follow guide
https://crunchify.com/ansible-how-to-execute-commands-on-remote-hosts-and-get-complete-result-response-result-log-back/

Automating the updating of all SBCs on the LAN

Source: https://docs.ansible.com/ansible/latest/playbook_guide/index.html

## Issues?
https://stackoverflow.com/questions/53205687/ansible-unable-to-parse-etc-ansible-hosts-as-an-inventory-source

## Getting Started

1. Install Ansible. Visit the installation guide for complete details.

`python3 -m pip install --user ansible`


2. Create an inventory by adding the IP address or fully qualified domain name (FQDN) of one or more remote systems to /etc/ansible/hosts. The following example adds the IP addresses of three virtual machines in KVM:

```
[myvirtualmachines]
192.0.2.50
192.0.2.51
192.0.2.52
```

3. Verify the hosts in your inventory.

`ansible all --list-hosts`

4. Set up SSH connections so Ansible can connect to the managed nodes.

https://www.geekyhacker.com/2021/02/15/configure-ssh-key-based-authentication-on-raspberry-pi/#:~:text=SSH%20to%20your%20Raspberry%20Pi,That's%20the%20public%20key%20file.

Add your public SSH key to the `authorized_keys` file on each remote system.

Test the SSH connections, for example:

`ssh username@192.0.2.50`

5. Ping the managed nodes.

`ansible all -m ping`

## Inventory
_In the previous section, you added managed nodes directly to the /etc/ansible/hosts file. Now let’s create an inventory file that you can add to source control for flexibility, reuse, and for sharing with other users._

Inventory files can be in INI or YAML format.

Complete the following steps:

1. Open a terminal window on your control node.

2. Create a new inventory file named `inventory.yaml` in any directory and open it for editing.

3. Add a new group for your hosts then specify the IP address or fully qualified domain name (FQDN) of each managed node with the `ansible_host` field. The following example adds the IP addresses of three virtual machines in KVM:
```
virtualmachines:
  hosts:
    vm01:
      ansible_host: 192.0.2.50
    vm02:
      ansible_host: 192.0.2.51
    vm03:
      ansible_host: 192.0.2.52
```
4. Verify your inventory. If you created your inventory in a directory other than your home directory, specify the full path with the -i option.
`ansible-inventory -i inventory.yaml --list`

5. Ping the managed nodes in your inventory. In this example, the group name is virtualmachines which you can specify with the ansible command instead of all.

`ansible virtualmachines -m ping -i inventory.yaml`
```
vm03 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
vm02 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
vm01 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
```
Congratulations! You have successfully built an inventory.

Tips for building inventories
Ensure that group names are meaningful and unique. Group names are also case sensitive.

Avoid spaces, hyphens, and preceding numbers (use floor_19, not 19th_floor) in group names.

Group hosts in your inventory logically according to their What, Where, and When.

What
Group hosts according to the topology, for example: db, web, leaf, spine.

Where
Group hosts by geographic location, for example: datacenter, region, floor, building.

When
Group hosts by stage, for example: development, test, staging, production.

### Use metagroups
Create a metagroup that organizes multiple groups in your inventory with the following syntax:
```
metagroupname:
  children:
  ```
The following inventory illustrates a basic structure for a data center. This example inventory contains a network metagroup that includes all network devices and a datacenter metagroup that includes the network group and all webservers.
```
leafs:
  hosts:
    leaf01:
      ansible_host: 192.0.2.100
    leaf02:
      ansible_host: 192.0.2.110

spines:
  hosts:
    spine01:
      ansible_host: 192.0.2.120
    spine02:
      ansible_host: 192.0.2.130

network:
  children:
    leafs:
    spines:

webservers:
  hosts:
    webserver01:
      ansible_host: 192.0.2.140
    webserver02:
      ansible_host: 192.0.2.150

datacenter:
  children:
    network:
    webservers:
Create variables
Variables set values for managed nodes, such as the IP address, FQDN, operating system, and SSH user, so you do not need to pass them when running Ansible commands.

Variables can apply to specific hosts.

webservers:
  hosts:
    webserver01:
      ansible_host: 192.0.2.140
      http_port: 80
    webserver02:
      ansible_host: 192.0.2.150
      http_port: 443
Variables can also apply to all hosts in a group.

webservers:
  hosts:
    webserver01:
      ansible_host: 192.0.2.140
      http_port: 80
    webserver02:
      ansible_host: 192.0.2.150
      http_port: 443
  vars:
    ansible_user: my_server_user
```

