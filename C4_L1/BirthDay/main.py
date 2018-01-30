# Path The Main File To Work: python-docs-samples > appengine > standard > hello_world > main.py

import webapp2                  # For Web Server
import cgi                      # For Escape Html From Users

###############################################################################
#             BirthDay       Task 1                                           #
###############################################################################

import webapp2                  # For Web Server
import cgi                      # For Escape Html From Users

HTML_FORM = """
<form method = "post">                        <!--post to send info to server  -->
       What is your birthday?
       <br>
       <label>
           Month
           <input type = "text" name = "month" value = "%(month)s">    <!-- Value Is Default If User Didn't Input Thing -->
       </label>
       <label>
           Day
           <input type = "text" name = "day" value = "%(day)s">
       </label>
       <label>
           Year
           <input type = "text" name = "year" value = "%(year)s">
       </label>
       <div style = "color :red">%(error)s</div>                       <!-- Error If User's Input Are Not Valid -->
       <br>
       <br>
       <input type="submit">               <!-- Submit User's Inputs -->
   </form>
"""
                            #List of Months
months = ['January',
         'February',
         'March',
         'April',
         'May',
         'June',
         'July',
         'August',
         'September',
         'October',
         'November',
         'December']

# Dict: dictionary
# For Value In months                 e.x: For Loop For List Of Months and back it as Value
# Key[:3].lower()                     e.x: JaN        ....>  convert to jan
# dict(Key[:3].lower(), Value)        e.x: Key: jan ---->  Value: January    and store Key & Value In Map & if i call the [Key] Back to Me the [Value]
# Map Output: {Key: Value}            {'mar': 'March', 'feb': 'February', 'aug': 'August', 'sep': 'September', 'apr': 'April', 'jun': 'June', 'jul': 'July', 'jan': 'January', 'may': 'May', 'nov': 'November', 'dec': 'December', 'oct': 'October'}
month_abbvs = dict((m[:3].lower(), m) for m in months)

def valid_month(month):                                # Function For Month Take Parameter month from User's Input
   if month:                                          # If Month Ture & It Allways Ture
       short_month = month[:3].lower()                # Get First 3 Letters in LowerCase
       return month_abbvs.get(short_month)            # From Map Output take (Key) and Return the (Value)

def valid_day(day):                                    # Function For Day Take Parameter Day from User's Input
   if day and day.isdigit():                          # If Day Ture &  this Day is digit
       day = int(day)                                 # Convert This Day To Int                Hint:- Any Input is String
   if (day > 0 and day <= 31):                        # If Day Between 0 and 31
       return day                                     # Return This Day

def valid_year(year):                                  # Function For Year Take Parameter Year from User's Input
   if year and year.isdigit():                        # If Year Ture &  this Year is digit
       year = int(year)                               # Convert This Year To Int                Hint:- Any Input is String
   if year >= 1900 and year < 2020:                   # If Year Between 0 and 31
       return year                                    # Return This Year

def escape_html(s):                                    # Function To Check If User Enter HTML Code In Fields
   s = cgi.escape(s, quote=True)                      # From Lib cgi --> escape ["] If It In Field
   return s


class MainPage(webapp2.RequestHandler):                # Main Class Take Parameter RequestHandler in webapp2 Lib

   def write_HTML_FORM(self, error = "" , month = "" , day = "" , year = ""): # Function For All Of This Staff Take Parameter Empty As Default

       self.response.out.write(HTML_FORM % {"error" : error,                  # Print HTML_FORM & In HTML_FORM Find %(Key)s and Replace it By [Value]     Hint:- {"Key" : Value}
                                            "month" : escape_html(month),     # If Month False Check If This Input Have ["] Or Not
                                            "day" : escape_html(day),         # If Day False Check If This Input Have ["] Or Not
                                            "year" : escape_html(year)})      # If Year False Check If This Input Have ["] Or Not

   def get(self):                                                  # get Function To Get Info From The Server
       self.write_HTML_FORM()                                      # Call The write_HTML_FORM Function To Send To The Server Empty HTML And Get The Result

   def post(self):                                                 # post Function To Send Info To The Server
       user_month = self.request.get('month')                      # From Html Form Get The Content [User's Input] From Month Field
       user_day =   self.request.get('day')                        # From Html Form Get The Content [User's Input] From Day Field
       user_year =  self.request.get('year')                       # From Html Form Get The Content [User's Input] From Year Field

       month = valid_month(user_month)                             # Call valid_month Function and Send user_month As A Parameter
       day   = valid_day(user_day)                                 # Call valid_month Function and Send user_day As A Parameter
       year  = valid_year(user_year)                               # Call valid_month Function and Send user_year As A Parameter

       if (month and day and year):                                       # If all Of These Inputs are True
           self.redirect('/thanks')                                       # Redirect To ThanksHandler Have Path [/thanks]
       else:                                                              # If Not True [False]
           self.write_HTML_FORM("Please Enter The Valid Data." , user_month , user_day , user_year)    # Call The write_HTML_FORM Function And Send This Error Msg As A Parameter & Still All Inputs Are There

class ThanksHandler(webapp2.RequestHandler):                           # This Class To Reload WebSite Without Asking Me If I Need To Continue
   def get(self):
       self.response.out.write("Thanks! That's a totally valid day.") # Print This Msg

app = webapp2.WSGIApplication([('/', MainPage), ('/thanks' , ThanksHandler)], debug=True)        # Class MainPage For [/ path URL]
