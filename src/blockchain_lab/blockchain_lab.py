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

    def __init__(self, path=os.getcwd()):
        self.old_path = os.getcwd()
        self.path = path

    def create_docker(self):

        os.chdir(self.path)

        os.system("git clone https://github.com/Decentra-Network/Decentra-Network")
        os.system("docker pull ghcr.io/decentra-network/api:latest")
        os.system("python3 Decentra-Network/auto_builders/docker.py -nn 3 -i -r -s")

        os.chdir(self.old_path)

    def create_local(self):

        os.chdir(self.path)

        if sys.platform != "linux":
            print("Local builded lab only available on Linux")
            return

        os.system("git clone https://github.com/Decentra-Network/Decentra-Network")
        os.system("python3 Decentra-Network/auto_builders/local.py -nn 3 -i -r -s")

        os.chdir(self.old_path)

    def delete_docker(self):

        os.chdir(self.path)

        if sys.platform != "linux":
            print("Local builded lab only available on Linux")
            return        

        os.system("python3 Decentra-Network/auto_builders/docker.py -nn 3 -d")

        os.chdir(self.old_path)

    def delete_local(self):

        os.chdir(self.path)

        os.system("python3 Decentra-Network/auto_builders/local.py -nn 3 -d")
        
        os.chdir(self.old_path)

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


def blockchain_lab_create_docker():
    parser = argparse.ArgumentParser(
        description="Create blockchain lab with decentra-network-api docker."
    )

    parser.add_argument("-p", "--path", type=str, help="Give the path to the blockchain lab")

    args = parser.parse_args()

    if len(sys.argv) < 2:
        blockchain_lab().create_docker()
    else:
        blockchain_lab(args.path).create_docker()


def blockchain_lab_create_local():
    parser = argparse.ArgumentParser(
        description="Create blockchain lab with local system."
    )

    parser.add_argument("-p", "--path", type=str, help="Give the path to the blockchain lab")

    args = parser.parse_args()

    if len(sys.argv) < 2:
        blockchain_lab().create_local()
    else:
        blockchain_lab(args.path).create_local()

def blockchain_lab_delete_docker():
    parser = argparse.ArgumentParser(
        description="Delete blockchain lab with decentra-network-api docker."
    )

    parser.add_argument("-p", "--path", type=str, help="Give the path to the blockchain lab")

    args = parser.parse_args()

    if len(sys.argv) < 2:
        blockchain_lab().delete_docker()
    else:
        blockchain_lab(args.path).delete_docker()


def blockchain_lab_delete_local():
    parser = argparse.ArgumentParser(
        description="Delete blockchain lab with local system."
    )

    parser.add_argument("-p", "--path", type=str, help="Give the path to the blockchain lab")

    args = parser.parse_args()

    if len(sys.argv) < 2:
        blockchain_lab().delete_local()
    else:
        blockchain_lab(args.path).delete_local()


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