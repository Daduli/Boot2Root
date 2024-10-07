# EXPLOIT 8: EMAILS FOR DEVELOPERS

After acquiring *lmezard*'s credentials from the forum, we can skip using the */webmail* page and directly access the `IMAP` server instead.

## Browsing the IMAP server

First, we need to connect to the IMAP server, which can be accessed through two ports: *143* for IMAP and *993* for SSL/IMAP. Similar to the webserver, we can deduce that port 993 is more secure since it uses an SSL certificate. Therefore, we will connect through that port.

```sh
openssl s_client -connect 192.168.144.3:993 -quiet
```

Now that we've established a connection to the IMAP server, we need to log in to access additional commands. We'll use *lmezard*'s credentials to authenticate and gain access to the server.

```
A LOGIN laurie@borntosec.net !q\]Ej?*5K5cy*AJ
```

We're in! The next step is to explore the session and examine the available mailboxes for any interesting information.

```
A LIST "" "*"
```

As we can see, the main "INBOX" may contain all the emails. Let's check its contents!

```
A STATUS INBOX (MESSAGES)
```

It seems there are two messages in the "INBOX." We'll need to select that mailbox to view the contents of both messages.

```
A SELECT INBOX
```

At last, we can examine the content of both messages, one at a time.

```
> A FETCH 1 RFC822
> A FETCH 2 RFC822
```

We discover the credentials for the *root* user in the database! Now, we can proceed from the point where we log in to the database as *root*.