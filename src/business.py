from src import backend
import logging

def get_details_vm(rg_name , resource_name, subscription_id):
    try:
        vm_details=backend.get_details_vm(rg_name, resource_name, subscription_id) 

        object1= vm_select(vm_details)
        return object1
    except Exception as e:
        logging.error(f"Error in get_details_vm function: {e}")
        exit(1)


def get_details_serviceplan(rg_name , resource_name, subscription_id):
    try:
        plan_details=backend.get_details_service_plan(rg_name, resource_name, subscription_id) 
            
        object1= serviceplan_select(plan_details)
        return object1
    except Exception as e:
        logging.error(f"Error in get_details_serviceplan function: {e}")
        exit(1)


def get_details_appservice(rg_name , resource_name, subscription_id):
    try:
        app_details=backend.get_details_appService(rg_name, resource_name, subscription_id)
        app_sett=backend.get_appsettings_functionapp(rg_name, resource_name, subscription_id)
        
        object1= appservice_select(app_details, app_sett)
        return object1
    except Exception as e:
        logging.error(f"Error in get_details_appservice function: {e}")
        exit(1)


def get_details_function_app(rg_name , resource_name, subscription_id):
    try:
        func_details=backend.get_details_functionapp(rg_name, resource_name, subscription_id)
        func_functions=backend.get_functions_functionApp(rg_name, resource_name, subscription_id)
        func_app_sett=backend.get_appsettings_functionapp(rg_name, resource_name, subscription_id)
        

        object1= functionapp_select(func_details, func_functions, func_app_sett)
        return object1
    except Exception as e:
        logging.error(f"Error in get_details_function_app function: {e}")
        exit(1)


def functionapp_select(func_details, func_functions,func_app_sett ):

    dynamic_object = {}

    # Add wanted properties
    dynamic_object["name"]                             = func_details.name        
    dynamic_object["resource_group"]                   = func_details.resource_group
    dynamic_object["location"]                         = func_details.location
    dynamic_object["kind"]                             = func_details.kind
    dynamic_object["type"]                             = func_details.type
    dynamic_object["state"]                            = func_details.state
    dynamic_object["enabled"]                          = func_details.enabled    
    dynamic_object["runtime"]                          = func_app_sett.properties["FUNCTIONS_EXTENSION_VERSION"]
    dynamic_object["linux_fx_version"]                 = func_details.site_config.linux_fx_version
    dynamic_object["java_version"]                     = func_details.site_config.java_version
    dynamic_object["always_on"]                        = func_details.site_config.always_on
    dynamic_object["java_container_version"]           = func_details.site_config.java_container_version
    dynamic_object["availability_state"]               = func_details.availability_state
    dynamic_object["reserved"]                         = func_details.reserved
    dynamic_object["vnet_route_all_enabled"]           = func_details.vnet_route_all_enabled
    dynamic_object["vnet_image_pull_enabled"]          = func_details.vnet_image_pull_enabled
    dynamic_object["vnet_content_share_enabled"]       = func_details.vnet_content_share_enabled
    dynamic_object["client_cert_enabled"]              = func_details.client_cert_enabled
    dynamic_object["client_cert_mode"]                 = func_details.client_cert_mode
    dynamic_object["client_cert_exclusion_paths"]      = func_details.client_cert_exclusion_paths
    dynamic_object["suspended_till"]                   = func_details.suspended_till
    dynamic_object["max_number_of_workers"]            = func_details.max_number_of_workers
    dynamic_object["default_host_name"]                = func_details.default_host_name
    dynamic_object["slot_swap_status"]                 = func_details.slot_swap_status
    dynamic_object["https_only"]                       = func_details.https_only
    dynamic_object["redundancy_mode"]                  = func_details.redundancy_mode
    dynamic_object["public_network_access"]            = func_details.public_network_access
    dynamic_object["storage_account_required"]         = func_details.storage_account_required
    dynamic_object["key_vault_reference_identity"]     = func_details.key_vault_reference_identity    
    dynamic_object["managed_environment_id"]           = func_details.managed_environment_id
    dynamic_object["service_plan"]                     = func_details.server_farm_id.split("/")[-1]
    dynamic_object["server_farm_id"]                   = func_details.server_farm_id
    dynamic_object["virtual_network_subnet_id"]        = func_details.virtual_network_subnet_id
    dynamic_object["tags"]                             = func_details.tags
    dynamic_object["tags_count"]                       = len(func_details.tags.keys()) if func_details.tags else 0 
    dynamic_object["id"]                               = func_details.id
    dynamic_object["min_tls_version"]                  = func_details.site_config.min_tls_version
    dynamic_object["ip_restrictions_default_action"]   = func_details.site_config.ip_security_restrictions_default_action
    dynamic_object["ftps_state"]                       = func_details.site_config.ftps_state
    dynamic_object["public_network_access"]            = func_details.site_config.public_network_access
    dynamic_object["health_check_path"]                = func_details.site_config.health_check_path 


    func_names=""
    func_functions_list=list(func_functions)
    i=1
    for fun in func_functions_list :
        func_names=func_names + f"\n {i})" + fun.name.split("/")[-1] 
        i=i+1
    
    dynamic_object["functions"] = func_names

   
    func_bindings=""
    i=1
    for fun in func_functions_list:
        func_bindings=func_bindings + f"\n - {i})" + fun.name.split("/")[-1] + " => language:" + fun.language + ", is_disabled:" + str(fun.is_disabled ) + ", bindings_details:" +  str(fun.config["bindings"]) 
        i=i+1
    dynamic_object["functions_details"] = func_bindings

    # show only number of entries in the app settings as they night contain sensitive data
    dynamic_object["app_settings_count"] = len(func_app_sett.properties.keys())

    identity_enabled = func_details.identity and func_details.identity.type == 'SystemAssigned'
    dynamic_object["system_assigned_identity"] = identity_enabled

    return dynamic_object



