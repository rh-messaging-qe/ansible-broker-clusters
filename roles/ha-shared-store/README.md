AMQ HA shared-store replication playbook
=========

Deploys JBoss AMQ 7 Broker cluster with shared-store based replication.

Requirements
------------

This role depends on cluster role provided in this git repository and builds upon it
High Availability mode with shared-store replication.

Variables
------------

| Name              | Default Value       | Description          |
|-------------------|---------------------|----------------------|
|amq_broker_cluster_broadcast_group_name | my-broadcast-group | name of broadcasting group |
|amq_broker_cluster_broadcast_group_address | 231.7.7.7 | broadcast IP |
|amq_broker_cluster_broadcast_group_port | 9876 | broadcasting prot |
|amq_broker_cluster_discovery_group_name | my-discovery-group | discovery group name |
|amq_broker_cluster_name | my-cluster | cluster name |
|amq_broker_nfs_server | - | NFS server hostname or IP, e.g. nfs-share-example.com |
|amq_broker_remote_nfs_path | - | exported NFS path, e.g./tmp/scratch |
|amq_broker_local_nfs_mount_path | - | local mount point, e.g. /tmp/scratch |
|amq_broker_local_shared_store_base_path | - | subdir for creating brokers pairs shared stores, e.g. "{{ amq_broker_local_nfs_mount_path }}/shared-store" |
|amq_broker_nfs_mount_options | - | NFS mount options, e.g. "rw,sync,intr,noac,soft,lookupcache=none" |

Usage
-----
You can substitute inventory file by your own, but we expect same groups of hosts as in examples.

#### HA shared-store replication cluster
```ansible-playbook roles/ha-shared-store/provision.yml -i roles/ha-shared-store/inventory/deployment.yml -u root```

