# Why

You want to be able to prove someone claimed something at a specific time. For legal
reasons, for archival reasons, or to back up claims made by an LLM.

## How

Web service. You give it a link to the resource, it downloads and archives
the inner http payload, then the certificate chain and info. Then adds the archive to
IPFS and returns the CID. It then publishes the existence of the hash and the signs it with the key of the downloader so we know the MAC hasn't been altered.

if the http payload already exists, winner! we now have two proofs.

## Uses?

* Share facts with other people using IPFS gateways. Create a knowledge tree.
* Use other models to build claims on top of claims. "whisper says this cid transcribes to xyz" etc
* Legal disputes.
* Use them as filters for adding data to datasets for ML. "X said Y about Z" doesn't make
  it true, but it's very hard to fake that they said it.
* Nation state tampering with certificate chains becomes part of the historical record.
* Makes your penis grow by at least 2 inches, if not in length then in girth.

