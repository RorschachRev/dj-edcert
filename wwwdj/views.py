from django.shortcuts import render
from wwwdj.eth import BC

def index(request):
	return render(request, 'pages/index.html')

# Example Blockchain Query View for Templates
def get_block_number(request):
	w3 = BC().resp.w3
	block_number = w3.eth.blockNumber
	context = {
		'block_number': block_number,
	}
	return render(request, 'pages/index.html', context)
