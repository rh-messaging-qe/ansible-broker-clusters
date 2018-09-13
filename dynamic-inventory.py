#!/usr/bin/env python

# This module uses system variables to define how dynamic inventory will be created.
# Following environment are used
#  EXTERNAL_IP_MODE [True|False] - whether use both ip addresses 'external_ip(internal_ip)' format
# AMQ_BROKER_SINGLE_NODE='external_ip' - single broker, same inventory like for cluster
# AMQ_BROKER_CLUSTER_NODES='external_ip1 external_ip2 external_ipN...'
# AMQ_BROKER_MASTER_NODES='..defined same as CLUSTER_NODES..' applicable to HA master deployment
# AMQ_BROKER_SLAVE_NODES='..defined same as CLUSTER_NODES..' applicable to HA slave deployment
import ast
import os
import re
import argparse
import pprint

EXTERNAL_IP_MODE = "EXTERNAL_IP_MODE"
AMQ_BROKER_SINGLE_NODE = None
AMQ_BROKER_CLUSTER_NODES = "AMQ_BROKER_CLUSTER_NODES"  # "10.0.0.1(172.0.0.1) 10.0.0.2(172.0.0.2) 10.0.0.3(172.0.0.3) 10.0.0.4(172.0.0.4)"
AMQ_BROKER_MASTER_NODES = "AMQ_BROKER_MASTER_NODES"    # "10.0.0.1(172.0.0.1) 10.0.0.2(172.0.0.2)"
AMQ_BROKER_SLAVE_NODES = "AMQ_BROKER_SLAVE_NODES"      # "10.0.0.3(172.0.0.3) 10.0.0.4(172.0.0.4)"

IP_BOTH_PATTERN = r'(.*)\((.*)\)'

# AMQ_BROKER_CLUSTER_INVENTORY || AMQ_BROKER_SINGLE_NODE
# [broker]
# <cluster_node> [amq_broker_external_address]
AMQ_BROKER_CLUSTER_INVENTORY = {
    "_meta": {
            "hostvars": {}
        },
    "broker": {
        "hosts": [],
        "vars": {}
    }
}

# AMQ_BROKER_HA_INVENTORY
# [broker:children]
# master
# slave
#
# [master]
# <master_node> [amq_broker_external_address]
#
# [slave]
# <slave_node> [amq_broker_external_address]
AMQ_BROKER_HA_INVENTORY = \
    {
        "_meta": {
            "hostvars": {}
        },
        "broker": {
            "hosts": [],
            "vars": {},
            "children": ["master", "slave"]
        },
        "master": {
            "hosts": [],
            "vars": {},
        },
        "slave": {
            "hosts": [],
            "vars": {},
        }
    }


def to_bool(value):
    if value.lower() in ['true', '1', 't', 'y', 'yes']:
        return True
    else:
        return False


class Inventory():

    def __init__(self):
        self.args = None
        self.inventory = {}
        self.read_cli_args()
        self.external_ip_mode = to_bool(os.getenv(EXTERNAL_IP_MODE, False))

        self.check_valid_environment_vars()

        if os.getenv(AMQ_BROKER_MASTER_NODES) is not None or os.getenv(AMQ_BROKER_SLAVE_NODES):
            self.populate_inventory_ha()
        elif os.getenv(AMQ_BROKER_CLUSTER_NODES):
            self.populate_inventory_cluster()
        else:
            self.inventory = Inventory.empty_inventory()

        if self.args.list:
            print self.inventory
        elif self.args.host:
            print self.inventory['_meta']
        elif self.args.debug:
            pprint.pprint(self.inventory)
        else:
            self.inventory = Inventory.empty_inventory()

    def __str__(self):
        return str(self.inventory)

    def check_valid_environment_vars(self):
        if os.getenv(AMQ_BROKER_MASTER_NODES) is not None and os.getenv(AMQ_BROKER_SLAVE_NODES) and \
                os.getenv(AMQ_BROKER_CLUSTER_NODES) is not None:
            print "Error, defined too many env variables. Unable to continue"
            exit(2)

    def populate_inventory_single(self):
        self.inventory = AMQ_BROKER_CLUSTER_INVENTORY

    def populate_inventory_cluster(self):
        self.inventory = AMQ_BROKER_CLUSTER_INVENTORY
        self.populate_inventory(os.getenv(AMQ_BROKER_CLUSTER_NODES), "broker")

    def populate_inventory_ha(self):
        self.inventory = AMQ_BROKER_HA_INVENTORY
        self.populate_inventory(os.getenv(AMQ_BROKER_MASTER_NODES), "master")
        self.populate_inventory(os.getenv(AMQ_BROKER_SLAVE_NODES), "slave")

    def populate_inventory(self, nodes, node_key):
        for node in nodes.split(" "):
            external_ip = node
            internal_ip = None
            if "(" in node:
                found = re.search(IP_BOTH_PATTERN, node)
                if found:
                    external_ip = found.group(1)
                    internal_ip = found.group(2)

            self.inventory.get(node_key).get('hosts').append(external_ip)
            self.inventory.get(node_key).get('vars')['ansible_user'] = 'root'

            if self.external_ip_mode is False:
                self.inventory.get('_meta').get('hostvars')[external_ip] = {}
            else:
                self.inventory.get('_meta').get('hostvars')[external_ip] = {'amq_broker_external_address': internal_ip}

    @staticmethod
    def empty_inventory():
        return {'_meta': {'hostvars': {}}}

    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action='store_true')
        parser.add_argument('--host', action='store_true')
        parser.add_argument('--debug', action='store_true')
        self.args = parser.parse_args()


def main():
    """Main function to execute dynamic inventory """
    my_inventory = Inventory()

if __name__ == '__main__':
    main()
