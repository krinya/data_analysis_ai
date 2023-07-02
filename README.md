# Welcome to Tablesense
## The dasboard that helps you with your data analysis

https://tablesense.streamlit.app/

This dashboard is created to help you to wire queries and scripts. It uses Chat GPT in the backbround.

It helps you to give answers to your coding questions based on the data that you have. Imagine as a Chat GPT, but better because it knows your data structure too.

So for example, once you configure it, you can ask questions like:

How to write an SQL query to calculate my website visitors per day?
How to write a Python script to calculate the number of items sold per day?
Or even more complex questions like: How to write a Python script to calculate the number of items sold per day for each country?
Do EDA on my data using pandas and plotly express using the data that it is defined.
And it will give you the answer. If you do not like the result you can continue the conversation with the chatbot and it will give you a new answer.

How to use the dashboard?
1. Get your OpenAI API key, and give it to the dashboard.
In order to intaract with the dashboard (otherwise it won't work) first you need to have an OpenAI API key. Do not worry, it is prety easy to get one. Register at the Open AI page and add a a credit / debit card. Unfortunately using the API of the Chat GPT is not free, it costs some money for the API calls. But do not worry so much about it, it is not expensive. I used it for a while and it costs cents not even dollars.

You can create the API key on https://beta.openai.com/account/api-keys. Once you create it you can copy it here below or to the sidebar to be able to use the dashboard

2. Define your tables at the 'Define data' page.
In order to be able to ask questions you need to define your tables. You can do it at the 'Define data' page.

You can do this either importing a CSV file or add your data manualy by defining the table names and the column names of the tables

Once you define the tables and the columns you can save it for latter use. Once you saved it you can load it later on the 'Load data' page.

(The dashboard do not share this data with anyone, it is stored on your local machine for only a given session.)

3. Ask your questions in the Chat tab.
Once you have your tables defined you can ask questions in the 'Talk with Chat GPT' page. Where you ask your questions and the Chat GPT will give you the answer.