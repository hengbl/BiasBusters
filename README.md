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
<!-- markdownlint-disable MD033 -->
<!-- The lack of line breaks within anchor tags is due to a weird underline appearing when line breaks are present. -->
<p align="center">
  <a href="https://www.python.org/" title="Python"><img src="images/python.svg" height="100" width="auto" /></a>
  &nbsp;
  <a href="https://scikit-learn.org/stable/" title="Scikit-Learn"><img src="images/sklearn.png" height="100" width="auto" /></a>
  &nbsp;
  <a href="https://www.tensorflow.org" title="Tensorflow"><img src="images/tensorflow.svg" height="100" width="auto" /></a>
  &nbsp;
  <a href="https://www.google.com/search?client=safari&rls=en&q=telebot&ie=UTF-8&oe=UTF-8" title="Telebot"><img src="images/telegram.svg" height="100" width="auto" /></a>
  &nbsp;
  <a href="https://www.google.com/search?client=safari&rls=en&q=mongodb+documentation&ie=UTF-8&oe=UTF-8" title="MongoDB"><img src="images/mongodb.svg" height="100" width="auto" /></a>
  &nbsp;
  <a href="https://git-scm.com/doc" title="Git"><img src="images/git.svg" height="100" width="auto" /></a>
</p>
<!-- markdownlint-enable MD033 -->

## Documentation
- See our full documentation and report [here](https://docs.google.com/document/d/1oEJ0yzHoCiJSVWkN6aBg4_yyP9agPJLlX_myntL60oU/edit?usp=sharing).
- See our demo video [here](https://drive.google.com/file/d/176iT__R4OvdXzZmzGBxateXnvpLJjSdC/view?usp=sharing).
