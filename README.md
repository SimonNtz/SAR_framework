Sentinel 1 (SAR) framework
===============================

This repository consists of a server using Flask API. It deploys  the application [SAR_app](https://github.com/SimonNtz/SAR_app/) by SixSq parametrized according the data input.

## Instructions

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

 4. SlipStream Client installed: `pip install slipstream-client`.

 5. Flask Api installed: `pip install Flask-API`

 6. Boto3 intstalled: `git clone git://github.com/boto/boto.git
                        cd boto
                        python setup.py install`

7. Requests installed

1. 
1. Do not change the file stucture (i.e. `SAR_mapper.py` and `SAR_reducer.sh` should stay at the root.)

1. Implement your own mapper and reducer.

1. The repository's name must stay as `SAR_proc`

*Note: data files are located in the root directory of the mapper and reducer scripts by default.*
