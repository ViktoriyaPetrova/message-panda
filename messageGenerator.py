#Presenter for the message-generator page
from flask import request, render_template
from markupsafe import escape
from flask.views import MethodView
from util import saveUserChoices
import os
from openai import OpenAI


#To run locally uncomment this code and follow the steps on this page to set up your OpenAI API key:
#https://platform.openai.com/docs/quickstart?context=python
client = OpenAI()

# Set up OpenAI API key with env variables
# client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))


class MessageGenerator(MethodView):
    def get(self):
        return render_template('message-generator.html', response='', isHome=False, wasSubmitted=False)
    def post(self):
        isReply = request.form['replyBtn']
        format = request.form['format']
        context = escape(request.form['context'])
        tone = request.form['tone']

        userChoices=saveUserChoices(isReply, format, tone)

        if isReply == 'yes':
            reply = escape(request.form['reply'])
            content = f"Write a {tone} {format} reply in English to this {format}: {reply}. Incorporate the following in the reply: {context}."
        else:
            content = f"Write a {tone} {format} in English that incorporates the following: {context}."

        # GPT 3
        response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        max_tokens=2000,
        messages=[
            {"role": "system", "content": f"You are a helpful assistant that helps write short and concise {tone} {format} messages."},
            {"role": "user", "content": content},
        ]
        )
        if isReply == 'yes':
            return render_template('message-generator.html', response=response.choices[0].message.content, isHome=False, wasSubmitted=True, userChoices=userChoices, context=context, reply=reply)
        return render_template('message-generator.html', response=response.choices[0].message.content, isHome=False, wasSubmitted=True, userChoices=userChoices, context=context)
