## STEP - 1
Create the virtual environment then install the requirment packages using below commands  

  	cd nirmatee_prj/tally_process
	pip install -r requirement

## STEP - 2
execute the below command to start the server
 
  	python manage.py runserver

## STEP - 3
Execute the below commands to check the xml to excel convert api
 
  	curl -X POST   http://localhost:8000/api/file/processing/   -H 'Content-Type: multipart/form-data'   -F 'xml_file=@Input.xml' -o new_output.xlsx -v	
