rpc
===

a python to python implementation of rpc (RMI) for generating hashes(sha256/sha512)

Tutorial
========

Step 1 :
==========
>Download the repo

Step 2 :
==========
>Extract the zip

Step 3 :
==========
>Rename the extracted folder to 'rpc'

Step 4 :
==========
>Start the server by the command :-  
>```shell  
>python rpc/server.py
>```

Step 5 :
==========
Run the client in a separate terminal as follows :-
>```python  
>import rpc  
>c = rpc.client()  
>#generate a sha256 hash  
>c.sha(256,'this is my string')  
>#generate a sha512 hash  
>c.sha(512,'this is another string')  
>```
