# Blockchain Lab
A fully functional blockchain lab.

# Install
```
pip3 install blockchain_lab
```
# Using
## In another script
### Docker | Create & Delete
```python
from blockchain_lab import blockchain_lab

blockchain_lab.create_docker()
```
```python
from blockchain_lab import blockchain_lab

blockchain_lab.delete_docker()
```
### Local (Not Recommended) | Create
```python
from blockchain_lab import blockchain_lab

blockchain_lab.create_local()
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

### Docker | Create & Delete
```console
blockchain_lab_create_docker
```
```console
blockchain_lab_delete_docker
```
### Local (Not Recommended) | Create
```console
blockchain_lab_create_local
```
### Status
```console
blockchain_lab_status
```
### Test with a transaction
```console
blockchain_lab_send_transaction -r decentra_network -a 5000
```