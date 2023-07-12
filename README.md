# Lord of the Rings SDK

Install package from command line by using PIP and downloading packages from TestPyPI instead of PyPI by specifying the --index-url flag::
python3 -m pip install --index-url https://test.pypi.org/simple/ lotr-sdk-reyka

Use the MovieQuoteSDK class contained within the core/movie_quite_sdk package. 

You must supply the MovieQuoteSDK class with your Auth Token from the LOTR API site. 

When running tests, it pulls the auth token from an environmental variable named 'sdk_lotr_token'.
