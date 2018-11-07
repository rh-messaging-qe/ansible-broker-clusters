# Ansible playbook to generate SSL keys

Download needed ansible-jdk-installer role to roles playbooks/jdk-installer/roles/ directory and execute as follows
```
ansible-galaxy install --roles-path . -f -r ansible-broker-clusters/playbooks/gen-ssl/requirements.yaml
```

```
ansible-playbook ansible-broker-clusters/playbooks/jdk-installer/provision.yml -i ansible-broker-clusters/dynamic-inventory.py -u root
```

As this role is internal, you won't be able to use it in upstream