from src import business
from src import utils
import logging
import click
import shutil
import os

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)




def handle_functionapp(ctx, resource_name1, rg_name1, resource_name2, rg_name2, output, debug):
    
    logging.info("Starting..")
    logging.info("Fetching data from Azure Cloud..")
    subscription_id = ctx.obj['SUBSCRIPTION_ID']

    func1=business.get_details_function_app(rg_name1, resource_name1, subscription_id)
    func2=business.get_details_function_app( rg_name2, resource_name2, subscription_id)
    logging.info("Data fetched.")
    logging.info("Exporting..")
    terminal_width, _ = shutil.get_terminal_size()
    utils.print_dict(func1, func2, terminal_width)

    if output is not False:
        utils.dict_to_csv(func1,func2, output)


def handle_appservice(ctx, resource_name1, rg_name1, resource_name2, rg_name2, output, debug):
    
    logging.info("Starting..")
    logging.info("Fetching data from Azure Cloud..")
    subscription_id = ctx.obj['SUBSCRIPTION_ID']

    app1=business.get_details_appservice(rg_name1, resource_name1, subscription_id)
    app2=business.get_details_appservice( rg_name2, resource_name2, subscription_id)
    logging.info("Data fetched.")
    logging.info("Exporting..")
    terminal_width, _ = shutil.get_terminal_size()
    utils.print_dict(app1, app2, terminal_width)

    if output is not False:
        utils.dict_to_csv(app1,app2, output)


def handle_serviceplan(ctx, resource_name1, rg_name1, resource_name2, rg_name2, output, debug):
    
    logging.info("Starting..")
    logging.info("Fetching data from Azure Cloud..")
    subscription_id = ctx.obj['SUBSCRIPTION_ID']

    plan1=business.get_details_serviceplan(rg_name1, resource_name1, subscription_id)
    plan2=business.get_details_serviceplan( rg_name2, resource_name2, subscription_id)
    logging.info("Data fetched.")
    logging.info("Exporting..")
    terminal_width, _ = shutil.get_terminal_size()
    utils.print_dict(plan1, plan2, terminal_width)

    if output is not False:
        utils.dict_to_csv(plan1,plan2, output)

def handle_vm(ctx, resource_name1, rg_name1, resource_name2, rg_name2, output, debug):
    
    logging.info("Starting..")
    logging.info("Fetching data from Azure Cloud..")
    subscription_id = ctx.obj['SUBSCRIPTION_ID']

    vm1=business.get_details_vm(rg_name1, resource_name1, subscription_id)
    vm2=business.get_details_vm( rg_name2, resource_name2, subscription_id)
    logging.info("Data fetched.")
    logging.info("Exporting..")
    terminal_width, _ = shutil.get_terminal_size()
    utils.print_dict(vm1, vm2, terminal_width)

    if output is not False:
        utils.dict_to_csv(vm1,vm2, output)





@click.group()
@click.option('--debug/--no-debug', default=False, help="Enable debug mode")
@click.pass_context
def cli(ctx, debug):
    click.echo(f"Debug mode is {'on' if debug else 'off'}")
    ctx.ensure_object(dict)
    ctx.obj['DEBUG'] = debug
    # check and get subscription_id here from env var then pass it further
    env_variable_name = "SUBSCRIPTION_ID"
    env_variable_value = os.environ.get(env_variable_name)
    if env_variable_value is not None:
        ctx.obj['SUBSCRIPTION_ID'] = env_variable_value
    else:
        print(f"{env_variable_name} is not set.")
        logging.error(f" ENV Variable {env_variable_name} is not set.")
        exit(1)



@cli.command()  
@click.option('--resource_name1', help="The name of the first resource")
@click.option('--rg_name1', help="The resource group of the first resource")
@click.option('--resource_name2', help="The name of the second resource")
@click.option('--rg_name2', help="The resource group of the second resource")
@click.option("--output", default=False, help="Export the output as csv")
@click.option('--debug/--no-debug', default=False, help="Enable debug mode")
@click.pass_context
def functionapp(ctx, resource_name1, rg_name1, resource_name2, rg_name2, output, debug):
    if any(item is  None for item in [resource_name1, resource_name2, rg_name1, rg_name2 ]):
        print ("please provide the params: --resource_name1 , --rg_name1 , --resource_name2 , --rg_name2")
        click.echo(cli.get_command(ctx, "functionapp").get_help(ctx))
    else:      
        handle_functionapp(ctx, resource_name1, rg_name1, resource_name2, rg_name2, output, debug)


@cli.command()  
@click.option('--resource_name1', help="The name of the first resource")
@click.option('--rg_name1', help="The resource group of the first resource")
@click.option('--resource_name2', help="The name of the second resource")
@click.option('--rg_name2', help="The resource group of the second resource")
@click.option("--output", default=False, help="Export the output as csv")
@click.option('--debug/--no-debug', default=False, help="Enable debug mode")
@click.pass_context
def appservice(ctx, resource_name1, rg_name1, resource_name2, rg_name2, output, debug):
    if any(item is  None for item in [resource_name1, resource_name2, rg_name1, rg_name2 ]):
        print ("please provide the params: --resource_name1 , --rg_name1 , --resource_name2 , --rg_name2")
        click.echo(cli.get_command(ctx, "appservice").get_help(ctx))
    else:     
        handle_appservice(ctx, resource_name1, rg_name1, resource_name2, rg_name2, output, debug)


@cli.command()  
@click.option('--resource_name1', help="The name of the first resource")
@click.option('--rg_name1', help="The resource group of the first resource")
@click.option('--resource_name2', help="The name of the second resource")
@click.option('--rg_name2', help="The resource group of the second resource")
@click.option("--output", default=False, help="Export the output as csv")
@click.option('--debug/--no-debug', default=False, help="Enable debug mode")
@click.pass_context
def serviceplan(ctx, resource_name1, rg_name1, resource_name2, rg_name2, output, debug):
    if any(item is  None for item in [resource_name1, resource_name2, rg_name1, rg_name2 ]):
        print ("please provide the params: --resource_name1 , --rg_name1 , --resource_name2 , --rg_name2")
        click.echo(cli.get_command(ctx, "serviceplan").get_help(ctx))
    else: 
        handle_serviceplan(ctx, resource_name1, rg_name1, resource_name2, rg_name2, output, debug)


@cli.command()  
@click.option('--resource_name1', help="The name of the first resource")
@click.option('--rg_name1', help="The resource group of the first resource")
@click.option('--resource_name2', help="The name of the second resource")
@click.option('--rg_name2', help="The resource group of the second resource")
@click.option("--output", default=False, help="Export the output as csv")
@click.option('--debug/--no-debug', default=False, help="Enable debug mode")
@click.pass_context
def vm(ctx, resource_name1, rg_name1, resource_name2, rg_name2, output, debug):
    if any(item is  None for item in [resource_name1, resource_name2, rg_name1, rg_name2 ]):
        print ("please provide the params: --resource_name1 , --rg_name1 , --resource_name2 , --rg_name2")
        click.echo(cli.get_command(ctx, "vm").get_help(ctx))
    else:    
        handle_vm(ctx, resource_name1, rg_name1, resource_name2, rg_name2, output, debug)






if __name__ == '__main__':
    cli(obj={})





