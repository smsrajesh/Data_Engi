data = {
    'invalid_data': {'gtin': []},
    'valid_data': [
        {
            'brand_name': 'SHEBA',
            'category': {
                'category_name': 'CAT FOOD',
                'segments_name': 'CAT TREATS',
                'subcategory_name': 'CAT TREATS'
            }
        }
    ]
}


print(data['valid_data'][0]['category']['category_name'])