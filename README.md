# Checkson self check for Google PubSub integration

This check is used to monitor Checkson itself. It checks if a message can be sent to Google PubSub and that
this message is received by the relevant service within the Checkson backend.

This check is likely not useful to anyone else, except as an example.

## Environment variables

| Variable           | Description |
|------------------- |-------------|
| `CHECK_API_SECRET` | The secret to use for sending the message |

## Use check on Checkson

This check can be used on [checkson.io](https://checkson.io) (or anywhere else) with the following Docker image:

```
ghcr.io/checkson-io/checkson-pubsub-self-check:main
```

## Run check locally

```
docker run \
  --env CHECK_API_SECRET=xyz \
  --rm \
  -it \
  ghcr.io/checkson-io/checkson-pubsub-self-heck:main
```
