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
>Start the server by the command :-  
>```shell  
>python rpc/server.py
>```

Step 4 :
==========
Run the client in a separate terminal as follows :-
>```python  
>import rpc  
>c = rpc.client()  
>#generate an sha256 hash  
>c.sha(256,'this is my string')  
>
>```
