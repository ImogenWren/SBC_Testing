# ansible-scripting

Automating the updating of all SBCs on the LAN

## Method

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

Add your public SSH key to the `authorized_keys` file on each remote system.

Test the SSH connections, for example:

`ssh username@192.0.2.50`

5. Ping the managed nodes.

ansible all -m ping
