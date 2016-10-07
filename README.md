excel2mysql
===========

Migrate data from Excel (xlsx file) to MySQL.


Usage
-----

1. Change `create.sql` in `/path/to/excel2mysql/excel2mysql/settings/sqls/` to your table schema.
2. Change MySQL settings in `/path/to/excel2mysql/excel2mysql/settings/database_config.py`.
3. Change Excel settings in `/path/to/excel2mysql/excel2mysql/settings/excel_config.py`.
4. Make sure you can connect to target MySQL server correctly.
5. Run the script:

    Option 1
    
        $ python excel2mysql
        
    Option 2
    
        $ cd /path/to/excel2mysql/
        $ python main.py
        
    Option 3
    
        $ cd /path/to/excel2mysql/
        $ python -m excel2mysql
