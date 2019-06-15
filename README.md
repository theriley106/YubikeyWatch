# YubikeyWatch

## What does this do?

This bot creates and posts dank memes whenever someone accidentally posts a Yubikey in a GroupMe thread.

## How does this work? (Technical Overview)

GroupMe has a really well documented API

I have a GroupMe bot called "tHeYuBiKeYpOlIcE" with the Callback URL pointing to a heroku app that contains this code.

Whenever a new post is made in the specified GroupMe thread, a POST request is sent to the Callback URL containing a payload similar to the following:

callBack = {
    "attachments": [],
    "source_guid": "REDACTED",
    "text": "Example Groupme post",
    "sender_id": "3981",
    "system": False,
    "id": "REDACTED",
    "user_id": "3981",
    "name": "Christopher Lambert",
    "created_at": 1560389057,
    "sender_type": "user",
    "avatar_url": "https://i.groupme.com/512x512.jpeg",
    "group_id": "4770"
}

## Example





looks for accidental Yubikey posts in a GroupMe chat, and creates
