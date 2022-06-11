#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
import argparse
import os
import sys
import time

import requests


class blockchain_lab:

    def __init__(self,
                 node_number=3,
                 security_circle_number=1,
                 path=os.getcwd()):
        self.node_number = node_number
        self.security_circle_number = security_circle_number
        self.old_path = os.getcwd()
        self.path = path

    def create_docker(self):

        os.chdir(self.path)

        os.system(
            "git clone https://github.com/Decentra-Network/Decentra-Network")
        os.system("docker pull ghcr.io/decentra-network/api:latest")
        os.system(
            f"python3 Decentra-Network/auto_builders/docker.py -nn {self.node_number} -scn {self.security_circle_number} -i -r -s"
        )

        os.chdir(self.old_path)

    def create_local(self):

        os.chdir(self.path)

        if sys.platform != "linux":
            print("Local builded lab only available on Linux")
            return

        os.system(
            "git clone https://github.com/Decentra-Network/Decentra-Network")
        os.system(
            f"python3 Decentra-Network/auto_builders/local.py -nn {self.node_number} -scn {self.security_circle_number} -i -r -s"
        )

        os.chdir(self.old_path)

    def delete_docker(self):

        os.chdir(self.path)

        if sys.platform != "linux":
            print("Local builded lab only available on Linux")
            return

        os.system(
            f"python3 Decentra-Network/auto_builders/docker.py -nn {self.node_number} -scn {self.security_circle_number} -d"
        )

        os.chdir(self.old_path)

    def delete_local(self):

        os.chdir(self.path)

        os.system(
            f"python3 Decentra-Network/auto_builders/local.py -nn {self.node_number} -scn {self.security_circle_number} -d"
        )

        os.chdir(self.old_path)

    def status(self):
        print("Status of nodes: ")
        print(str(requests.get("http://localhost:8000/status").text))
        for i in range(self.node_number - 1):
            print("- " +
                  str(requests.get(f"http://localhost:{8100 + i + 1}/status").text))

    @staticmethod
    def send_transaction(receiver, amount, data):
        requests.get(
            f"http://localhost:8000/send/coin-data/{receiver}/{amount}/{data}/123"
        )
        time.sleep(15)
        result = requests.get(
            "http://localhost:8000/export/transactions/json").text

        print("Result of the transaction: ")
        print(result)


def blockchain_lab_create_docker():
    parser = argparse.ArgumentParser(
        description="Create blockchain lab with decentra-network-api docker.")

    parser.add_argument(
        "-nn",
        "--nodenumber",
        default=3,
        type=str,
        help="Give the node number to the blockchain lab",
    )
    parser.add_argument(
        "-scn",
        "--securitycirclenumber",
        default=1,
        type=str,
        help="Give the security circle number to the blockchain lab",
    )

    parser.add_argument(
        "-p",
        "--path",
        default=os.getcwd(),
        type=str,
        help="Give the path to the blockchain lab",
    )

    args = parser.parse_args()

    nodenumber = args.nodenumber
    securitycirclenumber = args.securitycirclenumber
    if args.path is not None:
        path = args.path

    blockchain_lab(node_number=nodenumber,
                   security_circle_number=securitycirclenumber,
                   lab_path=path).create_docker()


def blockchain_lab_create_local():
    parser = argparse.ArgumentParser(
        description="Create blockchain lab with local system.")

    parser.add_argument(
        "-nn",
        "--nodenumber",
        default=3,
        type=str,
        help="Give the node number to the blockchain lab",
    )
    parser.add_argument(
        "-scn",
        "--securitycirclenumber",
        default=1,
        type=str,
        help="Give the security circle number to the blockchain lab",
    )

    parser.add_argument(
        "-p",
        "--path",
        default=os.getcwd(),
        type=str,
        help="Give the path to the blockchain lab",
    )

    args = parser.parse_args()

    nodenumber = args.nodenumber

    securitycirclenumber = args.securitycirclenumber

    path = args.path

    blockchain_lab(node_number=nodenumber,
                   security_circle_number=securitycirclenumber,
                   path=path).create_local()


def blockchain_lab_delete_docker():
    parser = argparse.ArgumentParser(
        description="Delete blockchain lab with decentra-network-api docker.")

    parser.add_argument(
        "-nn",
        "--nodenumber",
        default=3,
        type=str,
        help="Give the node number to the blockchain lab",
    )
    parser.add_argument(
        "-scn",
        "--securitycirclenumber",
        default=1,
        type=str,
        help="Give the security circle number to the blockchain lab",
    )

    parser.add_argument(
        "-p",
        "--path",
        default=os.getcwd(),
        type=str,
        help="Give the path to the blockchain lab",
    )

    args = parser.parse_args()

    nodenumber = args.nodenumber

    securitycirclenumber = args.securitycirclenumber

    path = args.path

    blockchain_lab(node_number=nodenumber,
                   security_circle_number=securitycirclenumber,
                   path=path).delete_docker()


def blockchain_lab_delete_local():
    parser = argparse.ArgumentParser(
        description="Delete blockchain lab with local system.")

    parser.add_argument(
        "-nn",
        "--nodenumber",
        default=3,
        type=str,
        help="Give the node number to the blockchain lab",
    )
    parser.add_argument(
        "-scn",
        "--securitycirclenumber",
        default=1,
        type=str,
        help="Give the security circle number to the blockchain lab",
    )

    parser.add_argument(
        "-p",
        "--path",
        default=os.getcwd(),
        type=str,
        help="Give the path to the blockchain lab",
    )

    args = parser.parse_args()

    nodenumber = args.nodenumber

    securitycirclenumber = args.securitycirclenumber

    path = args.path

    blockchain_lab(node_number=nodenumber,
                   security_circle_number=securitycirclenumber,
                   path=path).delete_local()


def blockchain_lab_status():
    parser = argparse.ArgumentParser(
        description="Get the status of blockchain lab.")

    parser.add_argument(
        "-nn",
        "--nodenumber",
        default=3,
        type=str,
        help="Give the node number to the blockchain lab",
    )

    args = parser.parse_args()

    nodenumber = args.nodenumber


    blockchain_lab(node_number=nodenumber).status()


def blockchain_lab_send_transaction():
    parser = argparse.ArgumentParser(
        description="A fully functional blockchain lab.")

    parser.add_argument(
        "-r",
        "--receiver",
        default="DecentraNetworkCommunity",
        type=str,
        help="Give the receiver adress",
    )
    parser.add_argument("-a",
                        "--amount",
                        default=5000,
                        type=str,
                        help="Give the amount")
    parser.add_argument("-d",
                        "--data",
                        default="blockchain-lab",
                        type=str,
                        help="Give the data")

    args = parser.parse_args()

    blockchain_lab.send_transaction(args.receiver, args.amount, args.data)
