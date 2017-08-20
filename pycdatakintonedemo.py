# -*- coding: utf-8 -*-
import pyodbc
import sys

def Main(event, context):
    print('************************************************')
    print('\t\t Kintone Demo')
    print('This demo uses the CData ODBC for Kintone')
    print('************************************************')
    print('option:1,               - List all the tables in the database')
    print('option:2, table:name    - List all the columns for a specific table')
    print('option:3, table:name    - Select data from table')
    print('option:4, sql:statement - Custom SQL Query')
    print('------------------------------------------------')

    connStr =  'Driver={./cdata/libkintoneodbc.x64.so};' + event['conn_str']
    conn = pyodbc.connect(connStr)

    if event['option'] == '1':
        for table in conn.cursor().tables():
            print(table.table_name)
    elif event['option'] == '2':
        tableName = event['table']
        for column in conn.cursor().columns(tableName):
            print(column.column_name)
    elif event['option'] == '3':
        tableName = event['table']
        c = conn.cursor();
        c.execute('SELECT * FROM ' + tableName)
        for row in c.fetchall():
            print(row)
    elif event['option'] == '4':
        sql = event['sql']
        c = conn.cursor();
        c.execute(sql)
        for row in c.fetchall():
            print(row)
    else:
            print('Invalid option')

    conn.close();

    return {
        'status' : 'finish'
    }
