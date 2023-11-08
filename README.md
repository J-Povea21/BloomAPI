# BloomAPI

Hi! In this repo is stored the BloomFilter API that we've created for our Data Structures class


## Installation
In order to use this API, first clone the repository via http/ssh or download the zip in the **<>code** section. In this example, we'll
clone the repository via **ssh**:

```bash
git clone git@github.com:J-Povea21/BloomAPI.git
```

Once you've cloned the repo, install the necessary dependencies. You can do it by using the requeriements.txt file:

```bash
pip install -r requirements.txt
```

## Database and migrations
The idea of this implementation is to use a database and show how we can reduce the amount of queries to the database using
the bloom filter. You can use whatever database you like, but in this case we're going to use sqlite3, SQLAlchemy and alembic to
manage the migrations and the database.

### Set an url for the database
In the **database.py** file located in the _src/db_ folder you'll find a variable called **DB_URL** that is set to a default value. Right
now, it looks like this:

```python
DB_URL = "sqlite:///./DB_NAME.sqlite3"
```

You'll need to change the **DB_NAME** part to the name of the database you created in the previous step (in case you're using sqlite3, of course)

### Creating the migrations
Fine! Now we're gonna use alembic to create the migrations. The **first step** is create an _alembic.ini_ file. To do this, run the following
command:

```bash
alembic init migration_folder
```

The _migration_folder_ is the name of the folder where you want to allocate the migrations. In this case, we're gonna called _migrations_. At
this point, our project structure should look like this:

    ```
    alembic.ini
    migrations/
            other_files.py
    src/
       other_folders/

    ```

### Running the first migration
Now, we're gonna create the first migration. To do this, run the following command:

```bash
alembic revision -m "First migration"
```

This will create a file in the _migrations/versions_ folder. This file will have a name like this: **_first_migration.py**. Open this file and
you'll see a function called **upgrade()**. This function is where you'll write the code to create the tables in the database. In this case,
we need to create a table called **users** with the columns _id_, _username_ , _password_ and _is_active_:

```python
def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('username', sa.String, unique=True, index=True),
        sa.Column('password', sa.String),
        sa.Column('is_active', sa.Boolean, default=True)
    )


def downgrade() -> None:
    op.drop_table('users') # This one is a fn we can use if we want to go back
```

With this, you can run the migration. To do this, run the following command:

```bash
alembic upgrade head
```
where **head** is the most recent revision. Note that the **upgrade** argument is basically calling
the **upgrade()** function in our revision file which is the one that is creating the table in the
database. 

### Testing
With this, you're done! To test the API, run the following command and test the different methods
in the docs route (http://localhost:8000/docs):

```bash
uvicorn src.main:app --reload
```

## Members of the project
Finally, these are the members of the project:
- Juan Andrés Povea
- Jesús David Cantillo
- Yovany Zhu
- Carlos Elías López