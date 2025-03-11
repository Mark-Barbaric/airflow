## Fundamental Concepts

### Using Astro CLI

Installation

>`https://www.astronomer.io/docs/astro/cli/install-cli/?tab=linux#install-the-astro-cli`

Initialize astro environment

>`astro dev init`

Start astro environment

>`astro dev start`

Login credentials

username: admin\
password: admin

### General Commands

*Running an airflow server*

>`airflow webserver`

username: airflow\
password: airflow

### Tutorial Commands

*Running the script*

>`python ~/airflow/dags/tutorial.py`

*Command Line Metadata Validation*

>`airflow db migrate`

>`airflow dags list`

>`airflow tasks list tutorial`

>`airflow tasks list tutorial --tree`

*Testing*

>`airflow tasks test tutorial print_date 2015-06-01`

>`airflow tasks test tutorial sleep 2015-06-01`

*Testing templated*

>`airflow tasks test tutorial templated 2015-06-01`