# Ansible playbook to generate SSL keys


This role creates Certificate Authority certificate and key on 'localhost' and signs per host specific certificate.
These signed certificates and private keys (along with Certificate Sign Request) are copied into given node.

See defaults variables for details like used password, locations, subject/issuer information etc.
```
ansible-galaxy install --roles-path . -f -r ansible-broker-clusters/playbooks/gen-ssl/requirements.yaml
```

```
ansible-playbook ansible-broker-clusters/playbooks/gen-ssl/provision.yml -i ansible-broker-clusters/dynamic-inventory.py -u root -e @ansible-broker-clusters/playbooks/gen-ssl/defaults/main.yml
```

TODO create a table with user provided variables.
