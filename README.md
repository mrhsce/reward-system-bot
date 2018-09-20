# reward-system-bot
A telegram bot to manage my rewarding system for time management

TODO 
- use web hook to take audio response from the server for fun time query


In order to execute this code pip should be installed, then executes these commands:

```shell
pip install python-telegram-bot

pip install python-telegram-bot[socks]

pip install requests
```

| Activity type |  facotr |        command      |          voice command|
| --------------| --------| --------------------| -----------------------|
|fun            |-1       |      /subtract fun x|         I had fun for x hours| 

Work            1/4             /add work x             I worked for x hours

Study           1/3             /add study x            I studied for x hours


On the server it should be executed in background:
      
```
nohup python python/reward_system/main.py > /dev/null 2>&1&
```
