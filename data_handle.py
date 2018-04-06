import time  
import pandas as pd

def data_handle():
	all_data = pd.DataFrame(pd.read_csv('all_file.csv'))
	#print(all_data.info())

	all_data = all_data.sort_values(by = ['CredIssueTime'])
	handled_data = all_data.loc[:,['CredIssueTime']]
	handled_data = handled_data.values

	tag = all_data.loc[:,['Event1']]

	for i in range(len(handled_data)):
		handled_data[i][0] = time.strptime(handled_data[i][0], "%Y-%m-%d %H:%M:%S") 
		handled_data[i][0] = int(time.mktime(handled_data[i][0])) 
	#print(handled_data)

	return (handled_data, tag)


if __name__ == "__main__":
	handled_data, tag = data_handle()
	print(handled_data)
