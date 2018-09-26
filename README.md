# reward-system-bot
A telegram bot to manage my rewarding system for time management

TODO
------
- add start pause and stop timer commands to calculate time exp start timer for work
- use toggl Api to store time and take queries
Installation
---------------------
In order to execute this code pip should be installed, then executes these commands:

```shell
pip install python-telegram-bot

pip install python-telegram-bot[socks]

pip install requests
```
Running
-------------
On the server it should be executed in background:
      
```
cd python/reward_system
nohup python main.py > /dev/null 2>&1&
```

How to use
------------

| Activity type |  facotr |        command      |          voice command|
| --------------| --------| --------------------| -----------------------|
|fun            |-1       |      /subtract fun x|         I had fun for x hours| 
|Work           | 1/4     |        /add work x  |          I worked for x hours|
|Study          | 1/3     |        /add study x |           I studied for x hours|
|Reading        | - 1/3   |       /add read x   |       I read for x hours |
|Exercise       | const 0.5 |     /activity exercise |  I exercised |
|Leitner        | const 0.25 |   /activity leitner  |  Daily leitner finished |



