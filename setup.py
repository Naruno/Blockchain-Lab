from setuptools import setup


setup(name='blockchain_lab',
version='0.2.0',
description="""A fully functional blockchain lab.""",
long_description="""
# Blockchain Lab
A fully functional blockchain lab.

# Install
```
pip3 install blockchain_lab
```
# Using
## In another script
```python
from blockchain_lab import blockchain_lab

blockchain_lab.create()
```
```python
from blockchain_lab import blockchain_lab

blockchain_lab.status()
```
```python
from blockchain_lab import blockchain_lab

blockchain_lab.send_transaction(receiver = "decentra_network", amount = 5000)
```
```python
from blockchain_lab import blockchain_lab

blockchain_lab.delete()
```
## In command line
```console
blockchain_lab_create
```
```console
blockchain_lab_status
```
```console
blockchain_lab_send_transaction -r decentra_network -a 5000
```
```console
blockchain_lab_delete
```
""",
long_description_content_type='text/markdown',
url='https://github.com/Decentra-Network/Blockchain-Lab',
author='Decentra Network Developers',
author_email='onur@decentranetwork.org',
license='MPL-2.0',
packages=["blockchain_lab"],
package_dir={'':'src'},
entry_points = {
    'console_scripts': [
        'blockchain_lab_create=blockchain_lab.blockchain_lab:blockchain_lab.create', 
        "blockchain_lab_delete=blockchain_lab.blockchain_lab:blockchain_lab.delete",
        "blockchain_lab_status=blockchain_lab.blockchain_lab:blockchain_lab.status",
        "blockchain_lab_send_transaction=blockchain_lab.blockchain_lab:blockchain_lab_send_transaction"
    ],
},
python_requires=">=3.6",
zip_safe=False)