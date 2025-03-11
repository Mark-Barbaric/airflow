from dags.astro_example_dag import example_astronauts


def test_example_astronauts():
    """
    test if a DAG has retries set
    """
    dag = example_astronauts()
    assert dag.default_args.get("retries", None) >= 2