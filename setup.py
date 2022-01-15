from setuptools import setup


setup(name='blockchain_lab',
version='0.4.0',
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
You can give path as a argument to blockchain_lab(path).
### Docker | Create & Delete
```python
from blockchain_lab import blockchain_lab

blockchain_lab().create_docker()
```
```python
from blockchain_lab import blockchain_lab

blockchain_lab().delete_docker()
```
### Local | Create & Delete
```python
from blockchain_lab import blockchain_lab

blockchain_lab().create_local()
```
```python
from blockchain_lab import blockchain_lab

blockchain_lab().delete_local()
```
### Status
```python
from blockchain_lab import blockchain_lab

blockchain_lab.status()
```
### Test with a transaction
```python
from blockchain_lab import blockchain_lab

blockchain_lab.send_transaction(receiver = "decentra_network", amount = 5000)
```


## In command line
You can give path as a parameter with -p or --path in create and delete.
### Docker | Create & Delete
```console
blockchain_lab_create_docker
```
```console
blockchain_lab_delete_docker
```
### Local | Create & Delete
```console
blockchain_lab_create_local
```
```console
blockchain_lab_delete_local
```
### Status
```console
blockchain_lab_status
```
### Test with a transaction
```console
blockchain_lab_send_transaction -r decentra_network -a 5000
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
        'blockchain_lab_create_docker=blockchain_lab.blockchain_lab:blockchain_lab_create_docker', 
        'blockchain_lab_create_local=blockchain_lab.blockchain_lab:blockchain_lab_create_local',
        "blockchain_lab_delete_docker=blockchain_lab.blockchain_lab:blockchain_lab_delete_docker",
        "blockchain_lab_delete_local=blockchain_lab.blockchain_lab:blockchain_lab_delete_local",
        "blockchain_lab_status=blockchain_lab.blockchain_lab:blockchain_lab.status",
        "blockchain_lab_send_transaction=blockchain_lab.blockchain_lab:blockchain_lab_send_transaction"
    ],
},
python_requires=">=3.6",
zip_safe=False)