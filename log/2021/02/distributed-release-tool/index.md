Decentralized Media Releases
============================

Premise
-------

It ought to be possible to do completely distributed crowd-funded media
releases where:

1. No publishing company or middlemen are involved in the release.
2. The artist gets paid a fixed-fee at the time when the work is released
   to the public.
3. The work is distributed by fans on a peer-to-peer network before it is
   released.
4. The release mechanism is done by bots who have a financial incentive to
   not share early (ideally not fans).

Mechanism
---------

The artist takes the release that they wish to sell and opens up a web-based
tool. The tool is written in plain old JavaScript, ideally hosted on IPFS.

The tool creates an archive, a `tar` file containing a `json` file that
describes the contents, and a bunch of files/fragments of files that have one
of the following encryption statuses:

1. Not encrypted.
2. Can be unlocked by one of several groups of "M of N" release keys.

The user now solicits escrow bots in a p2p fashion. Once the bots have been
found, the file is encrypted so that they can unlock the encrypted chunks.
The bots sign the final contract, and the file is released on IPFS.

Users download the file and examine the plaintext contents. If they like the
previews, they submit money to the contract. Once the funding goal is met,
bots release the keys that allows the content to be decrypted. Once this
step is complete, the author finalizes the contract and their money is
released.

Attacks, failures and mitigations
---------------------------------

### Colluding keyholders

Two keyholders get together and share their keys, unlocking the file early.

* Submitting a private key allows you to take 50% of that keyholder's deposit.

### Vanishing keyholders

Once the funding goal is met, the keyholders don't show up to release the
keys.

* The author should be able to release manually in case the escrow bots go
offline and never return.

* There should be multiple groups of "M of N" keyholders, who act as backups
for each other. Later groups have a larger N.

* The keys should be in a format that's storeable in a crypto-wallet so it
doesn't actually rely on bots; humans can manually do the process. Maybe
the release key is, by default, a phrase combined with their wallet key and
hashed?

* The process should be easy to automate. If there's a smart contract bot
automation thingy that we can add this as a module?

### Author never releases the file

The author solicits the bots, but never releases the file. So it's not
available on IPFS.

* Users shouldn't send money unless they can view the file.

### Author sends a brick in a box

The author publishes a different file to what was agreed, ripping off their
community.

* Allow plaintext file parts inside the archive. So, with streaming video or
audio, segments of the file can be released as a preview. If they don't do
that then they're suspect by default.

* It's their reputation on the line.

### Failure to fund

The funding goal is never met, the keyholders have money locked up in the
contract.

* The contract needs an expiry date. 

### Releasing keys after failure

I don't need to pay, I can just wait until it fails and the keyholders
get their money back, then get keyholders to leak the keys.

* The license isn't valid if the contract isn't fulfilled. Standard 
copyright applies, and the media can't be legally used by the community that
funded it.

* Keyholders should get reputation for each completed contract, and have that
removed by leaking the keys early or outside of the contract terms.

* Some small percentage of each successful contract should go into a reputation
fund. If anyone can prove that they are dishonest or negligent, they get a
portion of the money.

### Cashing out reputation

I've built up this reputation fund. I'll spend it by snitching on myself.

* Reputation should be able to be cashed in without leaking keys, but not while
contracts are open, or until some time after the last contract.

* When you snitch, you don't get the reputation payout any quicker. It's no more
convenient to snitch on yourself than it is to just wait and then withdraw.

### Reputation farming

I can get reputation by farming Sybil contracts, and get more future contracts
than others because I have more reputation.

* Allow people with money to stake it in their own reputation fund. So rather
than earning it by running fake contracts, they can just put their money where
their mouth is instead.

