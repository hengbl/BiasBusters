# BiasBusters
<img src="images/logo.png" width="384" height="384">
Sentiment Analysis telegram bot that gives students the best insights on NUS module based on online reviews &lt;3 

## Installation
1. Clone repository to your local machine:
```bash
git clone https://github.com/hengbl/BiasBusters.git
cd BiasBusters
```
2. Create a virtual environment to isolate our package dependencies locally:
```bash
python -m venv env
source env/bin/activate
```
3. Install all the required packages:
```bash
pip3 install -r requirements.txt
```
4. Set up the necessary environment variables:
Create a `.env` file in the root directory and add the following:
```plaintext
TELE_TOKEN='your_telegram_bot_api_key_here'
MONGO_URL = `your_mongodb_uri`
```
5. To start the Telegram bot, run:
```bash
python run.py
```

## Motivation
Be it incoming freshmen matriculating into NUS or current students, we face uncertainties and questions involving our curriculum. One specific difficulty would be choosing our modules. Apart from pre-assigned modules, we could choose additional modules to clear our unrestricted electives. That poses a question: **What is a good module that we can take up?**

Not everyone has the privilege to consult seniors and friends about the modules, hence the internet becomes a helpful channel to aid us in our decision. I’m sure a lot of students, including us, went through the experience of doing hours of research through all the different avenues available such as NUSMods, Reddit or even blogs. However, with so many irrelevant posts or comments with different sentiments out there, we continue racking our brains over a decision. Furthermore, merely having the opinions of a couple individuals may not be adequate due to potential inherent personal bias. 

This makes us ponder, wouldn’t it be great if there’s a **fast and convenient way to collate all these posts and come up with a general sentiment about a module**, without the hassle of going through each and every one of them? As aspiring data analysts / scientists, we want to make use of Machine Learning and Natural Language Processing to offer a solution that can solve a problem that plagued many of our college peers. This will potentially allow them to make a more informed decision about their modules which are imperative to their college experience.

## User Stories
1. As an incoming freshman or current student who wants to have an overall review of the module I am interested in, I want to see the overall sentiment of the said module quickly and effortlessly. 
2. As a teaching assistant or professor who wishes to understand students’ opinions on a module that they teach, they can access the statistics of the overall sentiments of students regarding that module online. 
3. As a user, I want the bot to be intuitive, and be able to handle commands that may have been an input error
4. As a user, I want to use the bot without being confused
5. As a user, I want the bot to be able to display the commands that I can use
6. As a user, I want to be able to see what reviews the model deemed to be positive or negative to further affirm my opinions

## Bot Flow
![flow_chart](images/flow_chart.png)

## Tech Stack
<table style="border-collapse: collapse; border: none;"">
  <tr>
    <td align="center"><img src="images/python.svg" width="100" height="100"><br>Python</td>
    <td align="center"><img src="images/sklearn.png" width="102" height="56"><br>Scikit-Learn</td>
    <td align="center"><img src="images/tensorflow.svg" width="80" height="80"><br>TensorFlow</td>
    <td align="center"><img src="images/mongodb.svg" width="80" height="80"><br>MongoDB</td>
    <td align="center"><img src="images/Telegram.png" width="80" height="80"><br>Telebot</td>
  </tr>
</table>

## Documentation
- See our full documentation and report [here](https://docs.google.com/document/d/1oEJ0yzHoCiJSVWkN6aBg4_yyP9agPJLlX_myntL60oU/edit?usp=sharing).
- See our demo video [here](https://drive.google.com/file/d/176iT__R4OvdXzZmzGBxateXnvpLJjSdC/view?usp=sharing).
