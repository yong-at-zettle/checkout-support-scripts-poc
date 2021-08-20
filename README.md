# Purpose of this repo
We have Postman collections to invoke REST endpoints. This repo is yet another reinvented wheel :-), with the hope to give more flexibility when developers need to carry support tasks.

# Where to start
This repo assumes you have some basic knowledge of Python, at the time of writing this doc. Run [main.py](./main.py) to get a taste of what this repo can do.

# How is the code organized
As its name tells, it aims to assist solving support _tickets_. So, you usually start with creating a folder under [tickets](tickets) folder, with the Jira ticket number.

Normally, a support task will involve _use cases_ like [reads](usecases/reads.py) data from services or [finalizing](usecases/finalization.py) purchases. You find code under [usercases](usecases) to provide such support. 

A _use case_ is meant to be a aggregation of one or many REST calls. For example, [finalizing](usecases/finalization.py) involves calls to get [access token](clients/authorization/client.py) and send request to [checkout](clients/checkout/client.py). 

The atomic _REST calls_ are grouped under the name of the services from [clients](clients) folder.

As in most project, there are shared utility functions, e.g., parsing CSV file containing checkouts UUIDs etc. You find such functions under [commons](commons)

# Credentials configuration
Hopefully this is the **only** configuration you need to touch. It's **only** needed when talking to PROD env. You need to provide your `clientId` and `clientSecret` to [auth config](clients/authorization/config.py).