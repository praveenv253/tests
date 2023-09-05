#for i in {1..4}; do
#    echo -n "$i "
#    sem -j 4 "python3 -u blah.py $i >out-$i"
#done
while read i; do
	echo -n "$i "
	#sem -j 4 "python3 -u blah.py $i >out-$i"
	sem -j 4 --id testsem "sleep $i && echo $i finished"
done < args.txt
#i=1;
#while (( $i <= 4 )); do
	#echo -n "$i "
	#sem -j 4 "sleep $i && echo $i finished"
	#let i=i+1
#done
tty
echo
echo "Started wait"
sem --wait --id testsem
echo 'Done waiting'
