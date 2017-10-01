#! /bin/bash
BASE_URL=http://127.0.0.1:8000

USERNAME='imperatorsboy'
PASSWORD='4julian'
TITLE='Say+welcome+to+Bilbo!'
FILE_PATH='demo/bilbo.jpg'
BODY="isn't+he+JUST+SO+CUTE!!!"

command="curl -X POST"
command="$command -u $USERNAME:$PASSWORD"
command="$command --data-urlencode title='$TITLE'"
command="$command --data-urlencode body='$BODY'"
command="$command --data-urlencode file=@$FILE_PATH"
command="$command $BASE_URL/puppies/"

echo ">>$command"
echo

$command
