# hebrew-bot
[![Build Status](https://travis-ci.com/k9173a/hebrew-bot.svg?branch=master)](https://travis-ci.com/k9173a/hebrew-bot)
[![License: MIT](https://img.shields.io/github/license/k9173a/hebrew-bot)](https://github.com/K9173A/hebrew-bot/blob/master/LICENSE)

Bot can be found here: t.me/HebrewInfoBot

Deployed on [pythonanywhere.com](https://www.pythonanywhere.com/).
1. Copy private token from `.env` file:
   ```bash
   export BOT_TOKEN=XXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   ```
2. Check it:
   ```bash
   printenv | grep BOT_TOKEN
   ```
3. Clone:
   ```bash
   git clone https://github.com/K9173A/hebrew-bot.git
   ```
3. Run:
   ```bash
   cd hebrew-bot
   chmod +x deploy.sh
   ./deploy.sh
   ```