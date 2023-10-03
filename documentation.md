# Documentation
## Sample request
##### 1 . Sending video ,sample request
### endpoint `https://frontedhng.onrender.com/videos/`
### method : `post`
 ```
multipart/form-data 
"video": videofile
 ```
##### sample response
```
status: 202
message: created succesfully
id:2
```
##### 2 . Getting video ,sample request
### method : `GET`
### endpoint `https://frontedhng.onrender.com/videos/4`
##### sample response
```
status: 200
video: video
```
##### 2 . Getting transcript ,sample request
### method : `GET`
### endpoint `https://frontedhng.onrender.com/transcript/4`
##### sample response
```
status: 200
transcript: transcription
```
