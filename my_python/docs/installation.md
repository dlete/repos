# Installation

Instructions are for `Ubuntu 16:04`

```bash
sudo apt-get -qq update
sudo apt-get -qq install python3-venv    # needed to create venv
```

Create virtual environment

```bash
python3 -m venv .venv
```

Activate the virtual environment

```bash
source .venv/bin/activate
```

Upgrade `pip`

```bash
pip install --upgrade pip
```
