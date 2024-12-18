from flask import Blueprint, render_template, request, redirect, url_for
from models import Customer
import json

api_bp = Blueprint("api", __name__, url_prefix="/api")