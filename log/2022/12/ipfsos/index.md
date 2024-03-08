# A Distributed Operating System

What if your distro and desktop weren't on your computer? They were on all your computers.

## Ingredients

* Base OS is Linux. Could be a VM on Windows or Mac.
* Install app, depends on Docker and has a controller daemon that:
  * Mounts IPFSfs and encrypted areas
  * Create/destroy containers
  * Chown stuff for container users
  * Gives Wayland socket to a container that logs on from the logon manager
* Pull the main image down. Contains:
  * IPFS which gets mapped to the host's data area
  * Deals with user management and quotas
  * Pins files in IPFS for other users
  * Webserver that acts as a UI for users logging in
  * Drops a .desktop file in to enable login
  * XRDP/VNC bridge for remote users
* Mobile app/html+js 
  * peerjs for communication/authentication
  * not MFA, it's the 1FA.

## Setup/login

* Go to a machine, choose IPFSOS as your login manager
* Scan QR code on phone
  * Computer and phone pair using peerjs
  * Choose objects + permissions for computer (sync/read/write to OS/mount/session)
  * Phone sends over an IPFS pin root FS + keys to unlock object paths
* Computer presents list of  that it can unlock, plus available storage quota etc
  * Phone and computer are now linked.
  * If you're an admin on that box you get more options.
  * Stuff starts syncing to this box from others.
* Choose either a local session or a remote one.
  * Remote sessions are xrdp or similar, to another box.
* Log in to session using your phone

## Day to day use cases

### Log on to any machine

Log on to any machine that you trust, and get the same desktop and all your files.

### Distributed, free backup for your friends

No more backups. No more losing data. No more paying for cloud storage.

Any box is a backup and is backed up - your Raspberry Pi with NAS, your work machine,
a random VPS... Your phone? Maybe. There's no limit.

Disk crash? Just log in and download all your files from your friends.

### File sharing is light and easy.

Send someone a link to a pin and a hash, they get the same file as you. They probably
have the file anyway! To stop sharing new versions you just change the encryption key.

### p2p messaging layer

* File sharing with friends
* Notifications to phone

### Modern, phone-friendly

Backup by posting directory updates from your phone and syncing. Share files p2p using
any node of your choice.
