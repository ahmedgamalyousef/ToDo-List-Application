from flask import Flask, render_template, request, redirect, url_for
import pymysql
import os

app = Flask(__name__)