from pgsql import connect, meta

if __name__ == '__main__':
    schema_name = "raw"  # Replace with the desired schema name if needed
    engine = connect.get_engine()
    tables = meta.list_tables(engine, schema_name)
    mens_tables = meta.list_mncaa_tables(tables)
    tables.sort()
    whitespace = 31
    for table in tables:
        if table in mens_tables:
            check = "✅"
        else:
            check = "❌"
        spaces = whitespace - len(table)
        print(f"- {table+' '*spaces}\t{check}")