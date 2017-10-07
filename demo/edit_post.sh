#! /bin/bash
HEADERS='Accept:application/json;'
BASE_URL=http://127.0.0.1:8000

USERNAME='cloudknight'
PASSWORD='4julian'

DATA="title=ubeenhacked"

command="curl -H \"$HEADERS\" -X PATCH -d $DATA $BASE_URL/puppies/3/ -u $USERNAME:$PASSWORD"
eATA="$DATA&last_name=$LAST_NAME&emal=$EMAIL"

echo ">>$command"
echo

echo $($command) | python -m json.tool
