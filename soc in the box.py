import os
import time
import sqlite3
from datetime import datetime
import re
from flask import Flask, jsonify
import threading

def collect_logs(log_files):
    findings = []
    for log_file in log_files:
        with open(log_file, 'r') as f:
            for line in f:
                findings.append((datetime.now(), log_file, line))
    return findings

def ssh_brute_force(line):
    # Implement your SSH brute force detection logic here
    pass

def repeated_404(line):
    # Implement your repeated 404 errors detection logic here
    pass

def sql_injection(line):
    # Implement your SQL injection detection logic here
    pass

def xss_attempt(line):
    # Implement your XSS attempts detection logic here
    pass

def analyze_log(line, db):
    if ssh_brute_force(line) or repeated_404(line) or sql_injection(line) or xss_attempt(line):
        db.insert_alert((datetime.now(), 'SSH Brute Force', line, re.search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', line).group(0)))
        db.insert_alert((datetime.now(), 'Repeated 404', line, re.search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', line).group(0)))
        db.insert_alert((datetime.now(), 'SQL Injection', line, re.search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', line).group(0)))
        db.insert_alert((datetime.now(), 'XSS Attempt', line, re.search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', line).group(0)))

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS alerts (timestamp INTEGER, type TEXT, description TEXT, source IP TEXT)''')

def insert_alert(conn, alert):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO alerts (timestamp, type, description, source IP) VALUES (?, ?, ?, ?)", alert)
    conn.commit()

def connect_db():
    return sqlite3.connect('alerts.db')

app = Flask(__name__)

@app.route('/alerts', methods=['GET'])
def get_alerts():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alerts")
    results = cursor.fetchall()
    return jsonify([{'timestamp': result[0], 'type': result[1], 'description': result[2], 'source IP': result[3]} for result in results])

def main():
    log_files = ['/var/log/syslog', '/var/log/auth.log', '/var/log/nginx/access.log'] if os.path.exists('/var/log/nginx') else ['/var/log/syslog', '/var/log/auth.log']
    db = connect_db()
    create_table(db)

    def analyze_logs():
        while True:
            findings = collect_logs(log_files)
            for finding in findings:
                analyze_log(finding[2], db)
            time.sleep(1)

    threading.Thread(target=analyze_logs).start()
    app.run(port=5000, host='0.0.0.0')
