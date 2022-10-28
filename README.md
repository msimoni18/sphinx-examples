# sphinx-examples

Simple sphinx docs with examples
## Create the environment

In the top-level directory, run:

```{bash}
python3 -m venv venv
```

```{bash}
pip3 install -r requirements.txt
```

```{bash}
source venv/bin/activate
```

# Build docs

In ``doc/``, run:

```{bash}
make clean html
```
