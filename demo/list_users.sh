#! /bin/bash
HEADERS='Accept:application/json;'
BASE_URL=http://127.0.0.1:8000

USERNAME='imperatorsboy'
PASSWORD='4julian'

command="curl -H \"$HEADERS\" -u $USERNAME:$PASSWORD $BASE_URL/users/"

echo ">>$command"
echo

echo $($command) | python -m json.tool
