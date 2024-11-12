
# TianGongLCA-Matrix

## Env Preparing

Install `Python 3.12`

```bash
sudo apt update
sudo apt install python3.12
```

Setup `venv`:

```bash
sudo apt install python3.12-venv
python3.12 -m venv .venv
source .venv/bin/activate
```

Install requirements:

```bash
pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r requirements.txt --upgrade
```

Run:
```bash
watch -n 1 nvidia-smi
```
