from html.parser import HTMLParser
from enum import Enum


class AocStatus(Enum):
    DEFAULT = 1
    OK = 2
    KO = 3
    ALREADY = 4
    WAITING = 5
    UNKNOWN = 6


class AocHtmlParser(HTMLParser):
    def __init__(self, *args):
        self.in_body = False
        self.in_main = False
        self.in_article = False
        self.in_p = False

        self.status = AocStatus.DEFAULT
        self.message = ""

        super().__init__(*args)

    def handle_starttag(self, tag, attrs):
        if tag == "body":
            self.in_body = True
        if tag == "main" and self.in_body:
            self.in_main = True
        if tag == "article" and self.in_main:
            self.in_article = True
        if tag == "p" and self.in_article:
            self.in_p = True

    def handle_endtag(self, tag):
        if tag == "body":
            self.in_body = False
        if tag == "main" and self.in_body:
            self.in_main = False
        if tag == "article" and self.in_main:
            self.in_article = False
        if tag == "p" and self.in_article:
            self.in_p = False

    def handle_data(self, data):
        if self.in_p and self.status == AocStatus.DEFAULT:
            if data.startswith("You don't seem to be solving the right level."):
                self.status = AocStatus.ALREADY
                self.message = "This level has already been solved."
            elif data.startswith("That's not the right answer"):
                self.status = AocStatus.KO
                self.message = list(data.split('.'))[0]
            elif data.startswith("That's the right answer!"):
                self.status = AocStatus.OK
                self.message = "That's the right answer!"
            elif data.startswith("You gave an answer too recently"):
                self.status = AocStatus.WAITING
                self.message = list(data.split('.'))[1] + " to be able to submit again."
            else:
                self.status = AocStatus.UNKNOWN