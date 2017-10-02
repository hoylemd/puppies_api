#! /bin/bash
HEADERS='Accept:application/json;'
BASE_URL=http://127.0.0.1:8000

USERNAME='imperatorsboy'
PASSWORD='4julian'
FIRST_NAME='Cassius'
LAST_NAME='au+Belowna'
EMAIL='cassius@aubelowna.com'

DATA="username=$USERNAME&password=$PASSWORD&first_name=$FIRST_NAME"
DATA="$DATA&last_name=$LAST_NAME&email=$EMAIL"

command="curl -H \"$HEADERS\" -X POST -d $DATA $BASE_URL/register"

echo ">>$command"
echo

echo $($command) | python -m json.tool
