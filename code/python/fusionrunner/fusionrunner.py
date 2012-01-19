#!/usr/bin/python
""" FusionRunner

Queries Google Fusion Tables for MyTracks data.
"""
__author__ = 'hardware.hank@gmail.com (Erik Gregg)'
import sys, getpass
sys.path.append("./fusion-tables-client-python-read-only/src/")
from authorization.oauth import OAuth
from sql.sqlbuilder import SQL
import ftclient
from fileimport.fileimporter import CSVImporter

if __name__ == "__main__":
  consumer_key = "207320244638.apps.googleusercontent.com"
  f = open('secret')
  try:
    consumer_secret = f.readline().rstrip()
    print consumer_secret
  finally:
    f.close()
#  
#  url, token, secret = OAuth().generateAuthorizationURL(consumer_key, consumer_secret, consumer_key)
#  print "Visit this URL in a browser: "
#  print url
#  raw_input("Hit enter after authorization")
#  
#  token, secret = OAuth().authorize(consumer_key, consumer_secret, token, secret)
  token = "1/9rGx1JkAF8UtTSJKK1eSrqPznrZ-eYv1nE76Hb932Ho"
  secret = "6W7xLwgsiztHm-eOxFqaL20S"
  oauth_client = ftclient.OAuthFTClient(consumer_key, consumer_secret, token, secret)
  print "Token: ", token
  print "Secret: ", secret

  #show tables
  results = oauth_client.query(SQL().showTables())
  print results