from flask import Flask, jsonify, request
import sqlite3

def connect_db():
    # Change 'alerts.db' to your actual database file if needed
    return sqlite3.connect('alerts.db')

app = Flask(__name__)

@app.route('/alerts', methods=['GET'])
def get_alerts():
    filter_ip = request.args.get('ip')
    filter_type = request.args.get('type')
    filter_severity = request.args.get('severity')
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')

    conn = connect_db()
    cursor = conn.cursor()
    query = f"SELECT * FROM alerts WHERE 1=1"

    if filter_ip:
        query += f" AND source IP='{filter_ip}'"
    if filter_type:
        query += f" AND type='{filter_type}'"
    if filter_severity:
        query += f" AND severity='{filter_severity}'"
    if start_time and end_time:
        query += f" AND timestamp BETWEEN '{start_time}' AND '{end_time}'"

    cursor.execute(query)
    results = cursor.fetchall()
    return jsonify([{'timestamp': result[0], 'type': result[1], 'description': result[2], 'source IP': result[3]} for result in results])

if __name__ == "__main__":
    app.run(port=5001, host='0.0.0.0')
