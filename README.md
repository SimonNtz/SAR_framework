Sentinel 1 (SAR) framework
===============================

This repo consists of the installation scripts of an Nuvla app.
It launches a server waiting for incoming requests of SAR product processing [SAR_app](https://github.com/SimonNtz/SAR_app/) It provides a log benchmarking system via Elastic.

## prerequisites

In order to successfully execute the application, you should have:

 1. An account on [Nuvla](https://nuv.la).  Follow this
    [link](http://ssdocs.sixsq.com/en/latest/tutorials/ss/prerequisites.html#nuvla-account)
    where you'll find how to create the account.

 2. Cloud credentials added in your Nuvla user profile
    <div style="padding:14px"><img
    src="https://github.com/SimonNtz/SAR_app/blob/master/run/NuvlaProfile.png"
    width="75%"></div>

 3. Python `>=2.6 and <3` and python package manager `pip` installed. Usually
    can be installed with `sudo easy_install pip`.

 4. SlipStream python ss-client installed: `pip install slipstream-client`.

 ## Instructions

  1. Clone this repository with

     ```
     $ git clone https://github.com/SimonNtz/SAR_framework.git
     ```

  3. Set the environment variables

     ```
     $ export SLIPSTREAM_USERNAME=<nuv.la username>
     $ export SLIPSTREAM_PASSWORD=<nuv.la password>
     ```

     and run the SAR processor on [Nuvla](https://nuv.la) with

     ```
     $ ./SAR_server_run.sh
     ```
