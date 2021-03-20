FILE=docker-compose.yml
if [ ! -f "$FILE" ]
then
    echo "$FILE DOES NOT EXIST"
    echo "EXITING SCRIPT"
    exit 1
fi
VER=`date -u +'%Y%m%d'`
if [ -d .git ]
then
    COMMIT_ID=$(git rev-parse --verify HEAD)
    COMMIT_ID=${COMMIT_ID:0:8}
    VER="${VER}_${COMMIT_ID}"
fi
TAG=${PWD##*/}
sudo VER=$VER docker-compose -p $TAG up -d --build --force-recreate
echo "BUILD FROM $FILE COMPLETE"
exit 0