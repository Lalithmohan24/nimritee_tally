import xml.etree.ElementTree as ET
import pandas as pd
from datetime import datetime

def data_process(input_file):
    data = {
        'Date': [],
        'Transaction Type': [],
        'Vch No.': [],
        'Ref No': [],
        'Ref Type': [],
        'Ref Date': [],
        'Debtor': [],
        'Ref Amount': [],
        'Amount': [],
        'Particulars': [],
        'Vch Type': [],
        'Amount Verified': [],
    }

    tree = ET.parse(input_file)
    root = tree.getroot()

    for voucher in root.findall('.//VOUCHER'):
        date_str = voucher.findtext('DATE', default='')
        date_obj = datetime.strptime(date_str, "%Y%m%d")
        formatted_date = date_obj.strftime("%d-%m-%Y")
        
        for ledger_entry in voucher.findall('.//ALLLEDGERENTRIES.LIST'):
            # Mapping is done to match the given options
            transaction_type_mapping = {
                'Yes': 'Parent',
                'No': 'Child',
                'NA': 'Other'
            }
            transaction_type = ledger_entry.findtext('ISDEEMEDPOSITIVE', default='NA')
            transaction_type = transaction_type_mapping.get(transaction_type, 'NA')

            vch_no = voucher.findtext('VOUCHERNUMBER', default='')
            ref_no = ledger_entry.findtext('BILLALLOCATIONS.LIST/NAME', default='NA')
            ref_type = ledger_entry.findtext('BILLALLOCATIONS.LIST/BILLTYPE', default='NA')
            ref_date = ledger_entry.findtext('BILLALLOCATIONS.LIST/INTERESTCOLLECTION.LIST', default='NA')
            debtor = ledger_entry.findtext('LEDGERNAME', default='')
            ref_amount = ledger_entry.findtext('BILLALLOCATIONS.LIST/AMOUNT', default='NA')
            amount = ledger_entry.findtext('AMOUNT', default='NA')
            particulars = ledger_entry.findtext('BILLALLOCATIONS.LIST/STBILLCATEGORIES.LIST', default='NA')
            vch_type = voucher.findtext('VOUCHERTYPENAME', default='')
            amount_verified = ledger_entry.findtext('BILLALLOCATIONS.LIST/TDSEXPENSEALLOCATIONS.LIST/AMOUNT', default='NA')

            data['Date'].append(formatted_date)
            data['Transaction Type'].append(transaction_type)
            data['Vch No.'].append(vch_no)
            data['Ref No'].append(ref_no)
            data['Ref Type'].append(ref_type)
            data['Ref Date'].append(ref_date)
            data['Debtor'].append(debtor)
            data['Ref Amount'].append(ref_amount)
            data['Amount'].append(amount)
            data['Particulars'].append(particulars)
            data['Vch Type'].append(vch_type)
            data['Amount Verified'].append(amount_verified)

    df = pd.DataFrame(data)
    return df