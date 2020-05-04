#string formating

person = {'name': 'Peeyush', 'age': 20}


'''this line is not very appropriate to read'''
# sentence = 'My name is ' + person['name'] + ' and i am ' + str(person['age'])+ ' years old'


#string formating

sentence = 'My name is {} and i am {} years old'.format(person['name'], person['age'])
print(sentence)
#we can also write 



tag ='hi'
text = 'This is me'

#we can also do
sentence1 = '<{0}>{1}</{0}>'.format(tag,text)
print(sentence1)



"""we can also pass keyword in place holders"""
print("My name is {name}".format(name = 'Pk'))



#formating the digit : padding
for i in range(1,11):
	print("the value is {:02}".format(i))   #03,05

print("the value of pi is : {:.2f}".format(3.1451353))  #two decimal places



#use comma between a  long number
print("the comma separated number is {:,.2f}".format(1000**2))




#formating and priting date
import datetime
myDate = datetime.datetime(2016,9,24,12,30,12)
print(myDate)


print("my date is {:%b %d, %y}".format(myDate))
