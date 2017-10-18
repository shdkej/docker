#!/bin/bash

crontab -e
expect 4
* * * * * test
