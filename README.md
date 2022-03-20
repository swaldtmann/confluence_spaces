# confluence_spaces
A Python script to fetch information about spaces from Atlassian Confluence Server or Datacenter.


## Create Environment
    pipenv install
    pipenv shell

## create .env file
    vi .env

Add the following with the correct data for your purpose

    # .env 
    ATLASSIAN_USERNAME=<your username here>
    ATLASSIAN_PASSWORD=<your password here>

    # your url may look like: https://wiki.example.com/rest/api/space?limit=500
    ATLASSIAN_URL=<your url here>

    #
    # End of .env


# Run the script with
    pipenv run getConfSpaceInfo.py
