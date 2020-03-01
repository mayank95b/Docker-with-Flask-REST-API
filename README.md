# Flask_with_REST_API


# ------------------------------------ Basics of Flask and Json data-------------------
'''
Note : Difference b/w Web application and Web Service is that :
in most of the cases web services will return json where as Web application
will return web pages i.e. index.html(eg. return render_template("index.html")

All communications b/w server/server,server/browser, browser/browser
will in  some form of text/json (images or videos are invalid.)
# json eg :
{
  "field1" : 3,  # value can be number,string,boolean & array
  "field2" : "abc",
  "boolean" : 1,
  "array" : [1,2,3,4,"abc"],
  "array of objects" :
  [
      {
         "field1" : 1
      },

      {
         "field2" : "abc"
      }
  ],

  "array of nested array":
  [
   {
     "nested array":
     [

         {
            "field2" : "abc",
            "name" : "Mayank"
         }
     ]
   }

   ]
}
'''
