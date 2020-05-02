#string
message = "Hello World"

print(len(message))
print(message[-1:])
print(message.count('l'))
newMessage = message.replace('World','Universe')
print(newMessage)

#if we set 
message = message.replace('l','p')
print(message)


greetings = 'Hello'
name = 'LetsCode'

#place holders
mesg = '{}, {}.welcom'.format(greetings, name)
print(mesg)



print(dir(name)) #give all the funciton of string

print(help(str))