# python-flask-nft-metadata

simple flask app which gets nft metadata given the address of nft

# installation

you need to install python 3 https://www.python.org/downloads/

after that install flask using `pip install flask`

# usage 

1)start postgredb using sql provided in `/src` folder

2)launch flask web app

3)provide nft address

4)get the results

# example

enter `3LZ9ezL5BkCtvdVGLkrw1q633EgfeYDpgGtBgWDgmaSU` as an adress and get tne following result:

{"mint":"3LZ9ezL5BkCtvdVGLkrw1q633EgfeYDpgGtBgWDgmaSU","standard":"metaplex","name":"Baby Yetis #257","symbol":"","metaplex":

{"metadataUri":"https://arweave.net/4PtHGFuAw2U-T4nrIWVRxJ0EpVIivRWi4xjreBkmMVg","updateAuthority":"yeT3ik5jX5RuK8JF8P3RRHrr9g6ox6RMWbRMh3r9FxQ","sellerFeeBasisPoints":500,"primarySaleHappened":0,

"owners":[{"address":"64eiSEPv2KRKNkPAX6d4BZQ3b12PcFqZP2yPoNAZw9po","verified":0,"share":100},{"address":"yeT3ik5jX5RuK8JF8P3RRHrr9g6ox6RMWbRMh3r9FxQ","verified":1,"share":0}],"isMutable":true,"masterEdition":false}}
