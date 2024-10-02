# EXPLOIT 2: LINUX VULNERABILITY

There’s another method to gain root access on this machine. Since it runs on Linux, we can exploit the CVE-2016-5195 vulnerability, commonly referred to as Dirty COW.

## Dirty COW

*Dirty COW* is a privilege escalation vulnerability in the Linux Kernel, caused by a race condition. To exploit it, we'll return to the point where we first gained SSH access with the user `laurie`. From there, we can use this [exploit](https://github.com/firefart/dirtycow) to take advantage of the vulnerability and create a user with root privileges.

First, we need to copy the `dirty.c` exploit script to our local environment. After that, we'll compile it using the following command:

```
gcc -pthread dirty.c -o dirty -lcrypt
```

Then, we execute the script using the following command:

```
./dirty root
```

The program creates a thread that repetitively writes to a copy of the `/etc/passwd` file while simultaneously attempting to read from it. This triggers a race condition, as the file can only be accessed for reading or writing at any given time, allowing the exploit to create a new user with root privileges in the process.\
Finally, we can log in as the newly created user, `firefart`, who has root privileges, as confirmed by using the **id** command.

Another way to gain **root** access!