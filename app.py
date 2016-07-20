# bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from random import choice

app = Flask(__name__)

EMOJI = [u'🍄', u'🍕', u'🍪', u'🎨', u'🐌', u'🐦', u'🐶',
         u'👽', u'💀', u'💎', u'💜', u'💩', u'💰', u'🔮',
         u'🙃', u'🚀', u'🤑', u'🦀', u'🦄']


@app.route('/')
def home():
    """Home page"""

    random_emoji = choice(EMOJI)

    return render_template('index.html', emoji=random_emoji)

if __name__ == '__main__':
    # server checks for changes
    # better error messages

    app.run(debug=True)
