#python script to automate pulling reports
# Fill in with your personal access token and org URL
# Create a connection to the org
# Get a client (the "core" client provides access to projects, teams, etc)
# Get the first page of projects

#python runner.py config URL --set-to https://dev.azure.com/fabrikam
#python runner.py config PAT --set-to ABC123

from azure.devops.connection import Connection
import msrest
from msrest.authentication import BasicAuthentication
import config
import pprint

personal_access_token=config.PAT
organization_url=config.ORG_URL

my_credentials=BasicAuthentication("",personal_access_token)
my_connection= Connection(config.ORG_URL,my_credentials)
core_client = my_connection.clients.get_core_client();
print(core_client)
get_projects_response = core_client.get_projects()
print(get_projects_response);

index = 0
while get_projects_response is not None:
    for project in get_projects_response.value:
        print("[" + str(index) + "] " + project.name)
        index += 1
    if get_projects_response.continuation_token is not None and get_projects_response.continuation_token != "":
        # Get the next page of projects
        get_projects_response = core_client.get_projects(continuation_token=get_projects_response.continuation_token)
    else:
        # All projects have been retrieved
        get_projects_response = None