def appservice_select(app_details , app_sett):

    dynamic_object = {}

    # Add wanted properties
    dynamic_object["name"]                             = app_details.name        
    dynamic_object["resource_group"]                   = app_details.resource_group
    dynamic_object["location"]                         = app_details.location
    dynamic_object["kind"]                             = app_details.kind
    dynamic_object["type"]                             = app_details.type
    dynamic_object["state"]                            = app_details.state
    #dynamic_object["provisioning_state"]                = app_details.provisioning_state
    dynamic_object["enabled"]                          = app_details.enabled    
    #dynamic_object["runtime"]                          = func_app_sett.properties["FUNCTIONS_EXTENSION_VERSION"]
    dynamic_object["linux_fx_version"]                 = app_details.site_config.linux_fx_version
    dynamic_object["java_version"]                     = app_details.site_config.java_version
    dynamic_object["always_on"]                        = app_details.site_config.always_on
    dynamic_object["java_container_version"]           = app_details.site_config.java_container_version
    dynamic_object["availability_state"]               = app_details.availability_state
    dynamic_object["reserved"]                         = app_details.reserved
    dynamic_object["vnet_route_all_enabled"]           = app_details.vnet_route_all_enabled
    dynamic_object["vnet_image_pull_enabled"]          = app_details.vnet_image_pull_enabled
    dynamic_object["vnet_content_share_enabled"]       = app_details.vnet_content_share_enabled
    dynamic_object["client_cert_enabled"]              = app_details.client_cert_enabled
    dynamic_object["client_cert_mode"]                 = app_details.client_cert_mode
    dynamic_object["client_cert_exclusion_paths"]      = app_details.client_cert_exclusion_paths
    dynamic_object["suspended_till"]                   = app_details.suspended_till
    dynamic_object["max_number_of_workers"]            = app_details.max_number_of_workers
    dynamic_object["default_host_name"]                = app_details.default_host_name
    dynamic_object["slot_swap_status"]                 = app_details.slot_swap_status
    dynamic_object["https_only"]                       = app_details.https_only
    dynamic_object["redundancy_mode"]                  = app_details.redundancy_mode
    dynamic_object["public_network_access"]            = app_details.public_network_access
    dynamic_object["storage_account_required"]         = app_details.storage_account_required
    dynamic_object["key_vault_reference_identity"]     = app_details.key_vault_reference_identity    
    dynamic_object["managed_environment_id"]           = app_details.managed_environment_id
    dynamic_object["service_plan"]                     = app_details.server_farm_id.split("/")[-1]
    dynamic_object["server_farm_id"]                   = app_details.server_farm_id
    dynamic_object["virtual_network_subnet_id"]        = app_details.virtual_network_subnet_id
    dynamic_object["tags"]                             = app_details.tags
    dynamic_object["tags_count"]                       = len(app_details.tags.keys()) if app_details.tags else 0 
    dynamic_object["id"]                               = app_details.id
    dynamic_object["min_tls_version"]                  = app_details.site_config.min_tls_version
    dynamic_object["ip_restrictions_default_action"]   = app_details.site_config.ip_security_restrictions_default_action
    dynamic_object["ftps_state"]                       = app_details.site_config.ftps_state
    dynamic_object["public_network_access"]            = app_details.site_config.public_network_access
    dynamic_object["health_check_path"]                = app_details.site_config.health_check_path 



    # show only number of entries in the app settings as they night contain sensitive data
    dynamic_object["app_settings_count"] = len(app_sett.properties.keys())

    identity_enabled = app_details.identity and app_details.identity.type == 'SystemAssigned'
    dynamic_object["system_assigned_identity"] = identity_enabled
    
    # this depends in the runtime: todo in further release
    #dynamic_object["startup_cmd"] = app_sett.properties.get('appCommandLine') or app_sett.properties.get('WEBSITE_STARTUP_FILE')


    return dynamic_object



