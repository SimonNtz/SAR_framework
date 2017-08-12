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
  4. Wait for the 'ready' state

  5. Recover the ip of the server and send requests to the server

    ```
    - Initialization:

    curl -H "Content-Type: application/json" -X POST /<server_ip>:81/SLA_INIT -d
    '{
      "specs_vm"={"mapper":[4,16,100], "reducer":[1,0,5,10]},
      "product_list"=["S1A_IW_GRDH_1SDV_20151226T182813_20151226T182838_009217_00D48F_5D5F"],
      "result" = '{"s3_credentials":[<host_base>, <buket_id>, <access_key>, <secret_key>]}
      }'


    - SLA request:

    curl -H "Content-Type: application/json" -X POST /<server_ip>:81/SLA_CLI -d
     '{
       "SLA":{"requirements": [1000, 1],
              "product_list": ["S1A_IW_GRDH_1SDV_20151226T182813_20151226T182838_009217_00D48F_5D5F",
                               "S1A_IW_GRDH_1SDV_20160424T182813_20160424T182838_010967_010769_AA98"]},
              "result": {"s3_credentials":[<host_base>, <buket_id>, <access_key>, <secret_key>]}
      }'

    ```
