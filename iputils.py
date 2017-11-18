#!/usr/bin/env python3
# encoding: UTF-8

import ipaddress
import unittest


def check(nets, addr):
    ip = ipaddress.ip_address(addr)
    for net in nets:
        if ip in set(ipaddress.ip_network(net).hosts()):
            return True
    return False


def subset(nets):
    return None


class AssignmentTest(unittest.TestCase):

    def test_check(self):
        network1 = "1.0.0.0/32"
        network2 = "192.168.1.0/24"
        networks = [network1, network2]
        self.assertTrue(check(networks, "192.168.1.2"))
        self.assertFalse(check(networks, "192.168.2.0"))

    def test_subset(self):
        network1 = "1.0.0.0/32"
        network2 = "192.168.1.0/24"
        network3 = "192.168.0.0/16"
        networks = [network1, network2, network3]
        expected = [network1, network3]
        self.assertEqual(subset(networks), expected)


if __name__ == "__main__":
    unittest.main()