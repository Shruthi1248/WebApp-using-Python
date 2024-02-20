from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from .models import FormData,FieldData

def home(request):
    
    return render (request,'home.html')

@csrf_exempt
def submit_form_data(request):
    if request.method == 'POST':

        form_data_list = []
        items_list = list(request.POST.items())
        
        for (key1, value1), (key2, value2) in zip(items_list[::2], items_list[1::2]):
            if key1.startswith('form') and key2.endswith('path'):
                form_key= key1
                forms_name = value1 
                Rediretpath_name= value2
             
                form_data = {
                    'form_key': form_key,
                    'Rediretpath_name': Rediretpath_name,
                    'forms_name': forms_name
                }

                form_data_list.append(form_data)

        for form_data in form_data_list:
            FormData.objects.create(**form_data)

 
        return JsonResponse({'success': True})


@csrf_exempt
def submit_field_data(request):
    if request.method == 'POST':
        try:
            form_data_list = []
            items_list = list(request.POST.items())

            for i, (key, value) in enumerate(items_list):
                if 'field' in key:
                    field_key = key
                    field_value = value
                    selection_value = items_list[i + 1][1] if i + 1 < len(items_list) else None
                    
                    
                    required = False
                    readable = False
                    for k, value in items_list[i:]:
                        if 'required' in k:
                            required = value
                            
                        if 'readable' in k:
                            readable = value
                           
                        if required and readable:
                            break
                    
                    
                    form_data = {
                        'field_key': field_key,
                        'field_value': field_value,
                        'selection_value': selection_value,
                        'required': required,
                        'readable': readable
                    }
                    form_data_list.append(form_data)

            for form_data in form_data_list:
                FieldData.objects.create(**form_data)

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)
