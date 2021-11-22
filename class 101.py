import dropbox

class TransferData:
    def __init__(self,access__token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self._access_token)

    f=open(file_from,'rb')
    dbx.file_upload(f.read(),file_to)

def main():
    access_token=""
    tranferdata=TransferData(access_token)
    file_from=input("enter the file path to transfer ")
    file_to=input("enter the full path to upload to dropbox")
    transferdata.upload_file(file_from,file_to)
    print("file has been moved")
main()
