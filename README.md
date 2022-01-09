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