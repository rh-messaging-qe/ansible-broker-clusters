AMQ Cluster deployments Playbook
=========

Deploys various JBoss AMQ 7 Broker clusters.
Simple cluster deployment or high availability with replication, shared store or collocated.

Requirements
------------

Requirements are present on the requirements.yml file. To install them:

```ansible-galaxy install -f -r requirements.yml```

Note: All roles in this repository depend on amq-broker role.

Playbook details
--------------

This project contains default clustering playbooks for JBoss AMQ 7 / Artemis.
Playbooks are in *roles* directory:

* *cluster*: default basic settings for broadcast & discovery of brokers
* *ha-replication*: reuses *cluster* role and sets replication on master/slave nodes
* *ha-sharedstore*: TODO


Usage
--------------

For details about usage please see README.md in given roles.
