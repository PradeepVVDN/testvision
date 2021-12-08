filename=$0
[ -d result ] && echo "Result Directory Already Exists" || mkdir result
echo " This is simple test to evolute the test PASSed or FAILed" >> $PWD/result/"result_${filename%.*}".log
sleep 5
exit 1
