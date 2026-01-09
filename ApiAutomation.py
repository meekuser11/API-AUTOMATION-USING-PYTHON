# request module to
# work with api's

 
# json module to
# parse and get json\
import requests;
import json
from flask import request;

 
# This function are return the
# json response from given url
def getReq(url):

     
    # handle the exceptions
    try:
       
        # make a get request using requests
        # module and store the result.
        res = requests.get(url)
        print( res);
         
        # return the result after
        # formatting in json.
        return json.dumps(res.json(), indent=4)
    except Exception as ee:
        return f"Message : {ee}"
 
       
# This function are return the
# json response of url and json
# data you send the server  
def postReq(url, data):
   
    # handle the exceptions
    try:
       
        # make a post request with
        # the json data
        res = requests.post(url, json=data)
         
        # return the response after
        # formatting in json.
        return json.dumps(res.json(), indent=4)
    except Exception as er:
        return f"Message : {er}"
 
       
# Driver Code
if __name__ == '__main__':
   
    # always run loop to make
    # menu driven program
    while True:
       
        # handle the exceptions
        try:
            url_inpnew = input("Welcome To Automated Testing: ")
            url_inpnew1 = input("Select the Project ")

           
              
            choice = int(input("1.Get Request\n2.Post Request\n3.Exit\nEnter Choice : "))
             
            # get user choice and perform tasks.
            if choice == 1:
               
                # take a url as a input.
                url_inp = input("Enter a valid get url : ")
                 
                # print the result of the url.
                print(getReq(url_inp))
                 
            elif choice == 2:
               
                # take a url as a input
                url_inp = input("Enter a valid get url : ")
                 
                # take a formal data as input in dictionary.
                data_inp = {
                    "name": input("Name : "),
                    "email": input("Email : ")
                 
                  
                }
                 
                # print the result.
                print(postReq(url_inp, data_inp))
                 
            elif choice == 3:
               
                # if user want to exit.
                exit(0)
                 
        except Exception as e:
            print("Error : ", e)
