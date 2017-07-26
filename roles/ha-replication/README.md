AMQ HA Replication Playbook
=========

Deploys JBoss AMQ 7 Broker cluster with replication set on provided hosts.

Requirements
------------

This role depends on cluster role provided in this git repository and builds upon it
High Availability mode with Replication.

Usage
-----
You can substitute inventory file by your own, but we expect same groups of hosts as in examples.

#### HA Replication cluster
```ansible-playbook roles/ha-replication/provision.yml -i roles/ha-replication/inventory/deployment.yml -u root```
