# app.py
from flask import Flask, request, jsonify, render_template
import psycopg2
import pandas as pd
import re

app = Flask(__name__)

def connect_to_db(host, port, dbname, user, password):
    conn = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/connect', methods=['POST'])
def db_connect():
    data = request.json
    try:
        conn = connect_to_db(data['host'], data['port'], data['dbname'], data['user'], data['password'])
        cursor = conn.cursor()
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        tables = [table[0] for table in cursor.fetchall()]
        conn.close()
        return jsonify({"message": "Connected successfully", "tables": tables}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/get_columns', methods=['POST'])
def get_columns():
    data = request.json
    try:
        conn = connect_to_db(data['host'], data['port'], data['dbname'], data['user'], data['password'])
        cursor = conn.cursor()
        cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{data['table']}'")
        columns = [column[0] for column in cursor.fetchall()]
        conn.close()
        return jsonify({"columns": columns}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/check', methods=['POST'])
def quality_check():
    data = request.json
    conn = connect_to_db(data['host'], data['port'], data['dbname'], data['user'], data['password'])
    cursor = conn.cursor()
    
    table = data['table']
    columns = data['columns']
    checks = data['checks']
    
    results = {}
    
    if 'null_check' in checks:
        results['null_check'] = null_check(cursor, table, columns)
    
    if 'numeric_distribution' in checks:
        results['numeric_distribution'] = numeric_distribution(cursor, table, columns)
    
    if 'inaccurate_data' in checks:
        results['inaccurate_data'] = inaccurate_data(cursor, table, columns)
    
    if 'data_variety' in checks:
        results['data_variety'] = data_variety(cursor, table, columns)
    
    conn.close()
    return jsonify(results), 200

def null_check(cursor, table, columns):
    results = {}
    for column in columns:
        cursor.execute(f"SELECT COUNT(*) FROM {table} WHERE {column} IS NULL")
        count = cursor.fetchone()[0]
        results[column] = count
    return results

def numeric_distribution(cursor, table, columns):
    results = {}
    for column in columns:
        cursor.execute(f"SELECT {column} FROM {table} WHERE {column} IS NOT NULL")
        data = pd.DataFrame(cursor.fetchall(), columns=[column])
        results[column] = {
            'min': float(data[column].min()),
            'max': float(data[column].max()),
            'mean': float(data[column].mean()),
            'median': float(data[column].median()),
            'std': float(data[column].std())
        }
    return results

def inaccurate_data(cursor, table, columns):
    results = {}
    pattern = r'[*&!@#$%^()]'
    for column in columns:
        cursor.execute(f"SELECT COUNT(*) FROM {table} WHERE {column}::text ~ '{pattern}'")
        count = cursor.fetchone()[0]
        results[column] = count
    return results

def data_variety(cursor, table, columns):
    results = {}
    for column in columns:
        cursor.execute(f"SELECT COUNT(DISTINCT {column}) FROM {table}")
        unique_count = cursor.fetchone()[0]
        results[column] = unique_count
    return results

if __name__ == '__main__':
    app.run(debug=True)