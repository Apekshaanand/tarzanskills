# a = 'my name is apeksha and my phone number is 7004922419'
# digit=0
# for x in a:
#
#     print(a)
#
#
#
# a = 'my name is apeksha and my email is apekshaanand.aa@gmail.com'
#
#







(			# Start of group
  (?=.*\d)		#   must contains one digit from 0-8
  (?=.*[a-z])		#   must contains one lowercase characters
  (?=.*[A-Z])		#   must contains one uppercase characters
  (?=.*[0-9])       #   must contains numerical no.

              .		#     match anything with previous condition checking
                {8,12}	#        length at least 8 characters and maximum of 12
)			# End of group
