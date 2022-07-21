#!/usr/bin/python

import sqlite3

class SqlObj(object): pass

def execute(sql, sdata=None):
    with sqlite3.connect('test.db') as conn:
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        if sdata:
            r = c.execute(sql, sdata)
        else:
            r = c.execute(sql)
        rows = [
            _row_factory(row)
            for row in r
        ]
        result = SqlObj()
        result.rows = rows
        result.found_count = len(rows)
        result.new_rec_id = c.lastrowid
        c.close()
    return result
        
def _row_factory(row):
    return {
        k: row[k]
        for k in row.keys()
    }