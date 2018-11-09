# Ansible playbook to download and install various messaging clients

Download (link) needed ansible-messaging-clients role to roles playbooks/jdk-installer/roles/ directory and execute as follows
```
ansible-galaxy install --roles-path ./roles/ -f -r ansible-broker-clusters/playbooks/ansible-messaging-clients/requirements.yaml
```

```
ansible-playbook ansible-broker-clusters/playbooks/ansible-messaging-clients/provision.yml -i ansible-broker-clusters/dynamic-inventory.py -u root
```

As this role is internal, you won't be able to use it in upstream