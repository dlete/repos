# Installation

Instructions are for `Ubuntu 16:04`

```bash
sudo apt-get -qq update
sudo apt-get -qq install python3-venv    # needed to create venv in 16.04. It is not needed in 18.04 and above.
```

Create virtual environment

```bash
python3 -m venv .venv
```

Upgrade `pip`

```bash
pip install --upgrade pip
```
