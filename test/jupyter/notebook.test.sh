#!/usr/bin/env bash
# notebook testing 
# presetup:
# python3 -m ipykernel install --user --name python-cadlabs-eth-model --display-name "Python (NOTEBOOKS)"
#
# 

skip_files="template.ipynb *-checkpoint.ipynb *.nbconvert.ipynb environment_setup.ipynb"

files=$(find $1 -type f -name "*.ipynb" $(printf "! -name %s " $skip_files))
original_dir=$(realpath $1)
error_log_file="$(pwd)/error_file.log"
touch $error_log_file

num_procs=$2
num_jobs="\j"

process_notebook() {
	cd $(dirname $1)
	logfile=logs_$(basename $1).txt
	jupyter nbconvert --ExecutePreprocessor.timeout=1800 --to notebook --execute $(basename $1) &> $logfile
	return_value=$?
	if [[ $return_value -ne 0 ]]; then
		msg="Error $return_value when executing $1."
	    echo $msg
	    cat $logfile
	    echo $msg >> $error_log_file;
	else
		echo "Successfully executed $1."
	fi
	rm $logfile
	cd $original_dir
}

for file in $files; do
	while (( ${num_jobs@P} >= num_procs )); do
		wait -n
	done
	process_notebook $file &
done
while (( ${num_jobs@P} > 0 )); do
	wait -n
done

if [[ -s $error_log_file ]]; then
	cat $error_log_file
	rm $error_log_file
	exit 1
fi
sleep 1
echo "Test script exiting..."
exit 0
