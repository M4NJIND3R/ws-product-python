# -*- coding: utf-8 -*-

import os
from flask import Flask, jsonify
import sqlalchemy
from requestor import requestor
from limiter import limit_client_request


# web app
app = Flask(__name__)

# database engine
engine = sqlalchemy.create_engine(os.getenv('SQL_URI'))



@app.route('/')
def index():
    limit_client_request()
    return 'Welcome to EQ Works 😎'


@app.route('/events/hourly')
def events_hourly():
    limit_client_request(1,2)
    return query_helper('''
        SELECT date, hour, events
        FROM public.hourly_events
        ORDER BY date, hour
        LIMIT 168;
    ''')


@app.route('/events/daily')
def events_daily():
    limit_client_request(1,2)
    return query_helper('''
        SELECT date, SUM(events) AS events
        FROM public.hourly_events
        GROUP BY date
        ORDER BY date
        LIMIT 7;
    ''')


@app.route('/stats/hourly')
def stats_hourly():
    limit_client_request(1,2)
    return query_helper('''
        SELECT date, hour, impressions, clicks, revenue
        FROM public.hourly_stats
        ORDER BY date, hour
        LIMIT 168;
    ''')


@app.route('/stats/daily')
def stats_daily():
    limit_client_request(1,2)
    return query_helper('''
        SELECT date,
            SUM(impressions) AS impressions,
            SUM(clicks) AS clicks,
            SUM(revenue) AS revenue
        FROM public.hourly_stats
        GROUP BY date
        ORDER BY date
        LIMIT 7;
    ''')

@app.route('/poi')
def poi():
    limit_client_request(1,2)
    return query_helper('''
        SELECT *
        FROM public.poi;
    ''')

def query_helper(query):
    limit_client_request(1,2)
    with engine.connect() as conn:
        result = conn.execute(query).fetchall()
        return jsonify([dict(row.items()) for row in result])
