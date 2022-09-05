#!/bin/sh
sleep 20
mongoimport --jsonArray -d test -c users data.json
mongoimport --jsonArray -d test -c users data1.json
mongoimport --jsonArray -d test -c users data2.json
mongo myDbName
db.mycollection.findOne()
show collections

