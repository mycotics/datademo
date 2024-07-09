import os

from prefect import flow, task

# from prefect_airbyte.server import AirbyteServer
# from prefect_airbyte.connections import AirbyteConnection, AirbyteSyncResult
# from prefect_airbyte.flows import run_connection_sync
#
# from prefect_dbt.cli.commands import DbtCoreOperation

# remote_airbyte_server = AirbyteServer(
#     username="airbyte",
#     password=os.getenv("AIRBYTE_PASSWORD"),
#     server_host="localhost",
#     server_port="8000"
# )
#
# remote_airbyte_server.save("my-remote-airbyte-server", overwrite=True)
#
# airbyte_connection = AirbyteConnection(
#     airbyte_server=remote_airbyte_server,
#     connection_id="...my_airbyte_connection_id...",  # Replace the value with your Airbyte connection ID
#     status_updates=True,
# )


@task(name="Extract, Load with Airbyte 1")
def run_airbyte_sync1() -> str:
    return 'testing1  '
    # job_run = connection.trigger()
    # job_run.wait_for_completion()
    # return job_run.fetch_result()


@task(name="Extract, Load with Airbyte 2")
def run_airbyte_sync2() -> str:
    return 'testing2'
    # job_run = connection.trigger()
    # job_run.wait_for_completion()
    # return job_run.fetch_result()

@task(name="Extract, Load with Airbyte 3")
def run_airbyte_sync3(a, b) -> str:
    print('||||'.join([a,b]) )
    return ','.join([a,b])
    # return ','.join([a,b])
    # job_run = connection.trigger()
    # job_run.wait_for_completion()
    # return job_run.fetch_result()

# def run_dbt_commands(commands, prev_task_result):
#     dbt_task = DbtCoreOperation(
#         commands=commands,
#         project_dir="../dbt_project",
#         profiles_dir="../dbt_project",
#         wait_for=prev_task_result
#     )
#     return dbt_task


@flow(log_prints=True)
def my_elt_flow():
    # run Airbyte sync
    airbyte_sync_result1 = run_airbyte_sync1.submit()
    airbyte_sync_result2 = run_airbyte_sync2.submit()
    airbyte_sync_result3 = run_airbyte_sync3.submit(airbyte_sync_result1, airbyte_sync_result2)

    # a = airbyte_sync_result3.result()
    # a = airbyte_sync_result1.result()
    # a = airbyte_sync_result2.result()

    a = airbyte_sync_result3.result()

    return a


if __name__ == "__main__":
    my_elt_flow()