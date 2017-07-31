AMQ HA shared-store replication playbook
=========

Deploys JBoss AMQ 7 Broker cluster with shared-store based replication.

Requirements
------------

This role depends on cluster role provided in this git repository and builds upon it
High Availability mode with shared-store replication.

Usage
-----
You can substitute inventory file by your own, but we expect same groups of hosts as in examples.

#### HA shared-store replication cluster
```ansible-playbook roles/ha-shared-store/provision.yml -i roles/ha-shared-store/inventory/deployment.yml -u root```
