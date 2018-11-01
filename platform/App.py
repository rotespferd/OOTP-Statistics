from flask import Flask, Request


class App(Flask):
    request_class = Request