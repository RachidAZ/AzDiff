from azure.mgmt.web import WebSiteManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.identity import AzureCliCredential
import logging


logger = logging.getLogger('azure')
logger.setLevel(logging.ERROR)


def get_details_functionapp(rg_name, resource_name, subscription_id):
     credential = AzureCliCredential()
     web_mgmt_client = WebSiteManagementClient(credential, subscription_id)
     
     function_app = web_mgmt_client.web_apps.get(rg_name, resource_name) 
     return function_app


def get_functions_functionApp(rg_name, resource_name, subscription_id):
     credential = AzureCliCredential()
     web_mgmt_client = WebSiteManagementClient(credential, subscription_id)
     
     functions = web_mgmt_client.web_apps.list_functions(rg_name, resource_name)
     return functions



def get_appsettings_functionapp(rg_name, resource_name, subscription_id):
     credential = AzureCliCredential()
     web_mgmt_client = WebSiteManagementClient(credential, subscription_id)
     
     function_app_settings = web_mgmt_client.web_apps.list_application_settings(rg_name, resource_name) 
     return function_app_settings


def get_details_appService(rg_name, resource_name, subscription_id):
     credential = AzureCliCredential()
     web_mgmt_client = WebSiteManagementClient(credential, subscription_id)
     
     app_service = web_mgmt_client.web_apps.get(rg_name, resource_name) 
     return app_service


def get_details_service_plan(rg_name, resource_name, subscription_id):
     credential = AzureCliCredential()
     web_mgmt_client = WebSiteManagementClient(credential, subscription_id)
     
     service_plan = web_mgmt_client.app_service_plans.get(rg_name, resource_name) 
     return service_plan

def get_details_vm(rg_name, resource_name, subscription_id):
     credential = AzureCliCredential()
     compute_mgmt_client = ComputeManagementClient(credential, subscription_id)
     
     vm = compute_mgmt_client.virtual_machines.get(rg_name, resource_name) 
     return vm