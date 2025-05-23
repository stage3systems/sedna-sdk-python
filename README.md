# sedna-sdk-python

`sedna-sdk-python` is a lightweight internal Python SDK for interacting with the Sedna API. It provides an easy interface to authenticate and work with core Sedna resources like templates, messages, and more.

## 📦 Installation

To install via GitHub SSH, add the following line to your `requirements.txt`:

```

git+ssh://git\@github.com/stage3systems/sedna-sdk-python.git\@main#egg=sedna\_sdk

````

Make sure your SSH keys are set up correctly and you have access to the repository.

---

## 🚀 Getting Started

```python
from sedna_sdk.sedna_client import SednaClient

sedna_client = SednaClient(
    subdomain=sedna_tenant_name,
    client_id=sedna_api_username,
    client_secret=sedna_api_password
)
````

Once authenticated, you can interact with the API like so:

```python
# List available templates
templates = sedna_client.templates.list()
```

---

## 🔑 Authentication

`SednaClient` requires:

* `subdomain`: your tenant's subdomain on Sedna
* `client_id`: your API username
* `client_secret`: your API password

All credentials should be passed during initialization.

---

## 📚 Features

* Internal Python SDK for Sedna API
* Simple access to resources like templates
* Designed for integration in internal systems

---

## 🧪 Example Use Case

```python
# Fetch and print all templates
for template in sedna_client.templates.list():
    print(template["name"])
```
