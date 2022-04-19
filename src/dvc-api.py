import dvc.api

resource_url = dvc.api.get_url(
    'storage/train.csv',
    repo = 'https://github.com/ammagamma-tirocinio/dvc_example',
    rev ='master',
    remote = 'gdrive://1Y2KUxdpUyy-LMrdyBsKsT9rBrbrXwubc'
)
print(resource_url)