#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import cgi
import webapp2
from helpers import alphabet_position, rotate_character
from caesar import encrypt

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>ROT13</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
        Welcome to my Caesar cypher page!
    </h1>
"""

inputForm = '''
<form method="post">
    <label>Enter the text you'd like to encrypt</label>
    <input name="text" type="text" value="%(text)s">
    <br>
    <label>How many would you like to rotate by?</label>
    <input name="rotNum" type="text" value="%(rotNum)s">
    <input type="submit" value="go">
</form>
'''
page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
    def get(self):
        response = page_header + inputForm % {"text": "", "rotNum": ""} + page_footer
        self.response.write(response)

    def post(self):
        key1 = self.request.get("text")
        key2 = self.request.get("rotNum")
        rotated = encrypt(key1, int(key2))


        response = page_header + inputForm + page_footer
        self.response.write(page_header)
        self.response.write(inputForm % {"text": rotated, "rotNum": key2})









    '''
class Rotation(webapp2.RequestHandler):
    def post(self):
        text = self.request.get("text")
        rotNum = self.request.get("rotNum")
        edit_header = "<h2>Your text has been encrypted</h2>"
        newText = "<p>" + encrypt(text, rotNum) + "</p>"
        sentence = "<p>" + "Here is your rotated text." + "</p>"
        response = page_header + sentence + "<br>" + "<strong>" + newText +"</strong>" + page_footer
        self.response.write(response)
'''
app = webapp2.WSGIApplication([
    ('/', Index)
#    ('/encrypt', Rotation)
], debug=True)