def serviceplan_select(plan_details):

    dynamic_object = {}

    # Add wanted properties
    dynamic_object["name"]                             = plan_details.name        
    dynamic_object["resource_group"]                   = plan_details.resource_group
    dynamic_object["id"]                               = plan_details.id
    dynamic_object["location"]                         = plan_details.location
    dynamic_object["kind"]                             = plan_details.kind
    dynamic_object["type"]                             = plan_details.type
    dynamic_object["status"]                           = plan_details.status                  
    dynamic_object["tags"]                             = plan_details.tags
    dynamic_object["tags_count"]                       = len(plan_details.tags.keys()) if plan_details.tags else 0     
    dynamic_object["provisioning_state"]               = plan_details.provisioning_state
    dynamic_object["sku_size"]                         = plan_details.sku.size
    dynamic_object["sku_tier"]                         = plan_details.sku.tier
    dynamic_object["sku_capacity"]                     = plan_details.sku.capacity
    dynamic_object["zone_redundant"]                   = plan_details.zone_redundant    


    return dynamic_object



def vm_select(vm_details):

    dynamic_object = {}

    
    dynamic_object["name"]                             = vm_details.name        
    #todo: fix in further release
    #dynamic_object["resource_group"]                   = vm_details.resource_group
    dynamic_object["id"]                               = vm_details.id
    dynamic_object["location"]                         = vm_details.location
    dynamic_object["type"]                             = vm_details.type                 
    dynamic_object["tags"]                             = vm_details.tags
    dynamic_object["tags_count"]                       = len(vm_details.tags)  if vm_details.tags else 0  
    dynamic_object["provisioning_state"]               = vm_details.provisioning_state
    dynamic_object["plan"]                             = vm_details.plan       
    dynamic_object["installed_extensions"]             = len(vm_details.resources)
    dynamic_object["zones"]                            = vm_details.zones
    dynamic_object["managed_by"]                       = vm_details.managed_by
    dynamic_object["vm_size"]                          = vm_details.hardware_profile.vm_size
    dynamic_object["image_id"]                         = vm_details.storage_profile.image_reference.id
    dynamic_object["image_publisher"]                  = vm_details.storage_profile.image_reference.publisher
    dynamic_object["image_version"]                    = vm_details.storage_profile.image_reference.version
    dynamic_object["os_type"]                          = vm_details.storage_profile.os_disk.os_type
    dynamic_object["os_image"]                         = vm_details.storage_profile.os_disk.image
    dynamic_object["data_disks_count"]                 = len(vm_details.storage_profile.data_disks)
    dynamic_object["availability_set"]                 = vm_details.availability_set.id if vm_details.availability_set else None
    dynamic_object["priority"]                         = vm_details.priority
    dynamic_object["eviction_policy"]                  = vm_details.eviction_policy
    dynamic_object["ultra_ssd_enabled"]                = vm_details.additional_capabilities.ultra_ssd_enabled if vm_details.additional_capabilities else None
    dynamic_object["status"]                           = vm_details.instance_view.statuses[1].display_status if vm_details.instance_view else "Unknown"
    
    #note: only one subnet is returned(linked to the first NIC), a VM may be attached into multiple subnets
    # to get subnet will need to use azure.mgmt.network, todo: fix in further release
    #dynamic_object["subnet"]                          = vm_details.network_profile.network_interface_configurations[0].ip_configurations[0].subnet.id
    
    nic_list = ""
    # Iterate through the network interfaces associated with the VM
    for network_interface_reference in vm_details.network_profile.network_interfaces:
    # Extract the network interface name from the reference
        network_interface_name = network_interface_reference.id.split('/')[-1]
        nic_list = nic_list  + network_interface_name + " ; "

    dynamic_object["nic_list"]                        = nic_list


    #todo: fix in further release
    #dynamic_object["auto_shutdown_status"]            = vm_details.virtual_machine_profile.scheduled_events_profile.auto_shutdown_status
    
    #todo: fix in further release
    #dynamic_object["public_ip"]                          = vm_details.network_profile.network_interface_configurations[0].public_ip_address_configuration.public_ip_prefix.id

     
    identity_enabled = (vm_details.identity and vm_details.identity.type == 'SystemAssigned') or  vm_details.identity is not None
    dynamic_object["system_assigned_identity"] = identity_enabled

    dynamic_object["encryption_at_host"] = vm_details.security_profile.encryption_at_host if vm_details.security_profile else None
    
    return dynamic_object


