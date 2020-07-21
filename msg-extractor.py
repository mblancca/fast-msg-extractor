import extract_msg,sys,re

inputmail = input("Name of the msg file: ")

mail = inputmail + r'.msg'
msg = extract_msg.Message(mail)
msg_sender = msg.sender
msg_date = msg.date
msg_subj = msg.subject
msg_message = msg.body

result= r'Results_' + mail + r'.txt'

regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

f = open(result,'w')

f.write('Results from .msg uploaded: \n \n')
f.write('Sender: {}\n'.format(msg_sender))
f.write('Sent On: {}\n'.format(msg_date))
f.write('Subject: {}\n'.format(msg_subj))

f.write('\nLinks detected >>>>>>>>>>>>>>>>>>>>>>>>> \n')
match = re.findall(regex, msg_message)

for m in match:
    #print(m)
    f.write('<{}\n'.format(m))