AMQ Cluster Playbook
=========

Deploys JBoss AMQ 7 Broker cluster on provided hosts.

Requirements
------------

Requirements are present on the requirements.yml file. To install them:

```ansible-galaxy install -f -r requirements.yml```

This playbook depends on ansible amq-broker role provided in *msgqe/ansible-amq-broker* git repository.

Playbook details
--------------

* *provision-broker.yml*: to install, configure and create clustered broker instances.
* *provision.yml*: to install a whole system from scratch (both the host and the broker).


Usage
--------------

You can substitute inventory file by your own, but we expect same groups of hosts as in examples.

```ansible-playbook roles/cluster/provision.yml -i roles/cluster/inventory/deployment.yml -u root```
