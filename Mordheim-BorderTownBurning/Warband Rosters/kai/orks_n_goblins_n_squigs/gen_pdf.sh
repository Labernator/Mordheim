export GOPATH=/home/klaute/Mordheim/Bastelbrothers/toolheim   
TMP_DIR=`pwd`

cd $GOPATH/src

./toolheim386.bin -warband "$TMP_DIR"/kai.mordheim_post6.yml

cd -

mv $GOPATH/src/warband-roaster.pdf .

