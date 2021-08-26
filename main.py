from document_processing import download_file, fill_file_fields, upload_file

fields = {
    '[Client]': 'Jean',
    '[Client legal name]': 'Jean Carlos Marinos'
}

download_file()
fill_file_fields(fields)
upload_file()
