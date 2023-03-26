# ChatGPT LINE bot with Serverless Framework

You can talk to ChatGPT in LINE. The bot is deployed and running on AWS Lambda using the Serverless Framework.

## Credentials

1. Create an [OpenAI account](https://platform.openai.com/) and [API Key](https://platform.openai.com/account/api-keys)
2. Create a [LINE Developer account](https://developers.line.biz/en/) and set up a channel with [Message API](https://developers.line.biz/en/services/messaging-api/)
3. Create an [AWS account](https://aws.amazon.com/) and create an [IAM role](https://www.serverless.com/framework/docs/providers/aws/guide/credentials)

Create a file called `.env.yml`, and put the keys in the file.

```yaml
openaiKey: <OPENAI_API_KEY>
lineChannelSecret: <LINE_CHANNEL_SECRET>
lineChannelAccessToken: <LINE_CHANNEL_ACCESS_TOKEN>
```

## Installation

```bash
python3.8 -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Deployment

install dependencies with:

```
npm install
```

configure AWS credentials:

```
export AWS_ACCESS_KEY_ID=<your-key-here>
export AWS_SECRET_ACCESS_KEY=<your-secret-key-here>
```

and then perform deployment with:

```
serverless deploy
```

After running deploy, you should see output similar to:

```bash
Deploying chatgpt-line-bot-serverless to stage dev (us-east-1)

✔ Service deployed to stack chatgpt-line-bot-serverless-dev (182s)

endpoint: ANY - https://xxxxxxxx.execute-api.us-east-1.amazonaws.com
functions:
  api: chatgpt-line-bot-serverless-dev-api (1.5 MB)
```

_Note_: In current form, after deployment, your API is public and can be invoked by anyone. For production deployments, you might want to configure an authorizer. For details on how to do that, refer to [httpApi event docs](https://www.serverless.com/framework/docs/providers/aws/events/http-api/).

## Invocation

After successful deployment, put this URL into `Webhook URL` on LINE Developers Platform.

```bash
https://xxxxxxx.execute-api.us-east-1.amazonaws.com/dev/
```

Add the channel in your LINE account, then you can start chatting with ChatGPT!

## Todo

- [ ] Separate conversation history for different user
- [ ] Support voice message

Welcome to contribute!
