sum=0
file=$1
div=$2
path=$3

`truncate -s 0 $file`

for f in $path
do
	lines=`wc -l $f | awk '{print $1}'`
	N=$((lines/div))
	sum=$((sum+N))
	printf -v c "Shuffling data from $f and saving $N lines to $file"
	echo $c
	`shuf -n $N $f >> $file`
done
echo $sum
