#tally xml file processing 
from rest_framework.decorators import api_view
from .utils import process_xml
from django.http import HttpResponse
import io

@api_view(['POST'])
def process_xml_api(request):
    if request.method == 'POST' and request.FILES.get('xml_file'):
        xml_file = request.FILES['xml_file']
        excel_content = process_xml.data_process(xml_file)
        excel_content.columns = ['date', 'transaction_type', 'vch_no', 'ref_no', 'ref_type', 'ref_date', 'debtor', 'ref_amount', 'amount', 'particulars', 'vch_type', 'amount_verified']

        # Create an in-memory Excel file
        excel_buffer = io.BytesIO()
        excel_content.to_excel(excel_buffer, index=False, sheet_name='tally_output')
        excel_buffer.seek(0)  # Move the file pointer to the beginning

        # Create a response with appropriate content type and headers
        response = HttpResponse(excel_buffer.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="sample_excel2.xlsx"'
        return response