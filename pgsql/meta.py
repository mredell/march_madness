from sqlalchemy import inspect

def list_tables(engine, schema=None):
    """Lists all tables in a PostgreSQL database schema.
    Args:
        schema (str, optional): The schema name. Defaults to 'public'.
    """
    inspector = inspect(engine)
    return inspector.get_table_names(schema=schema)

def list_mncaa_tables(tables):
    """Scrubs the database tables for only the MNCAA data."""
    return [table for table in tables if (table[0]!="W") and ("Stage1" not in table)]

def list_table_columns(engine, schema, table_name):
    inspector = inspect(engine)
    columns = inspector.get_columns(table_name, schema=schema)
    return [column['name'] for column in columns]