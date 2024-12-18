from flask import Blueprint, render_template, request, redirect, url_for
from models import Customer
import json

from .base import api_bp