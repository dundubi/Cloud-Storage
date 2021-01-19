import dropbox

class TransferData :
    def __init__(self, access_token) :
        self.access_token = access_token

    def upload_file(self, folder_from, folder_to) :
        dbx = dropbox.Dropbox(self.access_token)

        f = open(folder_from, "rb")
        dbx.files_upload(f.read(), folder_to)

def main() :
    access_token = '0o59NTVcSg0AAAAAAAAAARyVLBylt_hapYcioA_ysUYfiCBWA3Ad0des0LuH63Lz' 
    transfer_data = TransferData(access_token) 
    folder_from = 'test.txt'
    folder_to = 'Test/text.txt'

    transfer_data.upload_file(folder_from, folder_to)
    print("done")
main()