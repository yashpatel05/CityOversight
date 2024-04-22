def handle_uploaded_file_photo(f):
    print("------", f.name)
    with open('CityWebsite/static/assets/img/profile_photo/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def handle_uploaded_file(f):
    print("------", f.name)
    with open('CityWebsite/static/assets/img/complain/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def handle_captured_image(f):
    print("------", f.name)
    with open('CityWebsite/static/assets/img/captured_image/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def handle_scanned_image(f):
    print("------", f.name)
    with open('CityWebsite/static/assets/img/scanned_image/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)