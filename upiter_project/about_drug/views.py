from django.http import HttpResponse
# Импортируем загрузчик.
from django.template import loader

def about_drug_page(request):
    # Подключаем HTML-файл.
    template = loader.get_template('about_drug.html')
    # Передаём в объект HttpResponse 
    # HTML-код из загруженного файла, объект запроса request;
    # и возвращаем этот объект.
    return HttpResponse(template.render({}, request)) 