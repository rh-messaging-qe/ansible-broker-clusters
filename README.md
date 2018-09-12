AMQ Cluster deployments Playbook
=========

Deploys various JBoss AMQ 7 Broker clusters.

Requirements
------------

Requirements are present on the requirements.yml file. To install them:

```ansible-galaxy install -f -r requirements.yml```

Note: All roles in this repository depend on ansible-amq-broker role.

Playbook details
--------------

This project contains default playbook for JBoss AMQ 7 / Artemis, with specific group variables to
* single broker
* cluster
* high availability 
  * replication
  * shared store (JDBC/FileSystem)


Usage
--------------

Make sure this playbook can use `ansible-amq-broker` role.
Export needed system variables, for example for HA deployment:

```
export EXTERNAL_IP_MODE=True
export AMQ_BROKER_MASTER_NODES="10.0.0.1(172.0.0.1)"
export AMQ_BROKER_SLAVE_NODES="10.0.0.2(172.0.0.2)"

ansible-playbook ansible-broker-clusters/roles/custom-broker/provision.yml -i dynamic_inventory.py -u root -e @ansible-broker-clusters/roles/custom-broker/group_vars/amq_broker_defaults_ha.yml
```

Please see various configuration files in `group_vars` folder for different deployment types and `dynamic_inventory.py` for possible deployments.

`dynamic_inventory.py` files