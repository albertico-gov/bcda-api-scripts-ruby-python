# BCDA API Examples: Ruby and Python

## Description

The following scripts provide basic examples in Ruby and Python to interact with the [Beneficiary Claims Data API](https://bcda.cms.gov/) (BCDA) Version 2.

These scripts are for demonstration purposes and are NOT intended to be used in production. Organizations most implement robust security practices to protect their secrets and tokens. Error handling, token validation/refresh and logging must also be implemented when integrating with a production environment.

The following steps are performed by these sample scripts:

1. Create access token
2. Submit a data `$export` request
3. Retrieve Job ID and URL
4. Check Job status

For additional details, please refer to the [BCDA documentation](https://bcda.cms.gov/guide.html)

### Assumptions

It is expected that the job processing a given data export request is completed before the token expires. Please refer to the [Try the API section](https://bcda.cms.gov/guide.html#try-the-api) in the [BCDA documentation](https://bcda.cms.gov/guide.html) to obtain sandbox credentials corresponding to an extra-small Accountable Care Organization (ACO).

## Ruby Example: `bcda.rb`

The `bcda.rb` script contains simple logic to interact with the BCDA v2 API using the [Ruby programming language](https://www.ruby-lang.org/en/).

### Requirements

Ruby 3.1.0+

> **Note:** 
> Please refer to the [Ruby Documentation](https://www.ruby-lang.org/en/documentation/installation/) for instructions on how to download and install Ruby in your system.

Execute the following command to install dependencies:

```shell
$ gem install http
```

### Usage

First you must modify the script to include the BCDA sandbox (testing) credentials:

```ruby
# Credentials
# Visit the following link for sandbox credentials: https://bcda.cms.gov/guide.html#try-the-api
CLIENT_ID = "REPLACE-WITH-SANDBOX-CLIENT-ID"
CLIENT_SECRET = "REPLACE-WITH-SANDBOX-CLIENT-SECRET"
```

> **Note:** 
> Please refer to the [Try the API section](https://bcda.cms.gov/guide.html#try-the-api) in the [BCDA documentation](https://bcda.cms.gov/guide.html) to obtain sandbox credentials corresponding to an extra-small Accountable Care Organization (ACO).

You can then execute the script by running the following command:

```shell
$ ruby bcda.rb
```

## Python Example: `bcda.py`

The `bcda.py` script contains simple logic to interact with the BCDA v2 API using the [Python programming language](https://www.python.org/).

### Requirements

Python 3.10.0+

> **Note:** 
> Please refer to the [Python Beginners Guide](https://wiki.python.org/moin/BeginnersGuide/Download) for instructions on how to download and install Python in your system.

Execute the following command to install dependencies:

```shell
$ pip3 install httpx
```

### Usage

First you must modify the script to include the BCDA sandbox (testing) credentials:

```python
# Credentials
# Visit the following link for sandbox credentials: https://bcda.cms.gov/guide.html#try-the-api
CLIENT_ID = "REPLACE-WITH-SANDBOX-CLIENT-ID"
CLIENT_SECRET = "REPLACE-WITH-SANDBOX-CLIENT-SECRET"
```

> **Note:** 
> Please refer to the [Try the API section](https://bcda.cms.gov/guide.html#try-the-api) in the [BCDA documentation](https://bcda.cms.gov/guide.html) to obtain sandbox credentials corresponding to an extra-small Accountable Care Organization (ACO).

You can then execute the script by running the following command:

```shell
$ python3 bcda.py
```

## License and Attribution

Developed by [Alberto Colón Viera](https://github.com/albertico-gov).

This software is licensed under the MIT License. See [LICENSE](LICENSE).
