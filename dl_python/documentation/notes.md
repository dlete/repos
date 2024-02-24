# My notes

## Compile Python module

See the question in Stackoverflow: [how to compile python script](https://stackoverflow.com/questions/52478939/how-to-compile-python-program-convert-to-pyc-in-python3)

```bash
import py_compile
py_compile.compile("file.py")
```

## How to solve: `Could not open a connection to your authentication agent` when using ssh-add

* start the ssh-agent in the background

```bash
$ eval "$(ssh-agent -s)"
> Agent pid 59566
```

* And then add the key:

```bash
$ ssh-add ~/.ssh/id_rsa
Enter passphrase for /home/dlete/.ssh/id_rsa:
Identity added: /home/dlete/.ssh/id_rsa (/home/dlete/.ssh/id_rsa)
```

See this [article](https://www.rockyourcode.com/ssh-agent-could-not-open-a-connection-to-your-authentication-agent-with-fish-shell/)

## Push to git repository

```bash
git push -u origin master
git push -u origin --all
git push -u origin --tags
```

## Nice to knows

### enums

[Enums](https://medium.com/better-programming/3-neglected-features-in-python-3-that-everyone-should-be-using-65cffc96f235)

### f strings

[fstrings](https://medium.com/better-programming/3-neglected-features-in-python-3-that-everyone-should-be-using-65cffc96f235)

## Markdown tricks

### Style and sytax

<https://docs.github.com/en/free-pro-team@latest/github/writing-on-github/basic-writing-and-formatting-syntax>

### Highlight languages

<https://github.com/github/linguist/blob/master/lib/linguist/languages.yml#start-of-content>

## Juniper PyEZ

### timeout

RPC timeout is not the same than connection timeout
RPC timeout
<https://www.juniper.net/documentation/en_US/junos-pyez/topics/task/program/junos-pyez-rpcs-executing.html#task-rpcs-timeout-specifying>
Netconf timeout
<https://github.com/Juniper/py-junos-eznc/issues/780>
