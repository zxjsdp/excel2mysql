excel2mysql
===========

Migrate data from Excel (xlsx file) to MySQL.


Usage
-----

1. Change `create.sql` in `/path/to/excel2mysql/excel2mysql/settings/sqls/` to your own table schema.

    The table described in `create.sql` will be created if not exist.
    
    You can drop the old table and create new one by adding force option.

2. Change MySQL settings in `/path/to/excel2mysql/excel2mysql/settings/database_config.py`.

    You should change basic database settings. For example, *host*, *port*, *username*, *password*, *database name*.
    
    You should also change ignored column names whose value will be inserted into table automatically. For example, *id*, *created_at*, *updated_at*.

3. Change Excel settings in `/path/to/excel2mysql/excel2mysql/settings/excel_config.py`.

    Change the header setting if first line of your excel file is not header row.

4. Make sure you can connect to target MySQL server correctly.

5. Run excel2mysql to do data migration:

    Option 1 (recommended):
    
        $ python excel2mysql
        
    Option 2:
    
        $ cd /path/to/excel2mysql/
        $ python main.py
        
    Option 3:
    
        $ cd /path/to/excel2mysql/
        $ python -m excel2mysql
