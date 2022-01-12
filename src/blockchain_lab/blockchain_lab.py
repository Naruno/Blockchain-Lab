#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.


import argparse
import os
import sys
import requests
import time



class blockchain_lab:

    @staticmethod
    def create_docker():
        os.system("git clone https://github.com/Decentra-Network/Decentra-Network")
        os.system("docker pull ghcr.io/decentra-network/api:latest")
        os.system("python3 Decentra-Network/auto_builders/docker.py -nn 3 -i -r -s")

    @staticmethod
    def create_local():
        os.system("git clone https://github.com/Decentra-Network/Decentra-Network")
        os.system("python3 Decentra-Network/auto_builders/local.py -nn 3 -i -r -s")

    @staticmethod
    def delete_docker():
        os.system("python3 Decentra-Network/auto_builders/docker.py -nn 3 -d")

    @staticmethod
    def delete_local():
        os.system("python3 Decentra-Network/auto_builders/local.py -nn 3 -d")

    @staticmethod
    def status():
        node_1_status = requests.get("http://localhost:8000/status").text
        node_2_status = requests.get("http://localhost:8010/status").text
        node_3_status = requests.get("http://localhost:8020/status").text

        print("Status of nodes: ")
        print(f"- {node_1_status}")
        print(f"- {node_2_status}")
        print(f"- {node_3_status}")

    @staticmethod
    def send_transaction(receiver, amount):
        requests.get(f"http://localhost:8000/send/coin/{receiver}/{amount}/123")
        time.sleep(15)
        result = requests.get("http://localhost:8000/export/transactions/json").text

        print("Result of the transaction: ")
        print(result)



def blockchain_lab_send_transaction():
    parser = argparse.ArgumentParser(
        description="A fully functional blockchain lab."
    )

    parser.add_argument("-r", "--receiver", type=str, help="Give the receiver adress")
    parser.add_argument("-a", "--amount", type=str, help="Give the amount")

    args = parser.parse_args()

    if len(sys.argv) < 3:
        print("Please give the receiver (-r) adress and amount (-a)")
    else:
        blockchain_lab.send_transaction(args.receiver, args.amount) 