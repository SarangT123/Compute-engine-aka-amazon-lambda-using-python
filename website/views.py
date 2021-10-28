from flask import render_template, url_for, flash, redirect, session, request
from website import app
from website.serverless_functions import *

key = "Put ur token"


@app.route('/<token>')
@app.route('/run/ping/<token>')
def ping_server(token):
    if key == token:
        return ping()
    else:
        return "access denied"


@app.route('/run/<func>/<token>')
@app.route('/run/<func>/<token>/<args>')
def ping_server_main(token, func="ping", args=[]):
    if key == token:
        try:
            print(type(args))
            if isinstance(args, str):
                print(True)
                args = args.split(',')
            print(type(args))
            return eval(func)(*args)
        except NameError as e:
            return e
    else:
        return "access denied"
