#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that causes the server to respond  You got me!
curl -o /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me
