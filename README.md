# Checkson Check for monitoring the page speed of a website

This check uses [Google's PageSpeed API](https://developers.google.com/speed/docs/insights/v5/get-started) 
(which in turn is built on [Lighthouse](https://github.com/GoogleChrome/lighthouse))

Use this check on [checkson.io](https://checkson.io) to monitor if your technical SEO, performance do not fall
below any defined thresholds.

To determine the threshold, it's a good idea to go to [pagespeed.web.dev](https://pagespeed.web.dev/) and analyze
your website initially as a baseline.

## Environment variables

| Variable       | Description |
|----------------|-------------|
| URL            | The URL to check |
| CATEGORY       | One of `accessibility`, `best-practices`, `performance`, `pwa`, `seo`. Default is `performance` |
| STRAGEGY       | One of `mobile`, `desktop`, Default is `desktop` |
| SCORE_THRESHOLD | Number between 0.0 and 1.0 |

## Use check on Checkson

This check can be used on [checkson.io](https://checkson.io) (or anywhere else) with the following Docker image:

```
ghcr.io/checkson-io/checkson-pagespeed-check:main
```

## Run check locally

This checks the performance score of a website is above 90%.

```
docker run \
  --env URL=https://nytimes.com \
  --env SCORE_THRESHOLD=0.9 \
  --rm \
  -it \
  ghcr.io/checkson-io/checkson-pagespeed-check:main
```
