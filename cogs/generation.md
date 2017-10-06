The generation script we **use** is doing the following things:
It generates a "IP"(IPv4 like IPs) which it then stores into the database, then it grabs the IPs it generated from the database and attempts to make a server with that name.
If that fails, it will notify the user specified in cogs.utils.checks that he needs to use a second command to transfer EXISTING servers to his or her account