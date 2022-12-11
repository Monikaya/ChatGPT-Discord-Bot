# ChatGPT-Discord-Bot
A simple discord bot that interacts with ChatGPT

### Setup
```bash
$ git clone https://github.com/Monikaya/ChatGPT-Discord-Bot.git
$ cd ChatGPT-Discord-Bot
$ pip install -r requirements.txt
```
Create a .env file with the following variables:
<br>
WEBHOOK={Webhook}
<br>
TOKEN={Token}
<br>
CHATGPT_EMAIL={ChatGPT-Email}
<br>
CHATGPT_PASS={ChatGPT-Password}

After that, you should just be able to run:
```bash
$ ./main.py
```

### Notes
For this bot you will need both a bot and a webhook. 
The bot will handle reading the messages, most of the commands, etc. 
While the webhook will simply just return the response to whatever channel it's configured to.

This is done as to make it more seamless, instead of using a prefix or slash command you can just send a message and have the webhook respond.
Like a conversation!

### TODO
- Make the bot getting the response from OpenAI async
- Add some more useful commands
- Other general improvements